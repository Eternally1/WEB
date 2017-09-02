<template>
	<div class="select__div">
	<button v-on:click="omitCount">add</button>
		{{counts}}
		{{reversedMessage}}
	</div>
</template>

<script type="text/javascript">
	// import {mapState} from 'vuex'
	import testStore from '../store/test.js'
	// //触发状态更改
	// testStore.commit('increment');
	// testStore.commit('increment');
	// //获取状态对象
	// console.log(testStore.state.count);
	// 
	export default{
		data(){
			return{
				message:"hello world"
			}
		},
		methods:{
			omitCount(){
				//每点击一次按钮就提交一次状态更改
				testStore.commit('increment');
			}
		},
		computed:{
			reversedMessage(){
				return this.message.split("").reverse().join("");
			},
			counts(){
				return testStore.state.count;
			}
		}
		
		// //使用mapState辅助函数
		// computed: mapState({
		// 	// counts:"count"
		// })
	}

</script>