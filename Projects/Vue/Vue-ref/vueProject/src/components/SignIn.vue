<template>
    <div class="signIn">
        <h2>Login</h2>
        <div>
            <input type="text" required placeholder="用户名" v-model="userName" />
            <input type="password" required placeholder="密码" v-model="userPsw" />
            <label id="promptInfo" v-bind:class="{show:isHidden}" v-text="info">用户名或者密码错误</label>
            <button id="signIn" v-on:click="submit">signIn</button>
            <router-link to="/infor">Infor</router-link>
        </div>
    </div>
</template>
<script>
    import VueResource from "vue-resource";
    import Vue from 'vue';
    //使用vue-resource
    Vue.use(VueResource);
    export default{
        data (){
            return{
                userName:"",
                userPsw:"",
                isHidden:true,
                info:""
            }
        },
        mounted:function(){
            this.$nextTick(function(){
            //    this.getUserInfo()
            })
        },
        methods:{
            submit:function(){
                var _this = this;
                if(_this.userName.trim() && _this.userName.trim()){
                    // console.log(this.userName+","+this.userPsw);
                    var data = {
                        userName:_this.userName,
                        userPsw:_this.userPsw
                    }
                    _this.$http.post('http://localhost/userInfo/userInfo.php',data,{emulateJSON: true}).then(function(res){
                        var result = res.data;
                        if(result.status == "0"){
                            //如果登陆成功就让登陆界面的输入框清空
                            _this.userName = "";
                            _this.userPsw = "";
                            console.log("登陆成功");
                            //这样就可以成功的跳转到 /infor界面
                            _this.$router.push({path:'/infor'});
                        
                        }else if(result.status == "2002"){
                            _this.info = "用户名或密码错误";
                            _this.isHidden = false;
                            // console.log("用户名或者密码错误");
                        }
                    },function(error){
                        console.log(error);
                    });
                }else{
                    _this.info="请输入用户名和密码";
                    _this.isHidden = false;
                }
            },
            //这里是测试获取本地的json文件。
            // getUserInfo (){
            //     this.$http.get('/api/result').then(function(res){
            //         console.log(res.data.data);
            //     });
            // }
        }
    }
</script>
<style>
    * {
        padding: 0;
        margin: 0;
    }
    
    .signIn {
        font-size: 100%;
        font-family: "Comic Sans MS", cursive, sans-serif;
        width: 300px;
        height: 300px;
        position: absolute;
        top: 50%;
        left: 50%;
        margin: -150px 0 0 -150px;
    }
    
    .signIn h2 {
        font-size: 2em;
        text-shadow: 0 0 20px #ccc;
        color: #000;
        letter-spacing: 1px;
        text-align: center;
        margin-bottom: 1.5em;
    }
    
    .signIn input {
        width: 278px;
        height: 18px;
        margin-bottom: 10px;
        outline: none;
        padding: 10px;
        font-size: 16px;
        color: #fff;
        /*text-shadow:0px 0px 2px #000;*/
        border-top: 1px solid #312E3D;
        border-left: 1px solid #312E3D;
        border-right: 1px solid #312E3D;
        border-bottom: 1px solid #56536A;
        background-color: #2D2D3F;
        border-radius: 5px;
    }
    
    .signIn button {
        display: block;
        width: 300px;
        line-height: 30px;
        background-color: #4a77d4;
        border: 1px solid #3762bc;
        color: #fff;
        /*margin:1em auto;*/
        text-align: center;
        font-size: 1em;
        border-radius: 5px;
        font-family: "Comic Sans MS", cursive, sans-serif;
        padding: 5px;
        outline: none;
        cursor: pointer;
    }
    
    .signIn label {
        display: inline-block;
        width: 100%;
        color: red;
        text-align: right;
        font-size: 13px;
    }
    
    .show {
        visibility: hidden;
    }
</style>