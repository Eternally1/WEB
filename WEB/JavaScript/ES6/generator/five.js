/**
 * 2017-8-20
 */
//定义一个函数delay
function delay(time, callback) {
    setTimeout(function() {
        callback("sleep for " + time);
    }, time);
}
// delay(1000, function(msg) {
//     console.log(msg);
//     //在执行一次
//     delay(1200, function(msg2) {
//         console.log(msg2);
//     })
// });
/**
 * 要确保两个delay依次被调用的方法是确保第二个delay在第一个delay的回调函数里面,
 * 这样，如果调用12次甚至更多次，就会碰到回调金字塔问题
 */

/**
 * 使用generator可以让我们的代码进行等待，而无需进行回调
 */
//1、定义一个generator
run(function* myDelayMessage(resume) {
    //2、调用delay
    console.log(yield delay(1000, resume));
    console.log(yield delay(1200, resume));
});
//3、delay需要一个回调函数，来继续我们的generator

//4、创建一个run函数
function run(generatorFunction) {
    let generatorItr = generatorFunction(resume);

    function resume(callbackValue) {
        generatorItr.next(callbackValue);
    }
    generatorItr.next();
}