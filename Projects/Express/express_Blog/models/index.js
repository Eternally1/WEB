const Sequelize = require('sequelize');
const config = require('../config');

//创建一个对象实例
const sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.hostname,
    dialect: 'mysql',
    pool: {
        min: 0,
        max: 5,
        idle: 30000
    }
});

module.exports = sequelize;