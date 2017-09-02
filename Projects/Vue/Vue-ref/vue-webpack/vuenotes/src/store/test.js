import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);
const store = new Vuex.Store({
	state:{
		count:10086
	},
	mutations:{
		increment(state){
			state.count++
		}
	}
})
export default store;
// //触发状态更改,而不是直接通过store.state.count赋值来更改。
// store.commit('increment');
// //获取状态对象
// console.log(store.state);