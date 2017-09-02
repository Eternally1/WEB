// 基础的服务器启动
var http = require('http');
http.createServer(function(request,response){
	//设置返回的头部信息
	response.writeHead(200,{'Content-Type':'text/plain'});
	//发送响应数据
	response.end('hello world!');
}).listen(8888);
console.log('服务已经在http://localhost:8888启动')
