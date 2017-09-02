<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/26
 * Time: 18:51
 * Desc：管理员登录界面
 */
header("content-type:text/html;charset=utf-8");
require('../../test/db.php');

if($_POST["username"] == "admin" && $_POST["password"] == "admin"){
    $_SESSION["login"] = true;      //创建全局变量即登录状态为true
    echo "<script>alert('管理员登录成功');location.href = 'initial.php'</script>";
    exit();
}else{
    echo "<script>alert('登录失败!')</script>";
}


?>