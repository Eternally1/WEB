<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/3
 * Time: 19:25
 */
header("content-type:text/html;charset=utf-8");
//接受传送过来的数据
$name = $_POST["name"];
$content = $_POST["content"];
//加载数据库配置文件
require('../config/config.inc.php');
//获取系统当前时间,这里的时间是毫秒数
$content_time = date("Y-m-d h:i:sa");
//echo is_string($content_time);//返回1，代表是string类型。
//echo $content_time." name ".$name." content ".$content;

$insertSql = "INSERT INTO info (name,content,content_time) VALUES( '$name','$content','$content_time')";
if($conn->query($insertSql)){
    $arr = array(
        "status"=>true,
        "msg"=>"留言成功",
        );
    echo json_encode($arr);
}else{
    $arr=array(
        "status"=>false,
        "msg"=>"留言失败",
        "error"=>$conn->error
    );
    echo json_encode($arr);
}

?>