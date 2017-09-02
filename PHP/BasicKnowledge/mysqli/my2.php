<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/24
 * Time: 18:36
 * DESC: 创建数据库表、插入单条和多条数据
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
//创建表的sql语句
//$sql = "CREATE TABLE MyGuest(
//  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
//  firstname varchar(30) NOT NULL,
//  lastname varchar(30) NOT NULL,
//  email varchar(50),
//  下面时间戳的默认值是当前时间。
//  reg_date TIMESTAMP
//)";
//if($conn->query($sql) === TRUE){
//    echo "Table MyGuest created successfully";
//}else{
//    echo "创建数据表错误:".$conn->error;
//}

/**
 * 向表中插入单条数据
 */
//$sql = "INSERT INTO MyGuest(firstname,lastname,email) VALUES('Jhon','Doe','1234567@jhon.com')";
//if($conn->query($sql) === TRUE){
//    echo "插入数据成功";
//}else{
//    echo "数据插入失败：".$conn->error;
//}
/**
 * 向表中插入多条数据.
 * 注意多条插入语句之间使用分号隔开，否则虽然不会报错，但是
 * 查看数据库的时候可能发现数据并没有插入禁进去
 */
$sql = "INSERT INTO MyGuest(firstname,lastname,email)VALUES('Tom','Jakey','2345634@Tom.com');";
$sql .= "INSERT INTO MyGuest(firstname, lastname,email)VALUES('Mary','Yal','34567@Tom.com');";
$sql .= "INSERT INTO MyGuest(firstname,lastname,email)VALUES('D.lufei','Qiu','45678@Tom.com')";

if($conn->multi_query($sql) === TRUE){
    echo "多条数据插入成功";
}else{
    echo "数据插入失败".$conn->error;
}

//断开连接
$conn->close();
