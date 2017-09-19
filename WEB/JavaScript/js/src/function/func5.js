/**
 * 立即调用函数表达式
 * 优点：1、提供一个比宝防止命名冲突
 * 2、提供了优雅的块级作用域
 * 3、防止污染全局命名空间
 * 4、促进了代码的模块化
 * 语句前加分号是一种防御式编程，防止其他模块没有以分号结尾。
 */

;
(function() {
    console.log("function 1");
})();

;
! function() {
    console.log("function 2");
}(); -

function() {
    console.log("function 3");
}(); +

function() {
    console.log("function 4");
}();
~ function() {
    console.log("function 5");
}();