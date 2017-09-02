/**
 * 
 */

const one = {};

(function(exports) {
    /**
     * underscore.js对象封装的实现
     */
    one.objectPackage = function() {
        //定义一个原生的对象
        const person = {
            name: "Tom",
            age: 20
        };
        //通过_()方法将对象封装为一个Underscore对象
        const underscorePerson = _(person);
        //通过value()方法获取原生数据
        const rowPerson = underscorePerson.value();
        //将原生数据输出
        console.log(rowPerson);
    };

    /**
     * 使用noConflict()方法改变命名空间
     */
    one.changeNamespaces = function() {
        //将Underscore对象重命名为us
        const us = _.noConflict();
        console.log(us);
        const person = {
            name: "Tom",
            age: 20
        };
        console.log(us(person).value());
    };

    /**
     * map和each，用于迭代集合（数据或者对象）
     * arrObj：数组或者对象
     * map()方法和each()方法的作用，参数相同，但是map会将每次迭代函数
     * 返回的结果放入到一个新的数组中返回。
     */
    one.map = function(arrObj) {
        //当为数组的时候，value相当于值，key相当于索引
        _(arrObj).map(function(value, key) {
            console.log("key=" + key + "  value=" + value);
        });
    };
    /**
     * reduce()方法，将list元素归结为一个单一个数值
     * arrObj是传入进来的数组或者对象。对对象也适用，只要对象的值是数值类型。
     */
    one.reduce = function(arrObj) {
        let sum = _.reduce(arrObj, function(a, b) {
            return a + b;
        }, 5)
        console.log(sum);
    }



    /**
     * debounce()和throttle()两个方法用于函数节流
     */

})(one)