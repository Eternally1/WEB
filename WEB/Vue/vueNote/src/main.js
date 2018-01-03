import Vue from "vue";  //引入vue模块
import App from "./App.vue";
import router from "./router"   //引入路由配置模块


// 这里的App应该就是  {name:"app"}。然后是注册组件怎么理解
new Vue({
	el:"#app",
	router,    //注入路由配置
	components:{
		App               //注入组件
	},
	template:"<App/>",   //配置根模板，即打开页面时显示那个组件
})