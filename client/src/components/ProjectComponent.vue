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
      <h4 class="mb-0">{{ title }}</h4>
    </template>

    <b-card-body>
      <b-card-title>{{ name }}</b-card-title>
      <b-card-sub-title class="mb-2">{{ createDate }}</b-card-sub-title>
      <b-card-text>
          {{ info }}
      </b-card-text>
    </b-card-body>

    <b-list-group flush>
      <!-- <b-list-group-item>Javascript</b-list-group-item>
      <b-list-group-item>p5.js</b-list-group-item>
      <b-list-group-item>AP Computer Science Principles</b-list-group-item>
      <b-list-group-item>Simulation</b-list-group-item> -->
    </b-list-group>

    <b-card-body>
      <!-- <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Carlo's profile</a> -->
    </b-card-body>

    <b-card-footer>{{ uploadDate}}</b-card-footer>

    <!-- <b-card-img src="../assets/code3.jpg" alt="code" bottom></b-card-img> -->
  </b-card>
</template>

<script>
export default {
  name: "projectCard",
  props: {
    title: String,
    name: String,
    createDate: String,
    info: String,
    uploadDate: String
  }
}
</script>