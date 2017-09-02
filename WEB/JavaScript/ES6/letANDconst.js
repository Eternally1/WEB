// var myApi = {};
// (function () {
   
// })(myApi)
// let b = 2;
// // console.log(global.b);
// var a = 1;
// console.log(1);

let[a,b,c] = [1,2,3];
let[first,...tail] = [1,2,3,4];
console.log(tail);//[2,3,4]
console.log(typeof tail);//object
console.log(tail instanceof Array);//true
console.log(a);


