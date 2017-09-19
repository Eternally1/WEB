/**
 * 参数对象,当不确定参数个数时使用
 */
function sum() {
    let len = arguments.length;
    let total = 0;
    for (let i = 0; i < len; i++) {
        total += arguments[i];
    }
    return total;
}
/**
 * 这里是测试sum的代码，注意传入的参数是单个参数，不是数组。
 */
// console.log(sum(1, 2, 3));

/**
 * 默认参数
 */
function join(name = "Tom", age = 18) {
    return name + " " + age;
}
// console.log(join());
// console.log(join("mary", 20));

/**
 * 剩余参数的概念 ES6
 * 1、使用参数对象实现
 */
const dispatcher = {
    join: function(before, after) {
        //传递进来的参数是一个数组，而使用了apply，因此表示的是当成两个参数来进行传递的。
        return before + "," + after;
    },
    sum: function() {
        /**
         * arguments是一个对象，索引是0,1,2,3...
         * 通过使用Array.prototype.slice()方法将它转换成一个数组。
         */
        // console.log(arguments);
        // console.log("--------");
        let args = Array.prototype.slice.call(arguments);
        // console.log(args);
        return args.reduce(function(prev, next, index, array) {
            return prev + next;
        })
    }
};
const proxy = {
    relay: function(method) {
        console.log(arguments);
        //注意这里的arguments是一个类数组对象，但是仍然可以使用splice方法。
        let args = Array.prototype.splice.call(arguments, 1);
        //这里使用apply是将参数放在数组中进行传递，接收之后依次展开对应
        return dispatcher[method].apply(dispatcher, args);
    }
};
//此时的args是一个数组，包含后面两个元素。
console.log(proxy.relay("join", 'foo', "bar"));
// console.log(proxy.relay("sum", 1, 2, 3, 4, 5, 6, 6));


/**
 * rest剩余参数的概念
 */
const dispatcher1 = {
    join: function(before, after) {
        return before + "," + after;
    },
    sum: function(...rest) {
        return rest.reduce(function(prev, next, index, array) {
            return prev + next;
        })
    }
};
const proxy1 = {
    relay: function(method, ...goodies) {
        console.log(goodies);
        return dispatcher1[method].apply(dispatcher1, goodies);
    }
}
console.log(proxy1.relay("sum", 1, 2, 3, 4, 5));