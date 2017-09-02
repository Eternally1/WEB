var _ = function(obj) {
    if (obj instanceof _) return obj;
    if (!(this instanceof _)) return new _(obj);
    // if (!(this instanceof _)) {
    //     var o = new _(obj);
    //     return o;
    // }

    this._wrapped = obj;
};

_(_([1, 2]));

/**
 * new的原理
 * 1、var o = {};
 * 2、o.__proto__ = _.prototype;
 * 3、_()被执行，此时构造函数里面的this代表的就是o，它的__ptoto__属性指向
 * 的是_.prototype，也就是说_.prototype在o的原型链上，this instanceof _ == true;
 */


// 当执行这句代码时，函数中的this指向window
// obj instanceof _ === false, this instanceof _ === false
// 所以执行 return new _(obj)
// 在new的时候，this指向了构造函数_的实例，所以 this instanceof _ === true
// this._wrapped = obj; 表示构造实例有一个属性_wrapped，值为obj（供后面_.mixin方法调用）

// 当obj已经是一个实例的时候，_(obj)直接返回这个实例： _(_([1,2])) == _([1,2])
// 自此，构造过程就结束了
// 这也就是所谓的 无new调用的构造函数