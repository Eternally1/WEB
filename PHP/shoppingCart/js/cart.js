var vm = new Vue({
    //新建一个vue实例
    el: "#app",
    data: {
        // title:"hello vue"
        productList: [],
        totalMoney: 0,
        checkAllFlag: false,
        totalPrice: 0, //总的价格
        delFlag: false, //是否显示弹出框
        curProduct: "" //用于存储要删除的商品
    },
    filters: {
        //过滤器,使用过滤器添加$ 或者￥.也就是货币符号
        //过滤器分为全局和局部过滤器
        formatMoney: function (value) {
            //默认会传一个值进来,也就是用在了谁身上，传进来的就是谁的值
            return "￥" + value.toFixed(2);

        }
    },
    mounted: function () {
        //实例化创建完成之后执行的内容,这里相当于实例化
        //之后就立即执行函数cartView()。
        this.$nextTick(function () {
            //这里使用this也可以，同时记得使用$nextTick()函数。可以查看官方文档
            vm.cartView();
            // console.log("success");
        })

    },
    methods: {
        cartView: function () {
            var _this = this;
            // this.title = "Vue hello";
            //已经引入了vue-resource，这里可以直接使用
            //$http.get()方法。这里是基于promise的写法。这里可以直接接受参数
            this.$http.get("data/cartData.json").then(function (res) {
                //这里可以输出res看一下具体什么内容，其实是被vue封装了一层,
                //我们需要的数据被放在了res.data里面
                _this.productList = res.data.result.list;
                _this.totalMoney = res.data.result.totalMoney;
            });
        },
        /**
         * 在参数中通过传递第二个参数+1  -1来区分点击的是增加还是减少按钮
         */
        changeMoney: function (product, way) {
            if (way > 0) {
                product.productQuantity++;
            } else {
                if (product.productQuantity > 1) {
                    product.productQuantity--;
                } else {
                    //商品数量最少为1；
                    product.productQuantity = 1;
                }
            }
            this.calcTotal();
        },
        selectedProduct: function (product) {
            if (typeof product.checked == "undefined") {
                //全局注册，
                Vue.set(product, "checked", true); //向全局product中注册一个checked属性，值为true
                // console.log(product.checked);
                //局部注册
                // this.$set(product,"checked",true);
            } else {
                product.checked = !product.checked; //取反
            }
            this.calcTotal();
        },
        checkAll: function (flag) {
            //全选
            this.checkAllFlag = flag;
            var _this = this;
            this.productList.forEach(function (value, index) {
                if (typeof value.checked == "undefined") {
                    //全局注册，
                    _this.$set(value, "checked", flag); //向全局product中注册一个checked属性，值为true
                    //这里也进行注册的原因是，如果直接点击全选的话，checked没有定义，因此这里需要注册一下。
                } else {
                    value.checked = flag;
                }
            });
            this.calcTotal();
        },
        calcTotal: function () {
            var _this = this;
            this.totalPrice = 0; //每一次遍历之前先清0
            this.productList.forEach(function (value, index) {
                if (value.checked == true) {
                    _this.totalPrice += value.productQuantity * value.productPrice;
                }
            })
        },
        delConfirm: function (item) {
            this.delFlag = true;
            this.curProduct = item;
        },
        delProduct: function () {
            this.delFlag = false;
            var index = this.productList.indexOf(this.curProduct);//用于在数组中查询某个元素在数组中的位置，即使是对象数组也可以找到
            this.productList.splice(index, 1);//之后通过splice方法来删除
            //这里应该是通过调用后台接口来操作的，通过传入商品ID到后台，然后后台删除对应的数据。
        }
    }
});

//使用全局过滤器
Vue.filter("money", function (value, type) {
    return "￥" + value + type;
})