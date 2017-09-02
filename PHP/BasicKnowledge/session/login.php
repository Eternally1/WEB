<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/6
 * Time: 20:59
 * Desc：用于用户登录界面的session
 */
header("Content-Type:text/html;charset=utf-8");
if($_POST["username"] == "admin" && $_POST["password"] == "admin"){
    session_start();//如果php的设置中没有设置自动启动session的时候
    $_SESSION["login"] = true;      //创建全局变量即登录状态为true
    $_SESSION["user"] = $_POST["username"];
    echo "登录成功";
}else{
    echo "用户的用户名或者密码错误";
}
