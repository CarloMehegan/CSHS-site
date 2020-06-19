<template>
  <div class="about">
    <h1>your profile</h1>
    <p>account info here and also ignore the stuff below</p>
    <HelloWorld Hi />
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld'

export default {
  name: 'about',
  components: {
    HelloWorld
  }
};

</script>