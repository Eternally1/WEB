<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/24
 * Time: 19:32
 * Desc: 从数据库读取数据
 */
header("Content-Type:text/html;charset=utf-8");
//phpinfo();
define("SERVERNAME","localhost");
define("USERNAME","root");
define("PASSWORD","root");
define("DATABASE","myPHP");
//数据库连接
$conn = new mysqli(SERVERNAME,USERNAME,PASSWORD,DATABASE);
//检测连接
if($conn->connect_error){
    die("连接失败:".$conn->connect_error);
}

//$sql = "SELECT id,firstname,lastname FROM MyGuest";
//使用where子句
$sql = "SELECT id,firstname,lastname FROM MyGuest WHERE firstname = 'Liao'";

//从数据库中取出结果集并赋给给变量 $result。
$result = $conn->query($sql);
if($result->num_rows>0){
    //输出数据
    //函数 fetch_assoc() 将结合集放入到关联数组并循环输出
    while($row = $result->fetch_assoc()){
        echo "id:".$row["id"]."-Name ".$row["firstname"]." ".$row["lastname"]."\n";
    }
}else{
    echo "0  结果";
}

/**
 * 释放结果集
 */
$result->free();

$conn->close();

?>