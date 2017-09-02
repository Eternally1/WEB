const express = require('express');
const app = express();
const fs = require('fs');

const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({extended:false})

//初始化用户操作界面
app.get("/",function(req,res){
	fs.readFile(__dirname+'/index.html',"utf8",function(err,data){
		if(err){
			console.log(err.stack);
		}
		res.end(data);
	})
})


//获取用户列表信息
app.get('/listUsers',function(req,res){
	fs.readFile(__dirname+"/userInfo.json","utf8",function(err,data){
		res.end(data);
	})
})
//添加一个用户信息
app.post('/addUser',urlencodedParser,function(req,res){
	const result = {
		"name":req.body.name,
		"password":req.body.password,
		"profession":req.body.profession,
		"id":req.body.userId
	};
	console.log(result);
	//读取json文件
	fs.readFile(__dirname+'/userInfo.json',"utf8",function(err,data){
		if(err){
			console.log(err.stack);
		}
		console.log(typeof data);//测试读取到的数据data是什么类型
		let newData = JSON.parse(data);
		console.log(newData);
		newData[result["name"]] = result;
		//将json转换成字符串然后写入到userInfo中
		console.log(newData);

		fs.writeFile(__dirname+'/userInfo.json',JSON.stringify(newData),"utf8",function(err){
			if(err){
				console.log(err.stack);
			}
			res.end("success")
		})
	})
})

//显示用户详情
app.get('/:id',function(req,res){
	//这种形式不知道是怎么回事，在地址栏输入http://localhost:8888/1就可以获取用户1的信息
	//读取已经存在的用户
	fs.readFile(__dirname+'/userInfo.json','utf8',function(err,data){
		if(err){
			console.log(err.stack);
		}
		data = JSON.parse(data);
		console.log(req.params);
		let userData = data["user"+req.params.id];
		console.log(userData);
		res.end(JSON.stringify(userData));
	})
})

const server = app.listen(8888,'localhost',function(){
	let host = server.address().address;
	let port = server.address().port;
	console.log(`服务已经在http://${host}:${port}启动`)
})