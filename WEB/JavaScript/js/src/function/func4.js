/**
 * 箭头函数
 * ES5 中只支持函数级别的作用域，对于习惯了块级作用域的开发者来说很不习惯，
 * 可以使用自由变量或者绑定函数来避免。
 */
//1、自由变量
const VindingMachine = function() {
    this.stock = ["Cookie", "Spite"];
    const that = this;
    return {
        dispense: function() {
            if (that.stock.length > 0) {
                return that.stock.pop();
            }
        }
    };
};
// const disp = VindingMachine();
// console.log(disp.dispense());

//2、绑定函数实现
const VindingMachine1 = function() {
    this.stock = ["Cookie", "Spite"];
    const dispense = function() {
        if (this.stock.length > 0) {
            return this.stock.pop()
        }
    };
    return {
        dispense: dispense.bind(this)
    };
};

// const disp = VindingMachine1();
// console.log(disp.dispense());

//3、使用箭头函数实现
const VindingMachine2 = function() {
    this.stock = ["Cookie", "Spite", "TOm"];
    return {
        dispense: () => {
            if (this.stock.length > 0) {
                return this.stock.pop();
            }
        }
    };
};
const disp = VindingMachine2();
console.log(disp.dispense());