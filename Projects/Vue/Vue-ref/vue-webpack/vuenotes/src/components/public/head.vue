<template>
	<header class="head">
		<div class="head__logo">
			<a href="#"><img src="../../assets/head/logo.png"/></a>
		</div>
		<div class="head__search">
			<i class="icon-search"></i>
		</div>
		<div class="head__aside">
			<div class="line"></div>
			<div class="line"></div>
			<div class="line"></div>
		</div>
	</header>
</template>

<style type="text/css">
	.head{
		min-width:500px;
		width:500px;
		height:30px;
		position:relative;
		margin:20px auto;
		background-color: #eee;
	}
	.head__logo{
		float:left;
	}
	.head__logo img{
		height:30px;
	}
	@font-face{
		font-family: "imooc-icon";
		src: url("../../assets/fonts/icomoon.eot");
		src: url("../../assets/fonts/icomoon.eot?#iefix") format("embedded-opentype")
		,url("../../assets/fonts/icomoon.woff") format("woff")
		,url("../../assets/fonts/icomoon.ttf") format("truetype")
		,url("../../assets/fonts/icomoon.svg") format("svg");
		font-weight: normal;
		font-style: normal;
	}
	.head__search .icon-search{
		font-family: 'imooc-icon';
		float:left;
		font-size:28px;
		line-height: 30px;
		height: 30px;
		margin-left:270px;
	}
	.head__search .icon-search:before{
		content:'\e986';
	}
	.head__aside{
		position:absolute;
		right:0px;
		top:0px;
		height:30px;
		width:30px;
		display: flex;
		flex-direction:column;
		justify-content: center;
		align-items:center;
		text-align:center;
		background: #d0c2c2;
	}
	.head__aside .line{
		height:2px;
		width:20px;
		background: red;
		border:2px solid #d0c2c2;
	}
	/*搜索按钮*/
	
	/*.icon-search{
		font-family:"imooc-icon";
		font-size:28px;
		color:##3255ad;
	}
	.icon-search:before{
		content:'\e986';
	}*/
</style>