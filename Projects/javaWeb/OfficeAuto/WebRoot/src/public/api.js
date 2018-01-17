const myApi = {};
(function(api){
	let hostname = "http://localhost:8080/OfficeAuto";
	let token = null;

	function postJSON(path,params,end,next){
		let url = hostname + path;
		let body = "token="+token;
		for(let key in params){   //遍历对象
			body += '&'+key+"="+params[key];
		}
		console.log(body);
		// 创建ajax对象，发送请求
		let xhr = new XMLHttpRequest();
		xhr.open("POST",url,true);
		xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
		xhr.onreadystatechange = function(){
			if(xhr.readyState == 4){  // readyState保存的是请求的状态
				if(xhr.status == 200){
					//如果请求成功,调用success方法，同时将参数转化为josn格式
					console.log(xhr.responseText);
					success(JSON.parse(xhr.responseText));
				}else{
					//调用fail函数，同时传入错误码
					fail(xhr.status);
				}
			}
		}
		xhr.send(body);

		function success(response){
			//成功的话，也可能出现一些可知的错误，根据匹配来执行对应的回调函数
			switch(response.status){
				case "1001":
				end(null,response.data,response.user);
				break;
				case "1002":
				end(new Error("输入有误"),response.data);
				break;
				default:
					next(response);   //这个什么时候会执行？
				}
			}

			function fail(status){
				let msg;
				if (status >=400) msg = "客户端错误";
				if (status >=500) msg = "服务端错误";
				end(new Error(msg));
			}
		}
		/**
		 * 登录操作
		 */
		 api.login = function(data,cb){
		 	let path = "/user/loginCheck.action";
		 	postJSON(path,data,function(err,...data){
		 		cb(err,data)
		 	},function(){
		 		cb(new Error("未知错误"));
		 	});
		 },
		 api.signup = function(data,cb){
		 	let path = "/user/saveUser.action";
		 	postJSON(path,data,function(err,...data){
		 		cb(err,data)
		 	},function(){
		 		cb(new Error("未知错误"));
		 	})
		 },
		 api.search = function(data,cb){
		 	let path = "/user/searchUser.action";
		 	postJSON(path,data,function(err,...data){
		 		cb(err,data)
		 	},function(){
		 		cb(new Error("未知错误"));
		 	})
		 },
		 api.timer = function(data,cb){
		 	let path = "/agenda/getNewestAgenda.action";
		 	postJSON(path,data,function(err,...data){
		 		cb(err,data)
		 	},function(){
		 		cb(new Error("未知错误"));
		 	})
		 },
		 api.sentence = function(data,cb){
		 	let path = "/sentence/getSentence.action";
		 	postJSON(path,data,function(err,...data){
		 		cb(err,data)
		 	},function(){
		 		cb(new Error("未知错误"));
		 	})
		 },
		 api.worklog = {
		/**
		 * 日志：管理者点击日期之后，在右边显示自己的日志内容，同时在列表中显示今天的员工的日志信息。
		 * 普通员工点击日期之后，只在右边显示日志内容，列表隐藏起来。
		 */
		 showPersonLog:function(data,cb){
			// 根据日期显示某一天的日志
			let path = "/diary/loadDiary.action";
			postJSON(path,data,function(err,...data){   //如何处理多个参数
				cb(err,data);
			},function(res){
				cb(new Error("未知错误"));
			});
		},
		showPersonLogList:function(data,cb){
			// 根据日期显示一个月的日志
			let path = "/diary/listDiarys_Month.action";
			postJSON(path,data,function(err,...data){   //如何处理多个参数
				cb(err,data);
			},function(res){
				cb(new Error("未知错误"));
			});
		},
		showAllPerLogs:function(data,cb){
			//显示当天所有用户日志
			let path = "/diary/listDiarys_All.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"))
			})
		},
		addLog:function(data,cb){
			let path = "/diary/addDiary.action";
			postJSON(path,data,function(err,...data){
				cb(err,data)
			},function(res){
				cb(new Error("未知错误"));
			});
		},
		// 更新日志
		updateLog:function(data,cb){
			let path = "/diary/updateDiary.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			});
		}	
	},
	api.schedule = {
		addSchedule:function(data,cb){
			let path = "/agenda/addAgenda.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			});
		},
		updateSchedule:function(data,cb){
			let path = "/agenda/updateAgenda.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			})
		},
		showSchedule:function(data,cb){
			let path = "/agenda/getAgendaByIdAndTime.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			})
		},
		finishSchedule:function(data,cb){
			let path = "/agenda/finishAgenda.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			})
		},
		deleteSchedule:function(data,cb){
			let path = "/agenda/deleteAgenda.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			})
		},
		unfinishSchedule:function(data,cb){
			// 修改为未完成
			let path = "/agenda/changeAgendaState.action";
			postJSON(path,data,function(err,...data){
				cb(err,data);
			},function(){
				cb(new Error("未知错误"));
			})
		},
	};
}(myApi));