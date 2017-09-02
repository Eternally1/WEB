const fs = require('fs');
const sayHello = function(){
	let data = '';
	//路径错误，这样写的路径是C盘下面的ABC文件
	// const readStream = fs.createReadStream('/ABC/input.txt');
	const readStream = fs.createReadStream('../ABC/input.txt');
	readStream.setEncoding('utf-8');
	//所以说一次读取的数据还是有额度的。
	readStream.on('data',function(chunk){
		data+=chunk;
		console.log(data);
	});
	readStream.on('end',function(){
		console.log("数据读取完毕");
	})
	readStream.on('error',function(error){
		console.log(error.stack);
	});
}
/**
 * 注意比较这两种方式的不同
 */
// exports.hello = sayHello;
module.exports = sayHello;