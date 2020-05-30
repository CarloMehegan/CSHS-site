<template>
    <div>
        <center>
        <b-form-group
            label="Create A Post"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="pl-3"
        >
            <label>Title</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="title"
                @focus="clearStatus"
                @keypress="clearStatus"
            />
            <br>
            <label>Name</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="name"
                @focus="clearStatus"
                @keypress="clearStatus"
            />
            <br>
            <label>Date of Creation</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="createDate"
                @focus="clearStatus"
                @keypress="clearStatus"
            />
            <br>
            <label>Date of Upload</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="uploadDate"
                @focus="clearStatus"
                @keypress="clearStatus"
            />
            <br>
            <label>Info about your project</label>
            <br>
            <b-form-textarea
                class="w-25"
                v-model="info"
                rows="12"
                @focus="clearStatus"
                @keypress="clearStatus"
            />
            <b-button
                v-on:click="submit"
                variant="outline-primary"
                class="w-25"
            >Submit
            </b-button>
        </b-form-group>
        </center>
    </div>
</template>
<script>
export default {
  name: "create",
  components:{
  },
  data() {
    return {
        title: '',
        name: '',
        createDate: '',
        uploadDate: '',
        info: '',
    }
  },
  methods: {
      submit: function(){
          //this is where the upload/creating new post goes
          console.log(this.title, this.name, this.createDate, this.uploadDate, this.info)
      }
  }
}
</script>
