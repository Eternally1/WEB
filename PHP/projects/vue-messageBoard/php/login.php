<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/3
 * Time: 20:56
 */
session_start();
if($_POST["name"] == "admin" && $_POST["password"]=="admin"){
    $_SESSION["login"] = true;   //设置登录成功标识
    $arr = array(
        "status"=>true,
        "msg"=>"登录成功"
    );
    echo json_encode($arr);
}else{
    $arr = array(
        "status"=>false,
        "msg"=>"登录失败"
    );
    echo json_encode($arr);
}

?>