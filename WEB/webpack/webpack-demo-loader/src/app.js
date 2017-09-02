import './css/common.css';
import Layer from './components/layer/layer.js'

const App = function(){
	const NUM = 1;
	// alert(NUM);
	var dom = document.getElementById("app");
	var layer = new Layer();//Layer得到的是一个函数，这里需要通过实例化一下来执行函数
	dom.innerHTML = layer.tpl;
	console.log(layer.name);
}
new App();