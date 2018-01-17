<template>
	<section class="container">  <!-- 最外层容器-->
		<section class="menu"></section>  <!-- 左边的容器-->
		<section class="content-container"></section>   <!-- 右边的容器-->
	</section>
</template>
<script>
	export default{

	}
</script>
<style>
	.container{
		width:100%;
		background: #ccc;
	}
	.container .menu{
		width:30%;
		background: red;
		float:left;
	}
	.container .content-container{
		width:65%;
		background: blue;
		float:left;
	}
</style>