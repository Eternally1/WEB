var util = require('util');
function Parent(){
	this.name = "Tom",
	this.age = 20;
	this.sayHello = function(){
		console.log("hello"+this.name);
	}
}
Parent.prototype.getName = function(){
	console.log('ffffff');
}
function Child(){
	this.name = "Tim";
}
util.inherits(Child, Parent);
var p = new Parent();
var c = new Child();
console.log(p);
console.log(c);

console.log(util.inspect(p, true));
console.log(util.isArray(new Array()));
