<template>
  <div class="home">
    <b-button v-on:click="get()">Click Me to Send API Request</b-button>


  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios"

const URL = "http://127.0.0.1:5000"

export default {
  name: "Home",
  components: {
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
