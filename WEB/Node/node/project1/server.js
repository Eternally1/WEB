const http = require('http');
const url = require('url');
const fs = require('fs');

function start(route){
	function onRequest(req,res){
		let pathname = url.parse(req.url).pathname;
		// console.log("request for"+pathname+"received");
		console.log(`request for ${pathname} received`);
		route(pathname);

		//从文件系统中读取请求的内容
		// fs.readFile(pathname.substr(1),function(err,data){
		// 	if(err){
		// 		console.log(err);
		// 		res.writeHead(404,{"Content-Type":"text/html"})
		// 	}else{
		// 		res.writeHead(200,{"Content-Type":"text/html"});
		// 		res.write(data.toString());
		// 	}
		// 	res.end();
		// })

		res.writeHead(200,{"Content-Type":"text/plain"});
		var data = {
			status:'2002',
			msg:'文件不存在'
		}
		res.write(JSON.stringify(data));
		//客户端收到的数据就是这里的write写的数据
		// res.write("hello world");
		res.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("Server has started");
}

exports.start = start;