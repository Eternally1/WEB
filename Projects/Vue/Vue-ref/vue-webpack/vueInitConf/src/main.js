//引用vue;
import Vue from 'vue';
//引用路由
import VueRouter from 'vue-router';
//使用路由
Vue.use(VueRouter);

//引用入口文件
import App from './App.vue';
//引用路由配置文件
import routes from './config/routes';
//引用API文件
import api from './config/api';
//将API方法绑定到全局
Vue.prototype.$api = api;
//使用配置文件规则
const router = new VueRouter({
	routes
})

//跑起来
new Vue({
	router,
	el:"#app",
	render:(h)=>h(App)
})
