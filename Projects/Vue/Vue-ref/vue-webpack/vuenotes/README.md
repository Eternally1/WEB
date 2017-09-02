vueInitConf  ---- 可以参考里面的默认配置文件
[项目参考blog](http://blog.csdn.net/fungleo/article/details/53171614) 
[项目参考github](https://github.com/fengcms/vuedemo)

 - 项目初始化配置完成
 - 开始渲染列表，通过接通API
    1、新建一个/config/api.js文件
    2、在main.js中引用api.js，并且绑定到全局
        `new Vue({
        	router,
        	el:"#app",
        	render:(h)=>h(App)
        })`
    3、安装superagent，用于请求。 cnpm install superagent --save-dev
    api链接文件：
     [api-2](https://cnodejs.org/api/v1/topics)
     [api-1](https://cnodejs.org/api)
     [superagent使用文档参考](https://cnodejs.org/topic/5378720ed6e2d16149fa16bd)
    4、编写api.js文件，完成我们需要的工作。
    	{}.toString.call(obj)可以参考 [参考链接](https://www.talkingcoder.com/article/6333557442705696719)
    5、在测试文件中使用调用API接口
    6、配置子路由
    	/frame/subroute.vue  这个就是子路由文件
    	接着是新建子页面
    	在components下面新建一个user文件夹，里面新建三个文件

    	然后是配置routes.js文件
		
 

 - 添加public页面，同时将App.vue中的布局改变
 - 添加head页面
 - 添加nav页面，注意页面的渲染以及router-link链接的使用。
 - vuex的使用  store/test.js

