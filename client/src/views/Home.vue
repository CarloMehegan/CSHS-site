<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <b-button v-on:click="get()">Click Me to Send API Request</b-button>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios"

const URL = "http://127.0.0.1:5000"

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  methods: {
    get: function () {
      axios
      .get(URL + "/api/v1.0/hello")
      .then(response => (console.log(response)))
    }
  }
};
</script>
<style scoped>
#home {
  padding: 10000px;
}
</style>
