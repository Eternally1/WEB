<template>
    <div class="todolist">
        <h2>todolists</h2>
        <input type="text" placeholder="接下来要做的事" v-model="todo" v-on:keyup.enter="addNew" />
        <button v-on:click="addNew">Add</button>

        <div class="lists">
            <ul>
                <li v-for="item in lists" :class="{finish:item.isFinished}">
                    <input type="checkbox" v-bind:checked="item.isFinished" @click="toggleFinish(item)" /> {{item.msg}}
                </li>
            </ul>
        </div>
    </div>

</template>

<script>
export default{
    data (){
        return{
            todo:"",
            lists:[]
        }
    },
    created:function(){
        this.$nextTick(function(){
            this.getListData();
        })
    },
    methods:{
        getListData:function(){
            var _this = this;
            //从服务器获取list列表
            this.$http.jsonp("http://localhost/userInfo/todolist.php",{jsonp:"_callback"}).then(function(res){
                var result = res.data;
                //对结果进行处理，将对应的0和1改成true或者false
                result.forEach(function(list){
                    if(list.isFinished == "0"){
                        list.isFinished = false;
                    }else if(list.isFinished == "1"){
                        list.isFinished = true;
                    }
                },function(error){
                    console.log(error);
                })
                _this.lists = result;
            })
        },
        addNew:function(){
            var _this = this;
            //判断输入框是否为空，如果为空就不添加
            if(_this.todo.trim()){
                var msg = this.todo;//先将数据存储起来，然后在慢慢的异步添加到数据库中。
                var data = {
                    msg:msg,
                    isFinished:0
                }
                 _this.lists.push(
                    {
                                msg:_this.todo,
                                isFinished:false
                    });
                _this.todo = "";//这里清空，防止出现空格的情况。
                //添加到数据库中。
                /**
                 * 问题：在添加到数据库的时候，会发现比较才会在下面相应出来，此时在此期间
                 * 如果多次点击回车键，就会产生空的lists
                 */
                this.$http.post("http://localhost/userInfo/todolist.php",data,{emulateJSON:true}).then(function(res){
                    var result = res.data;
                    console.log(result);
                    if(result.status === "0"){
                        //返回状态码的是一个字符串
                        console.log(result.message);
                        // _this.lists.push(
                        //     {
                        //         msg:_this.todo,
                        //         isFinished:false
                        //     });
                    }else if(result.status === "2003"){
                        console.log(result.message);
                    }
                    //注意这个post是一个异步函数，所以这里的this.todo清空需要放在里面
                    // this.todo = "";
                },function(error){
                    console.log(error);
                })
            }
        },
        toggleFinish:function(list){
            list.isFinished = !list.isFinished;
        }
    }
}

</script>

<style>
    .todolist input[type=text] {
        width: 500px;
        height: 36px;
        border-radius: 5px;
        border: 1px solid #ccc;
        color: #000;
        font-family: "Comic Sans MS", sans-serief;
        font-size: 15px;
        transition: background 0.3s ease-in-out;
        text-indent: 20px;
    }
    
    .todolist input[type=text]:focus {
        background: #eee;
        outline: none;
        border-color: #9ecaed;
        box-shadow: 0 0 10px #9ecaed;
    }
    
    .todolist button {
        background-color: #009dff;
        border: none;
        font-family: "Comic Sans MS", sans-serief;
        height: 36px;
        width: 50px;
        text-align: center;
        border-radius: 3px;
        margin-left: 5px;
        transition: background 0.3s ease-in-out;
        cursor: pointer;
        text-transform: uppercase;
    }
    
    .todolist button:hover {
        background: #00c8ff;
    }
    
    .todolist .lists {
        width: 550px;
        margin: 0 auto;
    }
    
    .lists ul {
        padding-left: 20px;
    }
    
    .lists ul li {
        list-style: none;
        font-size: 18px;
        color: #575151;
        text-align: left;
        font-family: "Comic Sans MS", sans-serief;
    }
    
    .lists ul li input {
        display: inline-block;
        width: 18px;
        height: 18px;
        margin-right: 10px;
        vertical-align: middle;
        text-align: left;
    }
    
    .finish {
        text-decoration: line-through;
    }
    
</style>