<template>
	<div class="index">
		<h1 class="logo">cnode Api Test</h1>
		<ul class="list">
			<li v-for="item in lists" v-text="item.title"></li>
		</ul>
	</div>
</template>

<script type="text/javascript">
	export default{
		data(){
			return{
				lists:[]
			}
		},
		created(){
			//组件创建完成之后调用这个方法
			//初始化的时候没有传递参数
			this.get_data();
		},
		methods:{
			get_data:function(params){
				// console.log(params);//undefined
				var _this = this;
				if(!params){
					params = {}
					// console.log("这里执行了")//这句话的确执行了
				}
				//采用全局绑定的$api来获取数据
				_this.$api.get('topics',params,function(r){
					// console.log(r);//这里可以查看返回的数据以及状态
					_this.lists = r.data;
				})
			}
		}
	}
</script>

<style type="text/css">
	ul li{
		list-style:none;
	}
	.index .list li{
		border-bottom: 1px solid #ccc;
		padding:10px 0;
	}
</style>

