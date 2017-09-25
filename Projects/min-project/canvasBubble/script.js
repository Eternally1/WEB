const nav = document.getElementById("nav");
const li = document.querySelectorAll("li");

/**
 * 给最上面一个添加点击事件，是最后面一个li.
 * 点击之后，展开成一个扇形
 */
let isFirstClick = true; //定义一个用来表示是第一次点击
li[li.length - 1].addEventListener("click", function() {

    /**
     * 第0张图片旋转-90度（逆时针90度）  
     * 第二张  -75度，
     * 依次到第11张，此时为75度。
     */
    for (let i = 0; i < li.length; i++) {
        //用i的值减去li.length/2就可以算出n的值。
        let n = i - li.length / 2;
        let deg = 0;
        if (isFirstClick) {
            deg = n * 15;
        } else {
            deg = 360;
        }
        li[i].style.transform = "rotate(" + deg + "deg)";
        console.log(n);
    }
    isFirstClick = !isFirstClick;
});

/**
 * 每一个li都要添加点击事件,点击封面的事件和其他的不一样，因此需要单独考虑
 */
for (let i = 0; i < li.length - 1; i++) {
    //添加一个索引，便于在下面进行操作。
    li[i].index = i;
    li[i].addEventListener("click", function() {
        let leftDeg = 0; //左边初始值的度数
        let rightDeg = 15; //右边初始值的度数
        this.style.transform = "rotate(" + 0 + "deg)";
        //左边的依次选装-15度，-30度等.
        for (let j = this.index - 1; j >= 0; j--) {
            leftDeg -= 15;
            li[j].style.transform = "rotate(" + leftDeg + "deg)";
        };
        //右边的图片旋转
        for (let k = this.index + 1; k < li.length; k++) {
            rightDeg += 15;
            li[k].style.transform = "rotate(" + rightDeg + "deg)";
        }
    })
};



/**
 * canvas气泡效果
 */
const canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight + 400;
const context = canvas.getContext('2d');
const colors = ["#69D2E7", "#A7DBD8", "#E0E4CC", "#F38630", "#FF4E58", "#F9D432"];
const circles = []; //存放创建的圆。
let timer;

//x y r vx[x轴的速度] vy c[color]
//在canvas上画圆
function draw(circle) {
    context.beginPath(); //开始的路径
    //开始画圆，注意参数
    context.arc(circle.x, circle.y, circle.r, 0, 2 * Math.PI);
    //填充颜色
    context.fillStyle = circle.c;
    context.globalCompositeOperation = "lighter"; //合成
    //填充到画布中
    context.fill();
};

//因为用到随机地，这里采用随机函数
function random(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

let on = true;
//鼠标移动事件
canvas.addEventListener("mousemove", function(event) {
    //移动一下，创建2个圆
    for (let i = 0; i < 2; i++) {
        let circle = {
            x: random(-5, 5) + event.clientX,
            y: random(-5, 5) + event.clientY + window.pageYOffset,
            r: random(20, 35),
            vx: Math.random() - 0.5, //随机出现-0.5到0.5之间
            vy: Math.random() - 0.5,
            c: colors[random(0, colors.length - 1)]
        }
        circles.push(circle); //将圆对象添加到数组中
        if (circles.length > 300) {
            circles.shift();
        }
        // console.log(circles.length);//可以看到最多为300
    }
    //让定时器只开启一次。
    if (on) {
        clearInterval(timer);
        timer = setInterval(drawBall, 30);
        on = false;
    }
    drawBall();
    //开始画圆
    function drawBall() {
        //清空画布
        context.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < circles.length; i++) {
            //需要在画的时候将球的位置，半径都修改。
            circles[i].x -= circles[i].vx * 3;
            circles[i].y -= circles[i].vy * 3;
            circles[i].r = circles[i].r * 0.97;
            //如果小球的半径小于1，就不让它画了
            circles[i].index = i; //添加索引，用于删除
            if (circles[i].r < 3) {
                circles.splice(circles[i].index, 1);
                continue;
            }
            draw(circles[i]);
            // console.log(1);
        }
        if (!circles.length) {
            clearInterval(timer);
            on = true;
        }
    };
});