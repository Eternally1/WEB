<template>
  <div id="app">
    <app-head></app-head>
    <keep-alive>
      <router-view class="view"></router-view>
    </keep-alive> 
    <app-foot></app-foot>
</div>
</template>

<script>
  import appHead from './components/public/head';
  import appFoot from './components/public/foot.vue';
  export default {
    name:'app',
    components:{
      'app-head':appHead,
      'app-foot':appFoot
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
    margin-top: 60px;
  }
</style>
