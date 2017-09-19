/**
 * 原型编程--封装
 */
//对于java中使用private来完成一个属性对外不可以，
//在JavaScript中可以通过构造函数的方式，里面定义的变量是
//局部的，从而外部不可以直接访问，而需要通过一些方法
const Car = function() {
    let name = "Tom";
    let age = 20;
    this.getName = function() {
        // return this.name; //这里不能添加this，在调用时，this指向的是car对象。而car没有这个name属性
        return name;
    }
    this.getAge = function() {
        return age;
    }
    this.setName = function(newName) {
        name = newname;
    }
    this.setAge = function(newAge) {
        age = newAge;
    }
}
const car = new Car();
console.log(car.name); //undefined
console.log(car.getName()); //Tom
console.log(car);