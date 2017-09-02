<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/4
 * Time: 18:42
 * Desc: 留言回复
 */
//加载数据库配置文件
require('../config/config.inc.php');
//判断是否登录
if(empty($_SESSION["login"])){
    $arr  =array(
        "status"=>"3001",
        "msg"=>"没有登录不能回复"
    );
    echo json_encode($arr);
}
//回复留言内容
$reply = $_POST["reply"];
//操作留言对应的id
$info_id = $_POST["info_id"];
//获取系统时间
$reply_time = date("Y-m-d h:i:sa");
//echo $reply."  ".$info_id;

$insertSql = "INSERT INTO reply (info_id,reply,reply_time)VALUES('$info_id','$reply','$reply_time')";
if($conn->query($insertSql)){
    $arr = array(
        "status"=>true,
        "msg"=>"回复成功",
    );
    echo json_encode($arr);
}else{
    $arr = array(
        "status"=>false,
        "msg"=>"回复失败"
    );
    echo json_encode($arr);
}


?>