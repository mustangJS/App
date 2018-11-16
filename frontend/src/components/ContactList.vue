

<template>
  <div class="contact-list-module">
    <div class="search-form">
      <div class="input">
        <svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <g stroke="none" stroke-width="1" fill="#000000" fill-rule="evenodd">
            <g>
              <path d="M12.9056439,14.3198574 C11.5509601,15.3729184 9.84871145,16 8,16 C3.581722,16 0,12.418278 0,8 C0,3.581722 3.581722,0 8,0 C12.418278,0 16,3.581722 16,8 C16,9.84871145 15.3729184,11.5509601 14.3198574,12.9056439 L19.6568542,18.2426407 L18.2426407,19.6568542 L12.9056439,14.3198574 Z M8,14 C11.3137085,14 14,11.3137085 14,8 C14,4.6862915 11.3137085,2 8,2 C4.6862915,2 2,4.6862915 2,8 C2,11.3137085 4.6862915,14 8,14 Z"></path>
            </g>
          </g>
        </svg>
        <input type="text" placeholder="Search..." v-model="query">
      </div>
    </div>

    <div class="contact-list">
      <div class="contact-item" v-for="contact in results" :key="contact.id">
        <div class="head">
          <span class="name">{{ displayName(contact) }}</span>

          <router-link v-bind:to="'/edit/' + contact.id" class="link">edit</router-link>
        </div>
        <div class="body swing-medium">
          <div class="contact-content">
            <div class="row">
              <div class="col-12 col-md-8 field">
                <div class="label">Birthday</div>
                <div class="field-value">{{ contact.date_of_birth }}</div>
              </div>
              <div class="col-12 col-md-8 field">
                <div class="label">Addresses</div>
                <div class="field-value" v-for="address in contact.addresses">{{ address.address }}</div>
              </div>
              <div class="col-12 col-md-8 field">
                <div class="label">Phone Numbers</div>
                <div class="field-value" v-for="number in contact.numbers">{{ number.phone }}</div>
              </div>
              <div class="col-12 col-md-8 field">
                <div class="label">Emails</div>
                <div class="field-value" v-for="email in contact.emails">{{ email.email }}</div>
              </div>
            </div>
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
      contacts : [],
      query : '',
      results : [],
    }
  },
  watch: {
    query : function(val){
      this.filterContacts(val)
    }
  },
  methods: {
    displayName (contact) {
      let display = '';

      if(contact.lastname.length) {
        display += contact.lastname;

        if(contact.firstname.length) {
          display += ', ';
        }
      }

      if(contact.firstname.length) {
        display += contact.firstname;
      }

      return display;
    },

    filterContacts (newVal) {
      // this simple search only searches the name fields for matching values
      // again, prob not a good solution or presentation, but in the interest of time
      // this is a basic search that works for names

      if(this.query.length == 0){
        this.results = this.contacts;
        return;
      }
      else
      {
        let self = this;

        let results = [];

        this.results = this.contacts.filter((contact) => {
          let checkFirst = false;
          let checkLast = false;
          
          if(contact.firstname.length){
            checkFirst = true;
          }

          if(contact.lastname.length){
            checkLast = true;
          }

          if(checkFirst && checkLast)
          {
            return (contact.firstname.trim().toLowerCase().indexOf(self.query.toLowerCase()) > -1)
            ||
            (contact.lastname.trim().toLowerCase().indexOf(self.query.toLowerCase()) > -1);
          }
          else if(checkFirst && !checkLast)
          {
            return (contact.firstname.trim().toLowerCase().indexOf(self.query.toLowerCase()) > -1);
          }
          else if(!checkFirst && checkLast)
          {
            return (contact.lastname.trim().toLowerCase().indexOf(self.query.toLowerCase()) > -1);
          }
          
        });
      }
    },

    fetchContacts () {
      axios.get('/api/all')
      .then(response => {
        this.contacts = response.data;
        this.results = response.data;
        this.filterContacts('');
      })
      .catch(error => {
        console.log(error)
      });
    },
  },
  created () {
    this.fetchContacts();
  }
}
</script>



<style lang="scss" scoped>

.search-form{
  margin:2em 0;

  .input{
    position:relative;
    box-shadow:0px 2px 4px rgba(0,0,0,.1);

    svg{
      opacity:0.2;
      position:absolute;
      top:50%;
      left:13.5px;
      transform:translateY(-50%);
      height:20px;
    }

    input{
      width:100%;
      padding-left:50px;
      height:45px;
      outline:none !important;
      border:none;
      border-radius:5px;

      &::-webkit-input-placeholder{ 
        color:rgba(0,0,0,.2);
      }
      &:-ms-input-placeholder { 
        color:rgba(0,0,0,.2);
      }
      &:-moz-placeholder{ 
        color:rgba(0,0,0,.2);
      }
      &::-moz-placeholder { 
        color:rgba(0,0,0,.2);
      }
    }
  }
}

.contact-list{
  border:1px solid #ddd;
  border-radius:4px;
  box-shadow:0px 2px 4px rgba(0,0,0,.1);
  background:#FFF;

  .contact-item{
    position:relative;
    border-radius:0px;

    &:first-child{
      border-top-left-radius:0px;
      border-top-right-radius:0px;
    }

    &:last-child{
      border-bottom-left-radius:0px;
      border-bottom-right-radius:0px;
    }
    
    .head{
      cursor:pointer;
      padding:1.5em;
      position:relative;

      a{
        position:absolute;
        top:50%;
        right:15px;
        transform:translateY(-50%);
      }
      
      .name{
        display:block;
        font-size:18px;
        color:#5a5a5a;
        font-weight:300;
        opacity:0.6;
      }

      svg{
        position:absolute;
        top:15px;
        right:20px;
        width:50px;
        height:50px;
        padding:10px;
        border-radius:100%;
        background:transparent;
        opacity:0.2;
      }
    }

    .body{
      padding:1.5em;
      display:none;

      .contact-content{
        padding-left:10px;
        overflow-y:scroll;
        overflow-x:hidden;
        max-height:calc(200px - 3em);
        width:100%;
      }

      .field{
        padding-bottom:2em;
      }

      .label{
        color:#5a5a5a;
        opacity:0.6;
        font-size:14px;
        text-transform:uppercase;
        letter-spacing:2px;
        font-weight:700;
        margin-bottom:5px;
      }

      .field-value{
        font-weight:400;
        color:#5a5a5a;
        font-size:13px;
        display:block;
        margin-bottom:10px;
      }
    }
  }
}

</style>
