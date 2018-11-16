<template>
  <div class="page-book">
    <div class="row">
      <div class="col-12 col-md-8">
        <h3>Contacts</h3>

        <ContactList></ContactList>
      </div>
    </div>
  </div>
</template>

<script>
import ContactList from './ContactList.vue';

// I had originally planned to do a lot more UI on this page - a way to view details without editing the contact
// a better search results experience, perhaps grouped by "field" markers
// due to time I was not able to get to it, but they were in my mind

export default {
  components : {
    ContactList
  },
  data () {
    return {
      
    }
  },
  methods: {
    
  },
  created () {
    
  }
}
</script>



<style lang="scss" scoped>



</style>
