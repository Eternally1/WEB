let promise = new Promise(function(resolve, rejected) {
        console.log('promise');
        // resolve();
        rejected();
    })
    //这里可以输出rejected，但是不能同时和resolve()一起，需要注释掉resolve();
    //然后就是在直行道rejected()的时候程序会自动停止然后需要一步步调试到最后输出。
    //如果使用cmder  node one.js，可以得到预期的结果。
promise.then(function() {
    console.log('resloved');
}, function() {
    console.log('rejected');
})

console.log('Hi');