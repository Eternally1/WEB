<template>
  <div id="app">
    <h1 v-text="title"></h1>
    <input v-model="newItem" @keyup.enter="addNew" class="input">
    <ul>
      <li v-for="item in items" :class="{finished:item.isFinished}" >
          <input type="checkbox" v-on:click="toggleFinish(item)" class="checkbox">
          {{item.label}}
      </li>
    </ul>
    <p>this is a great idea {{yeah}}</p>
  <componentA msgfromfather="you die!"
  v-on:child-tell-me-something="listen"></componentA>
  </div>
</template>

<script>
/**
 * 这里调用store.js文件
 */
import Store from './store.js'
// console.log(Store);
/**
* 导入组件A
*/
import ComponentA from "./components/componentA"

//这里的export可以看作是 new Vue({})里的参数和属性
export default {
  //data (){}和下面的data:function(){}等价
  data:function(){
      return{
        title:"this is a todo list",
        items:Store.fetch(),
        newItem:"",
        yeah:"yes"
      }
  },
  methods:{
    toggleFinish:function(item){
      //反一下
      item.isFinished = !item.isFinished;
    },
    addNew:function(){
      //这里直接使用this.newItem就可以获取到data里面的newItem值
      //这里的this不可省略
        this.items.push(
          {
            label:this.newItem,
            isFinished:false
          });
          /**
           * 这里可以直接执行Store.save(this.items)进行存储之类的，但是这样
           * 需要每次在执行方法的时候调用，比较麻烦，所以这时候可以使用watch
           * 监视items，当它改变的时候，就执行对应的方法
           */
        this.newItem = "";//清空input
    },
    listen:function(message){
      //这个message就是从ComponentA中传递过来的数据
      console.log(message);
      this.yeah = message;
    }
  },
  watch:{
    //要观察的是items的变化
    items:{
      handler :function(items){
        // console.log(val, oldVal);
        Store.save(items);
      },
      //深层次复制。
      deep:true
    }
  },
  /**
    注册组件
  */  
  components:{
    ComponentA
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
.input{
    width:500px;
    height:30px;
    border-radius:5px;
    outline:none;
    border:none;
    border:1px solid #ccc;
    font-size:20px;
    text-indent:40px;
}
.input:focus{
    border:1px solid green;
}
.finished{
    text-decoration:line-through;
}
ul li{
  list-style:none;
  text-align:left;
  line-height:30px;
  height:30px;
  font-size:20px;
}
.checkbox{
  width:20px;
  height:20px;
  padding-right:20px;
}
</style>
