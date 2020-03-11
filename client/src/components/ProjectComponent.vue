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
      <h4 class="mb-0">{{ p.title }}</h4>
    </template>

    <b-card-body>
      <b-card-title>{{ p.name }}</b-card-title>
      <b-card-sub-title class="mb-2">{{ p.createDate }}</b-card-sub-title>
      <b-card-text>
          {{ p.info }}
      </b-card-text>
    </b-card-body>

    <b-row>

      <b-col v-for="t in p.tags" v-bind:key=t>
        <a v-bind:href="t">{{ t }} </a>
      </b-col>

    </b-row>

    <b-card-body>
      <!-- <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Carlo's profile</a> -->
    </b-card-body>

    <b-card-footer>{{ p.uploadDate}}</b-card-footer>

    <!-- <b-card-img src="../assets/code3.jpg" alt="code" bottom></b-card-img> -->
  </b-card>
</template>

<script>
export default {
  name: "projectCard",
  props: {
    p:{}
  }
}
</script>