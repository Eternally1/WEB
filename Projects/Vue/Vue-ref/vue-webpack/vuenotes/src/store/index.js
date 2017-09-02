import Vue from "vue";
import Vuex from "vuex";

//引入modules
import PointStore from './modules/PointStore.js'
Vue.use(Vuex);

var store = new Vuex.Store({
	state:{
		count:10086
	},
	modules:{
		PointStore
	}
})
export default store;