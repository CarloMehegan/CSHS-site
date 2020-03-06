<template>
  <b-card
    no-body
    style="max-width: 20rem;"
    img-src="../assets/code3.jpg"
    img-alt="code"
    img-top
    class = "projectcard"
    >
    <template v-slot:header>
      <h4 class="mb-0">Underwater</h4>
    </template>

    <b-card-body>
      <b-card-title>Carlo Mehegan</b-card-title>
      <b-card-sub-title class="mb-2">October 2, 2019</b-card-sub-title>
      <b-card-text>
          I made this in AP Computer Science Principles. It is a simulation of an ocean with fish of random sizes swimming through the water.
      </b-card-text>
    </b-card-body>

    <b-list-group flush>
      <b-list-group-item>Javascript</b-list-group-item>
      <b-list-group-item>p5.js</b-list-group-item>
      <b-list-group-item>AP Computer Science Principles</b-list-group-item>
      <b-list-group-item>Simulation</b-list-group-item>
    </b-list-group>

    <b-card-body>
      <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Carlo's profile</a>
    </b-card-body>

    <b-card-footer>Uploaded March 5, 2020</b-card-footer>

    <!-- <b-card-img src="../assets/code3.jpg" alt="code" bottom></b-card-img> -->
  </b-card>
</template>