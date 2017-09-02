const db = require('../mysql/index.js');

//添加一篇文章
exports.add = function(req, res) {
    let result = {};
    // res.setHeader("Content-type", "text/plain");
    //怎么获取请求体
    //这里的打印信息应该在cmder中查看
    //通过post请求的数据在body中，get的数据在params中
    console.log(req.body);
    // console.log(typeof req.body);
    db.addArticle(req.body, function(err, info) {
        console.log(req.body);
        if (err) {
            console.log("failed------------------" + err);
            //err是一个对象，不方便返回，因此这里自己定义了一个返回的错误信息。
            result = {
                status: 2002,
                msg: "数据库操作错误"
            }
            res.send(result);
        }
        result = {
                status: 0,
                msg: "文章存储成功"
            }
            // res.setHeader("Content-Type", "application/json");
            // res.end(JSON.stringify(result));
        res.send(result);
    });
}

//编辑文章
exports.edit = function(req, res) {
    res.setHeader("Content-type", "text/html");
    res.render('article', {
        title: "写文章",
        layout: null
    })
}