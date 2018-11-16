from flask import Flask, render_template, jsonify, request
import json
import pprint
from random import *
from flask_cors import CORS
import requests
from flask_sqlalchemy import SQLAlchemy
import contextlib
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeclarativeMeta
import sys


app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

# used this for testing, ran frontend on a node.js server for rapid development
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(80), nullable=True)
	lastname = db.Column(db.String(80), nullable=True)
	date_of_birth = db.Column(db.String(80), nullable=True)
	addresses = db.relationship('Address', backref='contact', lazy=True)
	numbers = db.relationship('Number', backref='contact', lazy=True)
	emails = db.relationship('Email', backref='contact', lazy=True)

	@property
	def serialize(self):
		return {
			'id'            : self.id,
			'firstname'     : self.firstname,
			'lastname'      : self.lastname,
			'date_of_birth' : self.date_of_birth,
			# This is an example how to deal with Many2Many relations
			'addresses'  : self.serialize_addresses,
			'numbers'  : self.serialize_numbers,
			'emails'  : self.serialize_emails
		}

	@property
	def serialize_addresses(self):
		return [ item.serialize for item in self.addresses]

	@property
	def serialize_numbers(self):
		return [ item.serialize for item in self.numbers]

	@property
	def serialize_emails(self):
		return [ item.serialize for item in self.emails]

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(255), nullable=True)
	contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

	@property
	def serialize(self):
		return {
			'id'         : self.id,
			'address'    : self.address,
			'contact_id' : self.contact_id,
		}

class Number(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	phone = db.Column(db.String(255), nullable=True)
	contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

	@property
	def serialize(self):
		return {
			'id'         : self.id,
			'phone'      : self.phone,
			'contact_id' : self.contact_id,
		}

class Email(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), nullable=True)
	contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

	@property
	def serialize(self):
		return {
			'id'         : self.id,
			'email'      : self.email,
			'contact_id' : self.contact_id,
		}


# create the database, clear anything existing
db.drop_all(bind=None)
db.create_all()

# add a record to it to test retrieving
contact = Contact(firstname='Eric', lastname='Diviney')

db.session.add(contact)
db.session.commit()
db.session.flush()

address = Address(address='2626 Colby St', contact_id=contact.id)
number = Number(phone='903 767 6775', contact_id=contact.id)
email = Email(email='eric@brickwallagency.com', contact_id=contact.id)

db.session.add(address)
db.session.add(number)
db.session.add(email)

db.session.commit()
db.session.flush()

# end database initialization





# data validation throughout the app is basically verify ANYTHING non-empty is being passed
# no input-validation of emails, addresses, or phone number
# this was skipped solely in the interest of time

# also, did not really consider database restrictions such as unique numbers / emails
# in a production app I would think two unique contact having the same number/email should trigger some
# type of error, but for simplicity sake was left out of this app

@app.route('/api/all')
def getAll():
	return jsonify([i.serialize for i in Contact.query.all()])

@app.route('/api/contact', methods=['POST'])
def createContact():
	data = request.get_json()

	contact = Contact(firstname=data['firstname'], lastname=data['lastname'], date_of_birth=data['date_of_birth'])

	db.session.add(contact)
	db.session.commit()

	# send to database so we can get the contact id back
	db.session.flush()

	if 'address' in data:
		if len(data['address']):
			address = Address(address=data['address'], contact_id=contact.id)
			db.session.add(address)

	if 'number' in data:
		if len(data['number']):
			number = Number(phone=data['number'], contact_id=contact.id)
			db.session.add(number)

	if 'email' in data:
		if len(data['email']):
			email = Email(email=data['email'], contact_id=contact.id)
			db.session.add(email)

	db.session.commit()

	return jsonify([contact.serialize])

@app.route('/api/contact/<int:contact_id>/address', methods=['POST'])
def addAddress(contact_id):
	data = request.get_json()
	
	contact = Contact.query.get(contact_id)
	
	if len(data['address']):
		address = Address(address=data['address'], contact_id=contact.id)
		db.session.add(address)
		db.session.commit()

	return jsonify([contact.serialize])

@app.route('/api/contact/<int:contact_id>/number', methods=['POST'])
def addPhone(contact_id):
	data = request.get_json()
	
	contact = Contact.query.get(contact_id)

	if len(data['number']):
		phone = Number(phone=data['number'], contact_id=contact.id)
		db.session.add(phone)
		db.session.commit()

	return jsonify([contact.serialize])

@app.route('/api/contact/<int:contact_id>/email', methods=['POST'])
def addEmail(contact_id):
	data = request.get_json()
	
	contact = Contact.query.get(contact_id)
	
	if len(data['email']):
		email = Email(email=data['email'], contact_id=contact.id)
		db.session.add(email)
		db.session.commit()

	return jsonify([contact.serialize])


@app.route('/api/contact/<int:contact_id>', methods=['POST', 'GET'])
def contact(contact_id):
	contact = Contact.query.get(contact_id)

	if request.method == 'POST':
		data = request.get_json()

		contact.firstname = data['firstname']
		contact.lastname = data['lastname']
		contact.date_of_birth = data['date_of_birth']

		db.session.add(contact)
		db.session.commit()

	return jsonify([contact.serialize])


## for some reason, was having trouble with the methods=['DELETE'] for the following two routes
## was hoping to be more RESTful, but in the interest of time just wrote two simple POST endpoints
## for deleting resources. Did not have time to fully investigate DELETE HTTP issue

@app.route('/api/delete', methods=['POST'])
def deleteContact():
	data = request.get_json()

	contact = Contact.query.get(data['id'])
	contact.addresses = []
	contact.numbers = []
	contact.emails = []

	db.session.delete(contact)
	db.session.commit()
	db.session.flush()

	return jsonify({ 'message' : 'success' })


@app.route('/api/delete/attribute', methods=['POST'])
def deleteAttribute():
	data = request.get_json()

	if 'address' in data:
		address = Address.query.get(data['id'])
		db.session.delete(address)

	if 'phone' in data:
		number = Number.query.get(data['id'])
		db.session.delete(number)

	if 'email' in data:
		email = Email.query.get(data['id'])
		db.session.delete(email)

	db.session.commit()
	db.session.flush()

	contact = Contact.query.get(data['contact_id'])

	return jsonify([contact.serialize])
		


@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
  return render_template("index.html")


