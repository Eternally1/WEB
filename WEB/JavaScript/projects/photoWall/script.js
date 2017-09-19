/**
 * 运动的步骤---用来参考。
 * 1、闪的效果（瞬间宽高变为0，scale，随机）
 * 2、图片从小变大同时透明度从1变到0（每一张图片必须是上一步效果走完了，才会执行这一步）
 * 也就是说，因为第一个效果是随机的，因此完成第一个任务的时间前后不一致）
 * 3、图片旋转，同时透明度从0变到1（所有图片的前两个效果都完成之后才执行这个效果）
 */
const btn = document.getElementById("btn"),
    imgs = document.querySelectorAll("img");
btn.addEventListener("click", showEffect);

function showEffect() {
    for (let i = 0; i < imgs.length; i++) {
        // montion(imgs[i], "1s", function() {
        //     //写成一个函数可以放入多行代码，运动的属性函数
        //     imgs[i].style.transform = "scale(0)";
        // }, function() {
        //     console.log(this);
        // })
        //使用setTimeout解决同步运动问题，改成不同步
        (function(index) {
            /**
             * 第一个效果的实现，需要注意的是如何通过立即执行函数，
             * 将参数传递进去并保持着。
             */
            setTimeout(function() {
                //但是此时的i就找不到了。因此需要将i绑定进来，需要使用闭包？？
                montion(imgs[index], "1s", function() {
                    //写成一个函数可以放入多行代码，运动的属性函数
                    imgs[index].style.transform = "scale(0)";
                }, function() {
                    console.log(this);
                });
                //让时间随机的。
            }, Math.random() * 1000);
            // 上面就是第一个效果的代码
        })(i)
    };
};

/**
 * 运动函数，一些运动库也很多，可以借鉴，这里是自己实现
 * 参数:(运动对象，运动时间，运动的属性函数【里面放多行代码】,运动完成后要做的事情【回调函数】)
 */
function montion(obj, time, doFn, callback) {
    obj.style.transition = time;
    doFn.apply(obj); //让this指向obj

    obj.addEventListener("transitionend", function() {
        callback.call(obj);
    }, false); //在冒泡的阶段触发
};