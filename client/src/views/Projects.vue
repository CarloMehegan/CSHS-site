<template>
  <div>
    <br>
    <h1>Projects</h1>
    <h5>Games and programs made by students inside and outside of class.</h5>
    <br>
    <div class = "carddiv">
      <b-card-group deck columns>
        <Project 
          title="Hello" 
          name="Aiden" 
          createDate="10-10-10" 
          info="this is a test of our project component" 
          uploadDate="1-1-1-" 
        />
      </b-card-group>
    </div>
  </div>
</template>

<script>
import Project from '@/components/ProjectComponent'

export default {
  name:'Projects',
  components: {
    Project
  }
}
</script>


<style>

.carddiv {
  padding-right: 5%;
  padding-left: 5%;
  /* margin: auto;
  display: block;
  margin-left: auto;
  margin-right: auto;
  float: center; */
  /* float: center; */
  
  /* width: 90vw; i HATE THIS HOW DO I CENTER IT*/
}

.projectcard {
  min-width: 300px;
  max-width: 300px;
  
}

</style>