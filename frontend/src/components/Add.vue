<template>
  <div class="page-add">
    <div class="row">
      <div class="col-12 col-md-8">
        <h3 class="mb-4">Add Contact</h3>

        <div class="form">
        	<div class="row">
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="firstname">First Name</label>
						    <input v-model="contact.firstname" type="text" class="form-control" id="firstname" placeholder="Jane">
						  </div>
        		</div>
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="lastname">Last Name</label>
						    <input v-model="contact.lastname" type="text" class="form-control" id="lastname" placeholder="Doe">
						  </div>
        		</div>
        	</div>

        	<div class="row">
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="dob">Date of Birth</label>
						    <input v-model="contact.date_of_birth" type="date" class="form-control" id="dob">
						  </div>
        		</div>
        	</div>

        	<div class="row">
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="address">Address</label>
						    <textarea v-model="contact.address" class="form-control" id="address"></textarea>
						  </div>
        		</div>
        	</div>

        	<div class="row">
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="phone">Phone Number</label>
						    <input v-model="contact.number" type="text" class="form-control" id="phone" placeholder="555-555-5555">
						  </div>
        		</div>
        	</div>

        	<div class="row">
        		<div class="col-12 col-md-8">
        			<div class="form-group">
						    <label for="dob">Email</label>
						    <input v-model="contact.email" type="text" class="form-control" id="email" placeholder="your@email.com">
						  </div>
        		</div>
        	</div>

        	<div class="footer mt-3">
        		<a class="button" v-on:click.prevent="save">Add Contact</a>
        	</div>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  data () {
    return {
      contact : {
      	firstname : '',
      	lastname : '',
      	date_of_birth : '',
      	address : '',
      	number : '',
      	email : '',
      },
    }
  },
  methods: {
    
    save () {
      let self = this;

      if(this.contact.firstname.length == 0 && this.contact.lastname.length == 0){
        return;
      }

    	axios({        
        method:'POST',
        url: '/api/contact',
        headers: {
            'Content-type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
         },
        data: this.contact,
	    }).then(function (response){
        if(response.data){
        	self.$router.push({ path: '/' });
        }
	    })
	    .catch(function (error) {
	    	console.log(error);
	    });
    }

  },

  created () {
    
  }
}
</script>



<style lang="scss" scoped>



</style>
