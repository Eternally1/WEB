
// const fs = require('fs');
// let data = '';

//创建可读的数据流
// const readStream = fs.createReadStream('./text.txt');
// //设置编码格式
// readStream.setEncoding('utf-8');
// //处理流事件
// let count = 0;
// //用于计算总共出发了几次data事件，这里我在text.txt文件中存入了大量数据，可以发现出发了三次data事件。
// //所以说一次读取的数据还是有额度的。
// readStream.on('data',function(chunk){
// 	count++;
// 	console.log(count);//1,这个data事件不会触发多次。
// 	data+=chunk;
// });
// readStream.on('end',function(){
// 	// console.log(data);
// 	console.log("数据读取完毕");
// })
// readStream.on('err',function(error){
// 	console.log(error.stack);
// });
// console.log("程序执行完毕");
// 
/**
 * 管道流
 */

// const fs = require('fs');

// //创建可读流
// const readStream = fs.createReadStream('input.txt');
// //创建可写流
// const writeStream = fs.createWriteStream('output.txt');
// //管道流
// readStream.pipe(writeStream);
// console.log("程序执行完毕");
// 
// 
/**
 * 链式流
 */
const fs = require('fs');
const zlib= require('zlib');

fs.createReadStream('text.txt').
	pipe(zlib.createGzip()).
	pipe(fs.createWriteStream('text.txt.gz'));
console.log("程序执行完成");
