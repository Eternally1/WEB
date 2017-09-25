/**
 * 运动的步骤---用来参考。
 * 1、闪的效果（瞬间宽高变为0，scale，随机）
 * 2、图片从小变大同时透明度从1变到0（每一张图片必须是上一步效果走完了，才会执行这一步）
 * 也就是说，因为第一个效果是随机的，因此完成第一个任务的时间前后不一致）
 * 3、图片旋转，同时透明度从0变到1 有层次感（所有图片的前两个效果都完成之后才执行这个效果）
 * 难点，怎么判断所有的图片都将第一个和第二个效果完成？？
 */
const btn = document.getElementById("btn"),
    imgs = document.querySelectorAll("img");
btn.addEventListener("click", showEffect);
let on = true; //表示按钮btn是否可以点击

let allEnd;

function showEffect() {
    if (!on) {
        return;
    } else {
        on = false;
        let endNum = 0; //存储完成的图片的数目
        allEnd = 0; //用来判断所有动画都玩成之后才能再让用户点击，以免出现在连续点击出现预料之外的bug
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
                    montion(imgs[index], "10ms", function() {
                        //写成一个函数可以放入多行代码，运动的属性函数
                        this.style.transform = "scale(0)";
                    }, function() {
                        //2、第二个运动要在这里写，也就是在第一个动作完成之后才会执行的。
                        //注意setTimeout函数里面this的指向问题
                        montion(this, "1s", function() {
                            this.style.transform = "scale(1)";
                            this.style.opacity = "0";
                        }, function() {
                            endNum++; //只要有一张图完成前面两个效果，就将值加一
                            if (endNum == imgs.length) {
                                //3、第三个运动在这里执行
                                toBig();
                            }
                        });
                    });
                    //让时间随机的。
                }, Math.random() * 1000);
                // 上面就是第一个效果的代码
            })(i);
        };
    }
};


/**
 * 运动函数，一些运动库也很多，可以借鉴，这里是自己实现
 * 参数:(运动对象，运动时间，运动的属性函数【里面放多行代码】,运动完成后要做的事情【回调函数】)
 */
function montion(obj, time, doFn, callback) {
    obj.style.transition = time;
    doFn.apply(obj); //让this指向obj

    let called = false; //解决transitionend调用多次的bug。
    obj.addEventListener("transitionend", function() {
        if (!called) {
            callback && callback.call(obj);
            called = true;
        }
    }, false); //在冒泡的阶段触发
};

/**
 * 用来完成第三个效果
 * 坐标轴
 *  -X,平行水平面 
 *  -Y,垂直水平面
 *  -Z轴，垂直频幕
 * 层次感（用到位移translate）
 */
function toBig() {
    for (let i = 0; i < imgs.length; i++) {
        //此时在前两个动作完成之后就没有效果了。
        imgs[i].style.transition = "";
        // imgs[i].style.opacity = "1";
        //此时是从远处过来，因此是先使用负值。
        //想要一个物体有旋转，需要给一个初始值。
        imgs[i].style.transform = "rotateY(0deg) translateZ(-" + Math.random() * 300 + "px)";

        (function(i) {
            setTimeout(function() {
                montion(imgs[i], "2s", function() {
                    this.style.opacity = "1";
                    this.style.transform = "rotateY(-360deg) translateZ(0px)";
                }, function() {
                    allEnd++;
                    if (allEnd == imgs.length) {
                        //说明所有的图片都完成了三个效果，此时可以再次点击  
                        on = true;
                    }
                })
            }, Math.random() * 1000)
        })(i)

    }
}