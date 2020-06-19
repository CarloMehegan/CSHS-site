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
                
            />
            <br>
            <label>Name</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="name"
                
            />
            <br>
            <label>Date of Creation</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="createDate"
                
            />
            <br>
            <label>Date of Upload</label>
            <br>
            <b-form-input
                class="w-25"
                v-model="uploadDate"
                
            />
            <br>
            <label>Info about your project</label>
            <br>
            <b-form-textarea
                class="w-25"
                v-model="info"
                rows="12"
            />
            <b-button
                v-on:click="submit"
                variant="outline-primary"
                class="w-25"
            >Submit (yes it really will)
            </b-button>
        </b-form-group>
        </center>
    </div>
</template>
<script>
import axios from "axios"
const URL = "http://localhost:5000"

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
          var post_data = [this.title, this.name, this.createDate, this.uploadDate, this.info]
          axios.post(URL + "/postmethod", {
              post_data
          })
          .then(function (response) {
              console.log(response);
          })
          .catch(function (error) {
              console.log(error);
          });
          
      }
  }
};
</script>
