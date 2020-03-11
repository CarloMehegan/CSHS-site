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
        <Project
          v-for="p in projects"
          class="mx-auto"
          v-bind:key="p._id"
          :title="p.title"
          :name="p.name"
          :createDate="p.createDate"
          :info="p.info"
          :uploadDate="p.uploadDate"
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
      projects: [],
    }
  },
  methods: {
    get: function () {
      axios.get(URL + "/api/v1.0/card")
        .then(response => {
          // let res1 = [
          //   {
          //     "id": 1,
          //     "name": "Hello"
          //   },
          //   {
          //     "id": 2,
          //     "name": "World"
          //   }
          // ]
          console.log(response);
          for(var i = 0; i < response.data.length; i++) {
            this.projects.push(response.data[i])
          }
          
          
          // this.projects.push(response)
          // console.log(this.projects[this.projects.length - 1].data)
          // this.loaded = true
          // this.projects[this.projects.length - 1].id = this.projects.length - 1
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