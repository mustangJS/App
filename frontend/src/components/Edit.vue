<template>
  <div class="page-add">
    <div class="row">
      <div class="col-12 col-md-8">
        <h3 class="mb-4">Edit Contact: {{ contact.firstname }} {{ contact.lastname }}</h3>

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
						    <label for="address">Addresses</label>
						    
                <div class="contact-attribute-value" v-for="attr in addresses">
                  <span>{{ attr.address }}</span>

                  <a href="#" class="attribute-delete" v-on:click.prevent="deleteAttribute(attr)">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M2,2 L18,2 L18,4 L2,4 L2,2 Z M8,0 L12,0 L14,2 L6,2 L8,0 Z M3,6 L17,6 L16,20 L4,20 L3,6 Z M8,8 L9,8 L9,18 L8,18 L8,8 Z M11,8 L12,8 L12,18 L11,18 L11,8 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

                <div class="contact-attribute-field">
                  <input v-model="newAddress" placeholder="Add Another Address" type="text" class="form-control" id="dob">
                  <a href="#" class="attribute-add" v-on:click.prevent="addAttribute('address')">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M11,9 L11,5 L9,5 L9,9 L5,9 L5,11 L9,11 L9,15 L11,15 L11,11 L15,11 L15,9 L11,9 Z M10,20 C15.5228475,20 20,15.5228475 20,10 C20,4.4771525 15.5228475,0 10,0 C4.4771525,0 0,4.4771525 0,10 C0,15.5228475 4.4771525,20 10,20 Z M10,18 C14.418278,18 18,14.418278 18,10 C18,5.581722 14.418278,2 10,2 C5.581722,2 2,5.581722 2,10 C2,14.418278 5.581722,18 10,18 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

						  </div>
        		</div>
        	</div>

          <div class="row">
            <div class="col-12 col-md-8">
              <div class="form-group">
                <label for="address">Numbers</label>
                
                <div class="contact-attribute-value" v-for="attr in numbers">
                  <span>{{ attr.phone }}</span>

                  <a href="#" class="attribute-delete" v-on:click.prevent="deleteAttribute(attr)">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M2,2 L18,2 L18,4 L2,4 L2,2 Z M8,0 L12,0 L14,2 L6,2 L8,0 Z M3,6 L17,6 L16,20 L4,20 L3,6 Z M8,8 L9,8 L9,18 L8,18 L8,8 Z M11,8 L12,8 L12,18 L11,18 L11,8 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

                <div class="contact-attribute-field">
                  <input v-model="newNumber" placeholder="Add Another Number" type="text" class="form-control" id="dob">
                  <a href="#" class="attribute-add" v-on:click.prevent="addAttribute('number')">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M11,9 L11,5 L9,5 L9,9 L5,9 L5,11 L9,11 L9,15 L11,15 L11,11 L15,11 L15,9 L11,9 Z M10,20 C15.5228475,20 20,15.5228475 20,10 C20,4.4771525 15.5228475,0 10,0 C4.4771525,0 0,4.4771525 0,10 C0,15.5228475 4.4771525,20 10,20 Z M10,18 C14.418278,18 18,14.418278 18,10 C18,5.581722 14.418278,2 10,2 C5.581722,2 2,5.581722 2,10 C2,14.418278 5.581722,18 10,18 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-12 col-md-8">
              <div class="form-group">
                <label for="address">Emails</label>
                
                <div class="contact-attribute-value" v-for="attr in emails">
                  <span>{{ attr.email }}</span>

                  <a href="#" class="attribute-delete" v-on:click.prevent="deleteAttribute(attr)">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M2,2 L18,2 L18,4 L2,4 L2,2 Z M8,0 L12,0 L14,2 L6,2 L8,0 Z M3,6 L17,6 L16,20 L4,20 L3,6 Z M8,8 L9,8 L9,18 L8,18 L8,8 Z M11,8 L12,8 L12,18 L11,18 L11,8 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

                <div class="contact-attribute-field">
                  <input v-model="newEmail" placeholder="Add Another Email" type="text" class="form-control" id="dob">
                  <a href="#" class="attribute-add" v-on:click.prevent="addAttribute('email')">
                    <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g stroke="none" stroke-width="1" fill="#000" fill-rule="evenodd">
                        <g>
                          <path d="M11,9 L11,5 L9,5 L9,9 L5,9 L5,11 L9,11 L9,15 L11,15 L11,11 L15,11 L15,9 L11,9 Z M10,20 C15.5228475,20 20,15.5228475 20,10 C20,4.4771525 15.5228475,0 10,0 C4.4771525,0 0,4.4771525 0,10 C0,15.5228475 4.4771525,20 10,20 Z M10,18 C14.418278,18 18,14.418278 18,10 C18,5.581722 14.418278,2 10,2 C5.581722,2 2,5.581722 2,10 C2,14.418278 5.581722,18 10,18 Z"></path>
                        </g>
                      </g>
                    </svg>
                  </a>
                </div>

              </div>
            </div>
          </div>

        	<div class="footer mt-3 text-right">
            <a class="link" v-on:click.prevent="remove">Delete</a>
        		<a class="button" v-on:click.prevent="save">Save</a>
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
      },
      
      addresses : [],
      numbers : [],
      emails : [],

      newAddress : '',
      newNumber : '',
      newEmail : '',

    }
  },
  methods: {

    deleteAttribute (attr) {
      let self = this; 
      
      axios({        
        method:'POST',
        url: '/api/delete/attribute',
        headers: {
            'Content-type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
         },
        data: attr,
      }).then(function (response){
        self.contact = response.data[0];
        self.addresses = response.data[0].addresses;
        self.numbers = response.data[0].numbers;
        self.emails = response.data[0].emails;
      })
      .catch(function (error) {
        console.log(error);
      });
    },

    fetchContact () {
      axios.get('/api/contact/' + this.$route.params.id)
      .then(response => {
        this.contact = response.data[0];
        this.addresses = response.data[0].addresses;
        this.numbers = response.data[0].numbers;
        this.emails = response.data[0].emails;
      })
      .catch(error => {
        console.log(error);
      });
    },

    addAttribute (type) {
      let builtURL = '/api/contact/' + this.contact.id;
      
      let postData = {
        contact_id : this.contact.id
      };

      switch(type){
        case 'address':
          builtURL += '/address';
          postData['address'] = this.newAddress;
          this.newAddress = '';
          break;
        case 'number':
          builtURL += '/number';
          postData['number'] = this.newNumber;
          this.newNumber = '';
          break;
        case 'email':
          builtURL += '/email';
          postData['email'] = this.newEmail;
          this.newEmail = '';
          break;
        default:
            
          break;
      }

      let self = this; 
      axios({        
        method:'POST',
        url: builtURL,
        headers: {
            'Content-type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        },
        data: postData,
      }).then(function (response){
        if(response.data){
          self.contact = response.data[0];
          self.addresses = response.data[0].addresses;
          self.numbers = response.data[0].numbers;
          self.emails = response.data[0].emails;
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    },

    remove () {
      let self = this; 
      axios({        
        method:'POST',
        url: '/api/delete',
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
    },
    
    save () {
      let self = this; 
    	axios({        
        method:'POST',
        url: '/api/contact/' + this.contact.id,
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
    this.fetchContact();
  }
}
</script>



<style lang="scss" scoped>

  .footer{
    a{
      margin-left:20px;
    }
  }

  .contact-attribute-value{
    position:relative;
    padding:5px;

    .attribute-delete{
      position:absolute;
      right:5px;
      top:50%;
      transform:translateY(-50%);
      svg{
        width:20px;
        opacity:0.2;
      }
    }
  }
  
  .contact-attribute-field{
    position:relative;

    input{
      padding-right:50px;
    }

    .attribute-add{
      position:absolute;
      right:5px;
      top:50%;
      transform:translateY(-50%);
      svg{
        width:20px;
        opacity:0.2;
      }
    }
  }

</style>
