/**
 * apply  call的使用
 */
const objA = {
    warmth: 0,
    useWarm: function(level) {
        this.warmth = level;
    }
};
const objB = {
    warmth: 0,
    isWarm: function() {
        return this.warmth === 100;
    }
}

//使用objB调用objA的useWarmth方法
objA.useWarm.call(objB, 100);
console.log(objB.isWarm()); //true