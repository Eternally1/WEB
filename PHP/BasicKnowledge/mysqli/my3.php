<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/24
 * Time: 19:04
 * Desc：插入数据的另一种方式
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
}else{
    //连接成功的时候
    echo "连接成功";
    $sql = "INSERT INTO MyGuest (firstname,lastname,email) VALUES(?,?,?)";
    //为mysqli_stmt_prepare()初始化statement对象
    $stmt = mysqli_stmt_init($conn);
    //预处理语句
    if(mysqli_stmt_prepare($stmt,$sql)){
        //绑定参数
        //sss表示后面传递的三个从哪壶都是字符串类型。
        mysqli_stmt_bind_param($stmt,"sss",$firstname,$lastname,$email);
        //设置参数并执行
        $firstname = "Qiu";
        $lastname = "Junan";
        $email = "1243214@qiu.com";
        mysqli_stmt_execute($stmt);

        $firstname = "Dong";
        $lastname = "Yuanjie";
        $email = "2341324839@dong.com";
        mysqli_stmt_execute($stmt);
    }
}