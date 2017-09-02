var fs = require('fs');
//同步读取文件
// var data  = fs.readFileSync('./text.txt');
// 异步读取文件
// 回调函数接受错误对象作为第一个参数
// 如果此时的读取文件的路径不正确就会出现错误并且停止执行
var data  = fs.readFile('./text.txt',function(err,data){
	if(err){
		console.log(err.stack);
		return;
	}
	console.log(data.toString())
});
// console.log("读取到的数据是："+data);
console.log("程序执行结束")