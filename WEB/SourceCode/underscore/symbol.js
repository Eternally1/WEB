var symbol = {};
(function(exports) {
    exports.one = function() {
        const person = {
            name: "Tom",
            age: 20,
            toString: function() {
                return this.name + ":" + this.age;
            }
        };
        const sym = Symbol(person);
        console.log(sym);
    }
})(symbol)