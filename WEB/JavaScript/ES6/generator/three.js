/**
 * 在这里y不能得到yield的值。
 * yield使用括弧括起来和不使用是不一样的，注意对比
 * @param {any} x 
 * @returns 
 */
function* gen(x) {
    var y = yield x + 2;
    // console.log(y); //undefined
    // let y = 3;
    return y;
}
var g = gen(1);
console.log(g.next());
console.log(g.next());
// let res = g.next().value;
// console.log(res);
// console.log(g.next(res));