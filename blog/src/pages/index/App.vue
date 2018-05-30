<template>
  <div id="app">
    <head-top></head-top>
    <div class="body">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import headTop from "@/components/head/Head"
export default {
  name: 'App',
  components: {
      headTop
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}
.body {
  margin: auto;
  text-align: center;
  max-width: 900px;
  background: #e9e9e9;
}
</style>
