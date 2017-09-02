<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/24
 * Time: 18:25
 * 数据库的连接、创建数据库
 */
header("Content-Type:text/html;charset=utf-8");
//phpinfo();
define("SERVERNAME","localhost");
define("USERNAME","root");
define("PASSWORD","root");
//连接数据库
$conn = new mysqli(SERVERNAME,USERNAME,PASSWORD);
//检测连接
if($conn->connect_error){
    die("连接失败:".$conn->connect_error);
}else{
    echo "连接成功\n";
}

//2、创建数据库
$sql = "CREATE DATABASE myPHP";
if($conn->query($sql) === TRUE){
    echo "数据库创建成功";
}else{
    echo "Error in create database:".$conn->error;
}
//断开连接
$conn->close();

?>