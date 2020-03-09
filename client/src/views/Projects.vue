<template>
  <div>
    <br>
    <h1>Projects</h1>
    <h5>Games and programs made by students inside and outside of class.</h5>
    <br>
    <b-button v-on:click="get()">Click Me to Send API Request</b-button>
    <div class="carddiv">
      <b-card-group deck columns>
        <Project 
          class="mx-auto"
          title="Hello" 
          name="Aiden" 
          createDate="10-10-10" 
          info="this is a test of our project component" 
          uploadDate="1-1-1" 
        />
        <!-- <Project
          v-if="loaded"
          class="mx-auto"
          title="projects[projects.length-1].data.title"
          name=projects[projects.length-1].data.name
          createDate=this.projects[projects.length-1].data.createDate
          info=this.projects[projects.length-1].data.info
          uploadDate=this.projects[projects.length-1].data.uploadDate
        /> -->
        <Project
          v-for="project in projects"
          v-bind:key="project.id"
          v-bind:name="project.name"
        />
      </b-card-group>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import Project from '@/components/ProjectComponent'

const URL = "http://10.40.17.230:5000"

export default {
  name:'Projects',
  components: {
    Project
  },
  data() {
    return {
      loaded: false,
      projects: [
      ],
    }
  },
  methods: {
    get: function () {
      axios.get(URL + "/api/v1.0/card")
        .then(response => {
          this.projects.push(response)
          console.log(this.projects[this.projects.length - 1].data)
          this.loaded = true
          this.projects[this.projects.length - 1].id = this.projects.length - 1
        })
    },
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