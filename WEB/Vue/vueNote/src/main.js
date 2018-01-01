import Vue from "vue";  //引入vue模块
import App from "./App.vue";

// 这里的App应该就是  {name:"app"}。然后是注册组件怎么理解
new Vue({
	el:"#app",
	components:{
		App
	},
	template:"<App/>",
})