<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    
    <h2>{{msgfromfather}}</h2>
    <button v-on:click="onClickMe">Click</button>
    </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue2.js App'
    }
  },
  //这里需要加上引号，否则就表示变量名，是不对的。
  props:["msgfromfather"],
  methods:{
      onClickMe (){
        //这里的this可以直接获取从父级传递过来的数据。
        console.log(this.msgfromfather);
        //触发事件,同时将参数msg传递过去
        this.$emit('child-tell-me-something',this.msg);
        //dispatch已经被弃用了。
        // this.$dispatch('child-tell-me-something',this.msg);

      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
