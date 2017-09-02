const express = require('express');
const app = express();

//post请求要使用body-parser
const bodyParser = require('body-parser');
//创建application/x-www-form-urlencoded编码解析
const urlencodedParser = bodyParser.urlencoded({extended:false});

app.use(express.static('public'));
app.get('/',function(req,res){
	res.sendFile(__dirname+'/'+"index.html");
})

app.get('/get_info',function(req,res){
	let result = {
		name:req.query.userName,
		psw:req.query.password
	};
	console.log(result);
	res.end(JSON.stringify(result));
})
app.post('/post_info', urlencodedParser,function(req,res){
	var result = {
		'first-name':req.body.firstName,
		'last-name':req.body.lastName
	};
	res.end(JSON.stringify(result));
})

var server = app.listen(8888,'localhost',function(){
	let host = server.address().address;
	let port = server.address().port;
	console.log(`服务已经在${host}:${port}启动`);
})
