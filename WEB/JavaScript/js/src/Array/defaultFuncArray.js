/**
 * 数组一些已定义方法的使用
 * slice()
 * reduce()
 * aplice()
 */



/**
 * slice()返回一个从开始到结束（不包括结束）选择数组的一部分浅拷贝
 * 到一个新的数组对象，原始数组不会被修改
 */
let arrObj = [
    "Tom",
    {
        "age": 20,
        gender: "male"
    },
    "1404",
    "red"
];
//这里的中间的对象也可以正常输出，浅拷贝是什么意思？？
// console.log(arrObj.slice(0, 3));



/**
 * reduce()方法对累加器和数组中的每个元素（从左到右）应用一个函数，以将其减少为单个值
 */
let number = [1, 2, 3, 4];
let totalVal = number.reduce(function(prevValue, nextValue, index, array) {
    return prevValue + nextValue;
});
// console.log(totalVal);



/**
 * 该splice()方法通过删除现有元素和/或添加新元素来更改数组的内容,
 * 直接影响原来的数组。返回被删除的元素
 */
//添加元素，在索引为2的地方，删除0个元素，添加“right"元素。
console.log(arrObj.splice(2, 1, "right"));
console.log(arrObj);
//删除元素,从索引为2开始删除后面所有元素，包括索引值为2的元素
arrObj.splice(2);
console.log(arrObj);


/**
 * reduceRight()方法对累加器和数组的每个值（从右到左）应用函数将其减少为单个值
 */

const arr_name = ["Tom", "mary", "Jack"];
let str = arr_name.reduceRight(function(a, b) {
    return a + "," + b;
});
console.log(str);