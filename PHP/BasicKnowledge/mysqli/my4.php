<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/24
 * Time: 19:19
 * Desc: 预处理语句的使用
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
//预处理以及绑定
$stmt = $conn->prepare("INSERT INTO MyGuest (firstname,lastname,email) VALUES (?,?,?)");
/**
 * bind_param是告诉php哪些变量应该使用问号所替换。
 */
$stmt->bind_param("sss",$firstname,$lastname,$email);

//设置参数并执行
//如下所示，这里因为在设置类型的时候设置的是sss，
//下面这里执行的时候会报错，但是并不会终止执行。
$firstname  =Liao;
$lastname = "Baozhong";
$email = "34567@qq.com";
$stmt->execute();

echo "数据插入成功";
$stmt->close();
$conn->close();


?>