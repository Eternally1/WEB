<template>
	<div class="point">
		<div class="point__question">
			<div class="mask">
				<h2>热点城市放假是否持续疯涨</h2>
				<p>610期</p>
				<div class="result">
					<p><span>正方</span><span>反方</span></p>
					<progress value="75" max="100"></progress>
					<p><span>75%</span><span>25%</span></p>
				</div>
				<a href="#">进入专题</a>
			</div>
		</div>
		<div v-for="point in points">{{point.times}}</div>
		<!-- {{points}} -->
	</div>
</template>
<script>
import pointStore from '../store/index.js';

export default{
	computed:{
		points:function(){
			// return pointStore
			return pointStore.PointStore.points
		}
	}
}

</script>
<style>
	.point{
		width:500px;
		margin:0 auto;
		/*text-align:center;*/
	}
	.mask{
		position:relative;
		background:#ebf1eb;
		height:132px;
	}
	.mask h2{
		text-align:center;
		font-size:26px;
		font-family:"Microsoft YaHei";
		margin:0px;
	}
	.mask>p{
		font-size:16px;
		margin:0px;
		text-align:center;
	}
	.result{
		width:350px;
		margin:0 auto;
	}
	.result p span:nth-child(1){
		float:left;
	}
	.result p span:nth-child(2){
		float:right;
	}
	.result progress{
		width:100%;
		clear:both;
	}
	.result p{
		margin:0px;
	}
	.result p:nth-child(2) span:nth-child(1){
		float:left;
	}
	.result p:nth-child(2) span:nth-child(2){
		float:right;
	}
	.mask a{
		/*clear起作用的场合前提是display:block*/
		display:block;
		clear:both;
		position:absolute;
		right:5px;
		bottom:5px;
		text-decoration: #adbcda;
		cursor:pointer;
	}
</style>