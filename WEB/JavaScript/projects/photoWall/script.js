const btn = document.getElementById("btn"),
    imgs = document.querySelectorAll("img");
btn.addEventListener("click", showEffect);
let on = true;
let allEnd;

function showEffect() {
    if (!on) {
        return;
    } else {
        on = false;
        let endNum = 0;
        allEnd = 0;
        for (let i = 0; i < imgs.length; i++) {
            (function(index) {
                setTimeout(function() {
                    montion(imgs[index], "10ms", function() {
                        this.style.transform = "scale(0)";
                    }, function() {
                        montion(this, "1s", function() {
                            this.style.transform = "scale(1)";
                            this.style.opacity = "0";
                        }, function() {
                            endNum++;
                            if (endNum == imgs.length) {
                                toBig();
                            }
                        });
                    });
                }, Math.random() * 1000);
            })(i);
        };
    }
};



function montion(obj, time, doFn, callback) {
    obj.style.transition = time;
    doFn.apply(obj);
    let called = false;
    obj.addEventListener("transitionend", function() {
        if (!called) {
            callback && callback.call(obj);
            called = true;
        }
    }, false);
};


function toBig() {
    for (let i = 0; i < imgs.length; i++) {
        imgs[i].style.transition = "";
        imgs[i].style.transform = "rotateY(0deg) translateZ(-" + Math.random() * 300 + "px)";
        (function(i) {
            setTimeout(function() {
                montion(imgs[i], "1s", function() {
                    this.style.opacity = "1";
                    this.style.transform = "rotateY(-360deg) translateZ(0px)";
                }, function() {
                    allEnd++;
                    if (allEnd == imgs.length) {
                        on = true;
                    }
                })
            }, Math.random() * 1000)
        })(i)

    }
}