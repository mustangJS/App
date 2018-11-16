<template>
  <div id="app">
    <div class="navigation">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-12 col-md-4 col-lg-3">
            <img src="./assets/sf.png">
          </div>
          <div class="col-12 col-md-8 col-lg-9">
            <ul class="list-inline my-0">
              <li class="list-inline-item">
                <router-link to="/">Contacts</router-link>
              </li>
              <li class="list-inline-item">
                <router-link to="/add">+ Add New</router-link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="content container">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss" scoped>

.navigation{
  background:#FFF;
  padding-top:2em;
  padding-bottom:2em;
  box-shadow:0px 2px 4px rgba(0,0,0,.05);

  @media(max-width:992px){
    text-align:center;
  }

  img{
    width:200px;
    max-width:100%;

    @media(max-width:992px){
      margin-bottom:15px;
    }
  }

  li{
    margin:0 15px;
  }

  a{
    color:#09cfc0 !important;
  }
}

.content{
  padding-top:4em;
  padding-bottom:4em;
}

</style>
