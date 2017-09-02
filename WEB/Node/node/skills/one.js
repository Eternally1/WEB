/**
 * 到处模块有两种方式
 * 1、module.exports  当一个模块只存在一个类的使用
 * 2、exports   对外导出多个对象、方法和值
 */

// 1、module.exports
function MyClass() {}
MyClass.prototype = {
    method: function() {
        return 'hello';
    }
}
const myClass = new MyClass();
module.exports = myClass;

//2、对外导出多个对象、方法和值
exports.method = function() {
    return "hello";
}
exports.method2 = function() {
    return "hello again";
}

//使用加载模块
var my = require('./myClass');
/**
 * 关于模块的加载机制可以查看这里的链接
 * http://www.infoq.com/cn/articles/nodejs-module-mechanism/
 * 判断加载的是哪个模块，可以通过require.resolve(id),返回文件的绝对
 * 路径。
 */