require('./world');//commonJS的规范
//需要指定css-loader
require('style-loader!css-loader!./style.css')//在js文件中引入css文件

function hello(str){
	console.log(str);
}
hello('helloworld!!!!!');