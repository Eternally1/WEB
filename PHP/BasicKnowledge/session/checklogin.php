<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/6
 * Time: 21:04
 * Desc: 判断用户是否登录成功
 */
session_start();
//if(!$_SESSION["login"])   //使用这种会报错，没有login这个index
/**
 * 判断一个变量是否被认为是空的。当一个变量并不存在，
 * 或者它的值等同于FALSE，那么它会被认为不存在。
 * 如果变量不存在的话，empty()并不会产生警告。
 */
if(empty($_SESSION["login"])){
    //使用empty就不会报错。
    echo "你还没有登录，不能访问当前页面";
    exit;
}else{
    echo "你已登录成功，正在打开界面";
}