<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-nav>  
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/Classes">Classes</b-nav-item>
          <b-nav-item to="/Projects">Projects</b-nav-item>
          <b-nav-item to="/Create">Create</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/Account" right>Account</b-nav-item>
          <b-nav-item to="/SignIn" right>Sign In</b-nav-item>
        </b-navbar-nav>

      </b-navbar>
    </div>
    <router-view />
  </div>
  
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 1px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
