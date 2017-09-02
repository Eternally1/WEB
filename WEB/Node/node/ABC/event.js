// var events = require('events');
// //创建eventEmitter对象
// var eventEmitter = new events.EventEmitter();
// //创建事件处理程序
// function connectHandler(){
// 	console.log("连接成功");
// 	//触发事件处理程序
// 	eventEmitter.emit('data_received');
// }
// //绑定事件和时间处理程序
// // eventEmitter.on('connect',connectHandler);
// eventEmitter.addListener('connect',connectHandler);

// eventEmitter.on('data_received',function(){
// 	console.log("数据接收成功");
// })
// eventEmitter.emit('connect');
// console.log("程序执行完毕")
// 
var events = require('events');
//创建eventemitter对象
var emitter = new events.EventEmitter();
//监听器1
var listener1 = function(){
	console.log("listener1");
}
//监听器2
var listener2 = function(){
	console.log("listener2");
}
//绑定事件connection，处理函数是listener1
emitter.on('connection',listener1);
//绑定事件connection，处理函数是listener2
emitter.on('connection',listener2);
//计算事件connection上监听器的数目
let count = events.EventEmitter.listenerCount(emitter,'connection');
console.log(count+'个监听器在监听connection事件');

//处理connection事件
emitter.emit('connection');

//移除绑定的listener1监听器
emitter.removeListener('connection', listener1);

emitter.emit('connection');
//再次计算监听器个数
count = events.EventEmitter.listenerCount(emitter,'connection');
console.log(count+"个监听器监听connection事件");
//下面这句会报错，主要原因是没有设置error事件的监听器。
emitter.emit('error');