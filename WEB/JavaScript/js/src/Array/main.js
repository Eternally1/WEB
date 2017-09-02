/**
 * 这里面将一个个的api中的调用放在方法里面在，这样可以在需要的时候执行
 * 相关代码。
 */
function delEleByIndex() {
    var p1 = {
        name: "Mary",
        age: 19
    }
    var p2 = {
        name: "Tom",
        age: 20
    }
    var p3 = {
        name: "Jack",
        age: 21
    }
    var arr = [p1, p2, p3];
    myApi.delEleByIndex(arr, p2);
    /**
     * 这种情况下才可以删除，其余的会报错。
     */
    console.log(arr);
}