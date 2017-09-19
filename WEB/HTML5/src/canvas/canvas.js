let my_canvas = document.getElementById("myCanvas");
//创建context对象，getContext("2d")拥有多种绘制路径，圆形、矩形、字符等方法
let ctx = my_canvas.getContext("2d");
//绘制一个矩形
//fillStyle可以使css颜色，渐变，或者图案
ctx.fillStyle = "#FF0000";
ctx.fillRect(0, 0, 150, 75);