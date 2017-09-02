import Vue from 'vue'
import store from './vuex/store'
import App from './components/App.vue'

new Vue({
	store,//注册到所有子组件中
	el:'body',
	components:{App}
})