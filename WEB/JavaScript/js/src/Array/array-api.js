var myApi = {};
(function() {
    /**
     * 查找元素在数组中的索引，然后根据索引删除元素
     * 对于对象数组同样适用
     * arr:数组
     * ele:要删除的数组中的某个元素
     */
    myApi.delEleByIndex = function(arr, ele) {
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
        var index = arr.indexOf(ele);
        console.log(index);
        //从index开始，删除一个元素。
        arr.splice(index, 1);
    }
})(myApi);