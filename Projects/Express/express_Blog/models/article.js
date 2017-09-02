const sequelize = require('./index');
const Sequelize = require('sequelize');

//定义模型Article
const Article = sequelize.define('article', {
    id: {
        type: Sequelize.STRING(50),
        primaryKey: true
    },
    title: Sequelize.STRING(50),
    tags: Sequelize.STRING(50),
    abstract: Sequelize.STRING(300),
    rowtext: Sequelize.STRING(10000),
    markedtext: Sequelize.STRING(10000),
    year: Sequelize.STRING(4),
    date: Sequelize.DATEONLY,
    time: Sequelize.DATE
}, {
    timestamps: false
});

module.exports = Article;

// let now = new Date()
// console.log(now.getFullYear());

// 这里手动添加一条测试数据到articles表中
// Article.create({
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