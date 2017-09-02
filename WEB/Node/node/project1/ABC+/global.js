//全局变量  filename  表示当前正在执行的文件名
console.log(__filename);
//当前脚本的目录，也是绝对路径，但是不包含文件的名字
console.log(__dirname);

//setTimeout(cb,ms)
function sayHello(){
	console.log("helloworld");
}

setTimeout(sayHello,1000);
console.error('这会在sayHello之前执行');
