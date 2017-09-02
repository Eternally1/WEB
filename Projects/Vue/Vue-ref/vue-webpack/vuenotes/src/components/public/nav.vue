<template>
	<nav class="nav">
		<div class="nav__link" v-for="item in menus">
			<router-link v-bind:to="item.path">{{item.text}}</router-link>
		</div>
	</nav>
</template>
<script>
export default{
	data(){
		return{
			menus:[
			{
				text:"精选",
				path:'/select'
			},{
				text:"话题",
				path:'/point'
			},{
				text:"作者",
				path:"/author"
			}]
		}
	}
}
</script>
<style type="text/css">
	a{
		text-decoration: none;
		color:#3c3c3c;
	}
	.nav{
		width:500px;
		height:35px;
		margin:5px auto;
		text-align:center;
		line-height:35px;
		border:1px solid red;
	}
	.nav .nav__link{
		/*让边界重叠*/
		margin-left:-1px;
		float:left;
		width:165px;
		border-left:1px solid red;
		cursor:pointer;
	}
	.nav .nav__link a{
		display: block;
		width:100%;
	}
</style>
