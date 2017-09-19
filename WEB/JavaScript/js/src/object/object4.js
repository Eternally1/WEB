/**
 * 原型对象
 */

const Car = function(name) {
    this.name = name || "Tom";
}
Car.prototype.age = 10;
Car.prototype.incAge = function(inc) {
    this.age += inc;
    return this.age;
}
const car = new Car("mary");
console.log(car.incAge(10));
//这里可以发现car打印出了一个新的属性age
/**
 * 任何试图修改原型对象属性的行为都会在对象实例上产生一个 
 * 新的属性，从而避免访问到原型链中的属性。
 */
console.log(car);
Car.prototype.age = 40;
console.log(car.incAge(10));
//上面这一句返回的不是50，而是30，因为car已经包含了自己的age属性