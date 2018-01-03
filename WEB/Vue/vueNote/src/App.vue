<template>
	<div id="app">
		<router-view></router-view>
	</div>
</template>
<script>
export default {
	name: "app"    //这里为什么这样写还不是理解
}
</script>

<style>
#app{
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}
</style>