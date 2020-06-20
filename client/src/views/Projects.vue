<template>
  <div>
    <br>
    <h1>Projects</h1>
    <h5>Games and programs made by students inside and outside of class.</h5>
    <br>
    <!-- <b-button v-on:click="get()">Click Me to Send API Request</b-button> -->
    <div class="carddiv">
      <b-card-group deck columns>
        <Project
          v-for="p in projects"
          class="mx-auto"
          v-bind:key="p._id"
          :p="p"
        />
      </b-card-group>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import Project from '@/components/ProjectComponent'

const URL = "http://localhost:5000"

export default {
  name:'Projects',
  components: {
    Project
  },
  data() {
    return {
      projects: [],
    }
  },
  methods: {
    get: function () {
      axios.get(URL + "/api/v1.0/posts")
        .then(response => {
          console.log(response);
          for(var i = 0; i < response.data.length; i++) {
            this.projects.push(response.data[i])
          }
        })
    },
  },
  beforeMount: function(){
    this.get()
  }
}
</script>


<style>

.carddiv {
  padding-right: 5%;
  padding-left: 5%;

}

.projectcard {
  min-width: 300px;
  max-width: 300px;
  
}

</style>