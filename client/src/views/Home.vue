<template>
  <div class="home">
    <!-- <b-button v-on:click="get()">Click Me to Send API Request</b-button> -->
    <h1>Computer Science Honor Society</h1>
    <h2>What is Computer Science?</h2>
    <p>Computer Science is the study of computer technology, including hardware, software, networks, and the Internet.The career is focused on programming using mathematical algorithms.</p>
    <h2>General Information about HHS Computer Science</h2>
    <p>Computer Science is growing rapidly at Harrisonburg High School, from 1 course in 2004 to 24 courses in 2019.</p>
    <h2>Career in Computer Science</h2>
    <p>According to the U.S. Bureau of Labor Statistics, the principle fact-finding agency for the United States government, and a principle agency of the U.S. Federal Statistical System; Computer Science industry is expected to grow much faster than other careers in the next 10 years. Therefore, if you want a high-paying job, Computer Science is a perfect choice.</p>
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

<style>
.home {
  margin: auto;
  width: 60%;
}
</style>
