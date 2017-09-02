new Vue({
    el: ".container",
    data: {
        addressList: [],
        limitNum:3,    //默认的长度为3
        currentIndex:0,
        shippingMethod:1
    },
    mounted: function () {
        this.$nextTick(function () {
            this.getAddressList();
        });
    },
    methods: {
        getAddressList: function () {
            var _this = this;
            this.$http.get("data/address.json").then(function (res) {
                var result = res.data;
                console.log(result.result);
                if (result.status == "0") {
                    _this.addressList = result.result;
                }
            })
        },
        //loadMore加载更多，但是再次点击的时候不能收起。
        loadMore:function(){
            this.limitNum = this.addressList.length;
        },
        setDefault:function(addressId){
            this.addressList.forEach(function(item,index){
                if(item.addressId == addressId){
                    item.isDefault = true;
                }else{
                    item.isDefault = false;
                }
            })
        }
    },
    computed:{
        filterAddress:function(){
            return this.addressList.slice(0,this.limitNum);//会截取数据的前面3条。
        }
    }
})