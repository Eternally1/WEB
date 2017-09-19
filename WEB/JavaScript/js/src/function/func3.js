/**
 * 函数的类型：函数声明和函数表达式
 * 区别：解析器在语法解析期间可以访问到函数声明，而函数表达式是赋值
 * 表达式的一部分，在整个程序赋值完成前都不能执行。
 * 
 * 关于函数表达式的命名是可选的，但是如果给予命名有利于帮助调试过程。
 */

declaration(); //可以正常输出
//函数声明
function declaration() {
    console.log("Hi,I am a function declaration");
}

// expression(); //出现错误
//函数表达式
const expression = function() {
    console.log("Hi,I am a function expression");
}

/**
 * 另一个疑惑:
 * 此时发现ready函数声明并没有崩溃，影子第二个函数是赋值变量的一部分，拥有自己的作用域，在赋值
 * 完成之后，就没有了，所以JavaScript将他们当作不同的实体
 */
function ready() {
    console.log("I am ready");
}
const newReady = function ready() {
    console.log("I am new Ready");
}
const read = function write() {
    console.log("I am read not right");
}
write();
//上面这句会报错，因为write是一个局部的作用域，赋值完成之后就没了。【S】
ready();
newReady();