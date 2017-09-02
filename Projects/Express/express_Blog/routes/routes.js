const article = require('./articles');
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })


module.exports = function(app) {
    //主页
    app.get('/home', function(req, res) {
        //通过render渲染
        // res.send('hello');
        res.setHeader('Content-type', 'text/html');
        res.render('home', {
            title: 'home'
        })
    });
    //编辑文章
    app.get('/edit', article.edit);
    app.post('/add', urlencodedParser, article.add);
    app.get('/add', function(req, res) {
        res.end(".....");
    })
}