const express = require('express');
//引入handlebars模板
const exphbs = require('express-handlebars');
const path = require('path');
const helpers = require('./public/static/js/helpers');
//引入body-parser
const bodyParser = require('body-parser');
//引入数据库操作文件
// const db = require('./mysql/index.js');
//引入fs
const fs = require('fs');
//引入路由
const routes = require('./routes/routes');
const app = express();

app.use(express.static('public'));
//设置handlebars引擎
app.engine('handlebars', exphbs({
    defaultLayout: 'main',
    layoutsDir: 'views/layouts',
    partialsDir: 'views/partials',
    helpers: helpers
}));
// app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'handlebars');

//body-parser
// app.use(bodyParser.urlencoded({ extended: false }));
// app.use(bodyParser.json());
//create application/x-www-form-urlencoded parser
const urlencodedParser = bodyParser.urlencoded({ extended: false })
const jsonParser = bodyParser.json();

let port = process.env.port || 3000;

//解决跨域问题和中文乱码问题
app.all('*', function(req, res, next) {
    //允许的域名
    res.header('Access-Control-Allow-Origin', "*");
    //服务器支持的头信息
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    //服务器支持的方法
    res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By", ' 3.2.1');
    //设置返回的编码格式
    //res.header("Content-Type", "application/json;charset=utf-8");
    next();
});

routes(app);



// app.get('/home', function(req, res) {
//         //通过render渲染
//         // res.send('hello');
//         res.setHeader('Content-type', 'text/html');
//         res.render('home', {
//             title: 'home'
//         })
//     })
// app.get('/editarticle', function(req, res) {
//     res.setHeader("Content-type", "text/html");
//     res.render('article', {
//         title: "写文章",
//         layout: null
//     })
// })

//publishArticle
// app.post('/article', urlencodedParser, function(req, res) {
//     let result = {};
//     // res.setHeader("Content-type", "text/plain");
//     //怎么获取请求体
//     //这里的打印信息应该在cmder中查看
//     //通过post请求的数据在body中，get的数据在params中
//     // console.log(req.body.title);
//     // console.log(typeof req.body);
//     db.addArticle(req.body, function(err, info) {
//         if (err) {
//             console.log("failed------------------" + err);
//             //err是一个对象，不方便返回，因此这里自己定义了一个返回的错误信息。
//             result = {
//                 status: 2002,
//                 msg: "数据库操作错误"
//             }
//             res.send(result);
//         }
//         result = {
//                 status: 0,
//                 msg: "文章存储成功"
//             }
//             // res.setHeader("Content-Type", "application/json");
//             // res.end(JSON.stringify(result));
//         res.send(result);
//     });
// })

/**
 * 用作测试
 */
app.post('/test', function(req, res) {
    let data = {
        status: 0,
        msg: "操作成功"
    }
    res.setHeader("Content-type", "application/json");
    res.end(JSON.stringify(data));
})

app.listen(port);
console.log('server is running at ' + port);