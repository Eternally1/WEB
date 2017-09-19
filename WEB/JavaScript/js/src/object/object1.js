/**
 * 关于对象和原型的一些方法
 * 《来源于JavaScript专家编程》
 */
//1、configurable(可配置属性)
var car = {};

/**
 * 这里将相关操作封装在方法中，用于在需要的时候执行方法就可以看到相关的
 * 结果显示 
 */
function config() {
    Object.defineProperty(car, "doors", {
        configurable: true,
        value: 5
    });
    console.log(car.doors); //5
    delete car.doors; //这里可以删除doors这个属性，因为它的configurable属性为true
    console.log(car.doors); //undefined
}

/**
 * 如果将true修改成为false，就可以保护它不被修改
 */

//2、可枚举属性enumberable
function enumber() {
    Object.defineProperty(car, "doors", {
        writable: true,
        enumerable: true,
        configurable: true,
        value: 4
    });
    Object.defineProperty(car, "wheels", {
        writable: true,
        enumerable: true,
        configurable: true,
        value: 4
    });
    Object.defineProperty(car, "user", {
        enumerable: false,
        value: "Tom"
    });
    //遍历对象car的属性
    //doors wheels
    for (var x in car) {
        console.log(x);
    }
    //["doors","wheels"];
    //返回的是可枚举属性的数组
    console.log(Object.keys(car));
    //返回指定对象car的所有属性组成的数组，包括不可枚举属性
    console.log(Object.getOwnPropertyNames(car));
}
//3、writable(可写特性)
function write() {
    Object.defineProperty(car, "user", {
        writable: true,
        configurable: false,
        value: "Tom"
    });
    car.user = "Mary";
    //configurable表示此属性不可以被删除，但是可以修改
    console.log(car.user); //Mary
}
//4、获取对象的详细配置
function descriptor() {
    Object.defineProperty(car, "doors", {
        value: 4,
        writable: true,
        configurable: false
    });
    console.log(Object.getOwnPropertyDescriptor(car, "doors"));
}

//5、返回特定对象的原型
function getPrototype() {
    var a = {};
    //true
    console.log(Object.getPrototypeOf(a) == Object.prototype &&
        a.__proto__ == Object.prototype);
}
//6、获取对象的属性
function getProps() {
    var foo = {
        name: "Tom"
    };
    var bar = Object.create(foo, {
        age: {
            enumerable: false,
            value: 20
        },
        height: {
            enumerable: true,
            value: function() {
                return "180cm"
            }
        }
    });
    //输出bar的所有属性，包括原型链上的,但是不可枚举的属性不能获取
    for (var prop in bar) {
        console.log(prop);
    }
    console.log('--------华丽的分割线------------');
    //输出自身的属性
    //这里获取到的不包括原型链上的属性["age","height"]
    console.log(Object.getOwnPropertyNames(bar));
    //判断bar是否含有name属性
    if (bar.hasOwnProperty("name")) {
        console.log('bar有name属性');
    } else {
        //下面这句输出了
        console.log("bar不包含name属性");
    }
}
//7、Object.isFrozen()，判断对象是否可以修改和扩展
function frozen() {
    var bomb = {
        wrap: "great",
        array: [1, 2, 3]
    };
    //判断是否可以扩展，如果可以，冻结它
    if (!Object.isFrozen(bomb)) {
        console.log("对象可以扩展，现在冻结，让他不能扩展");
        Object.freeze(bomb);
    }
    //尝试修改wrap属性
    bomb.wrap = "Tom";
    //可以看到属性并没有被修改成功
    console.log(bomb);
}
//8、判断一个对象是否在另一个对象的原型链上
function checkProto() {
    //以下三种情况都输出的是true
    //说明Function.prototype的原型链上有Object.prototype.
    console.log(Object.prototype.isPrototypeOf([]));
    console.log(Object.prototype.isPrototypeOf(Array.prototype));
    console.log(Object.prototype.isPrototypeOf(Function.prototype));
}

//9、判断对象是否可以扩展，一起阻止对象的扩展性
function extensible() {
    var car = {
        doors: 4
    };
    //先输出属性的默认配置,属性的默认的三个
    //configurable  writable   enumberable均为true
    console.log(Object.getOwnPropertyDescriptor(car, "doors"));
    //判断还对象是否可以扩展
    console.log("对象可扩展?" + Object.isExtensible(car));
    //让对象不可扩展
    Object.preventExtensions(car);
    //再次判断是否可以扩展
    console.log("再次判断对象是否可以扩展?" + Object.isExtensible(car));
    //尝试向对象中添加属性
    car.name = "laosilaisi";
    //并没有成功的添加进去。
    console.log(car);
}
//10、Object.seal();
function seal() {
    var person = {};
    Object.defineProperty(person, "name", {
        configurable: true,
        writable: true,
        value: "Tom"
    });
    //判断对象person是否可以扩展以及全部的属性是否都不可配置
    console.log("isSealed()?" + Object.isSealed(person));
    //将对象变成不可扩展以及属性不可配置
    Object.seal(person);
    //修改对象的属性
    person.name = "Mary";
    //输出修改之后的对象
    console.log(person);
}

//11、valueOf()返回指定对象的原始值。一般JavaScript会自动调用。
function valueOfObject() {
    function number(n) {
        this.number = n;
    }
    var c = new number(3);
    console.log(c);
    number.prototype.valueOf = function() {
        return this.number;
    };
    console.log(c + 4); //7
}