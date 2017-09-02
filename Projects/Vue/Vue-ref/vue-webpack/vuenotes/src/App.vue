<template>
  <div id="app">
  <app-head></app-head>
  <app-nav></app-nav>
    <router-view
      class="view"
      keep-alive
      transition
      transition-mode="out-in">
      </router-view>
      <app-foot></app-foot>
  </div>
</template>

<script>
import appHead from './components/public/head';
import appFoot from './components/public/foot';
import appNav from './components/public/nav.vue';
export default {
  components:{
    'app-head':appHead,
    'app-nav':appNav,
    'app-foot':appFoot
  }
}
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>
