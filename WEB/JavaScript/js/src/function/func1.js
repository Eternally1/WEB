/**
 * 引用传递
 * @param {any} arr 
 * @returns 
 */
function paramTransfer(arr) {
    console.log(arr instanceof Array);
    if (!isArray(arr)) {
        return false
    }
    for (let i = 0; i < arr.length; i++) {
        arr[i].name += i;
    }
}

const arrP = [{
    name: "Tom",
    age: 20
}, {
    name: "mary",
    age: 23
}];
/**
 * 比较前后两次的arrP的输出可以发现，即使方法没有返回，但是执行完方法之后
 * arrP的内容得到了变化，因此是通过引用传递的
 */
console.log(arrP);
console.log(paramTransfer(arrP));
console.log(arrP);

function isArray(arr) {
    return Object.prototype.toString.call(arr) === '[object Array]';
}