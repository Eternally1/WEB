/**
 * 数据库的操作
 */
//创建一条article文章记录
const Article = require('../models/article');

const db = {};
(function(exports) {
    exports.addArticle = function(data, cb) {
        console.log(data);
        let now = new Date();
        Article.create({
            id: "article-" + Date.now(),
            title: data.title,
            tags: data.tags,
            abstract: data.abstract,
            rowtext: data.rowtext,
            markedtext: data.markedtext,
            year: now.getFullYear(),
            date: now,
            time: now
        }).then(function(info) {
            // console.log("created:" + info);
            cb(null, info);
        }).catch(function(err) {
            // console.log("failed:" + err);
            cb(err);
        })
    }
})(db)

module.exports = db;

// / Article.create({
//     //目前不增加id属性会报错
//     id: "article" + Date.now(),
//     title: "First test",
//     tags: "vue.js,mongoose,javascript",
//     abstract: "wanna success",
//     rowtext: "i am using __markdown__",
//     markedtext: "i am using <strong>markdown</strong>",
//     year: now.getFullYear(),
//     date: now,
//     time: now
// }).then(function(info) {
//     console.log("created:" + info);
// }).catch(function(err) {
//     console.log("failed:" + err);
// })