var myApi = {};
(function() {
    /**
     * 查找元素在数组中的索引，然后根据索引删除元素
     * 对于对象数组同样适用
     * arr:数组
     * ele:要删除的数组中的某个元素
     */
    myApi.delEleByIndex = function(arr, ele) {
        var index = arr.indexOf(ele);
        console.log(index);
        //从index开始，删除一个元素。
        arr.splice(index, 1);
    }
    myApi.delEle = function(arr, obj) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] == obj) {
                arr.splice(i, 1);
            }
        }
        return arr;
    }

    /**
     * 判断是否为数组
     */
    myApi.isArray = function(arr) {
        return Object.prototype.toString.call(arr) === '[object Array]';
    }

    /**
     * 将对象转换成数组，前提是对象的属性为0,1,2,3,4
     */
    myApi.transferObjToArray = function() {
        console.log(arguments);
        let arr = Array.prototype.slice.call(arguments);
        return arr;
    };
    //下面是测试代码
    // const obj = {
    //     "1": "Tom",
    //     "2": "mary",
    //     "3": "Jack"
    // };
    // /**
    //  * 这里必须通过参数传递进去进行转换，通过传递obj的话不能达到转换效果
    //  */
    // console.log(myApi.transferObjToArray("Tom", "Jack", "Mary"));

    /**
     * 
     */
})(myApi);