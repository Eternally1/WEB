(function() {
    var root = typeof self == 'object' && self.self === self && self ||
        typeof global == 'object' && global.global === global && global ||
        this || {};

    //保存"_"(下划线变量)被覆盖之前的值
    var previousUnderscore = root._;

    var ArrayProto = Array.prototype,
        ObjectProto = Object.prototype;
    var SymbolProto = typeof Symbol !== 'undefined' ? Symbol.prototype : null;

    //将内置对象中的常用方法赋值为引用变量，以便更加方便的引用
    var push = ArrayProto.push,
        slice = ArrayProto.slice,
        toString = ArrayProto.toString,
        hasOwnProperty = ArrayProto.hasOwnProperty;

    //我们希望使用的所有ECMAScript 5原生函数实现在此声明。
    var nativeIsArray = Array.isArray,
        nativeKeys = Object.keys,
        nativeCreate = Object.create;

    //用于替代原型交换的裸函数参考。
    var Ctor = function() {};

    //创建一个安全引用的下划线对象以供下面使用。
    var _ = function(obj) {
        //如果obj在"_"的原型链上(即_的原型所指向的对象是否和在obj对象的原型链上)，如果是，则返回obj
        if (obj instanceof _) return obj;
        //如果不是，就创建一个新的对象，这个新对象的__proto__属性指向_.prototype,因此也就是说
        if (!(this instanceof _)) return new _(obj);
        //将underscore对象存放在_wrapped属性中。
        this._wrapped = obj;
    }

    /**
     * 将上面定义的局部变量"_"赋值给全局对象中的"_"属性
     * 即客户端的window._ = _
     * 服务器(node)的 exports._ = _
     * 同时在服务端向后兼容老的 require() API
     * 这样暴露给全局之后，就可以在全局环境下使用`_`变量了
     * 使用nodeType确保exports和module不是HTML元素
     */
    if (typeof exports !== 'undefined' && !exports.nodeType) {
        if (typeof module !== 'undefined' && !module.nodeType && module.exports) {
            exports._ = module.exports._ = _;
        }
        exports._ = _;
    } else {
        root._ = _
    }

    //当前版本
    _.VERSION = '1.8.3';


    /**
     * underscore有大量的回调函数，因此对回调进行了特殊的处理。
     * 首先存在一个optimizeCb函数，他对正常传入的函数进行一次包装处理
     * 这样可以更好的重复使用，保证上下文，即this的正确性
     * void 0 返回undefined，即没有传入上下文的时候返回相应的函数
     */
    var optimizeCb = function(func, context, argCount) {
        if (context === void 0) return func;
        switch (argCount == null ? 3 : argCount) {
            //一个参数的时候，只需要传递当前值
            case 1:
                return function(value) {
                    return func.call(context, value);
                };
                //2、目前没有用到两个参数的时候
                //3、三个参数的时候，分别是当前值，当前索引，以及整个集合
            case 3:
                return function(value, index, collection) {
                    return func.call(context, value, index, collection);
                };
                //4、四个参数的时候分别是累计值，当前值，当前索引，以及整个集合
            case 4:
                return function(accumulator, value, index, collection) {
                    return func.call(context, accumulator, value, index, collection);
                }
        }
        //4、如果都不符合以上情况，直接使用apply调用相关函数
        return function() {
            func.apply(context, arguments);
        }
    }
})()