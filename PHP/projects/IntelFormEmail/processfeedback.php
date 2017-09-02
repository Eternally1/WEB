<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/19
 * Time: 19:10
 */
header("Content-Type:text/html;charset=utf-8");
//1、定义变量，并且赋值为从服务器接收的
$name = trim($_POST["name"]);
$address = trim($_POST["address"]);
$feedback = trim($_POST["feedback"]);

//2、设置邮件的收件人、邮件主题、邮件内容、邮件头(其实就是发件人）
$toaddress = "1425906472@qq.com";
$subject = "Feedback from web site";
$mailcontent = "Customer name:".$name."\n".
                "Customer address:".$address."\n".
                "Customer feedback:".$feedback."\n";
$fromaddress = "From:webserver@example.com";

/**
 * 检查邮箱的合法性
 */
if(!preg_match('/^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/',$address)){
    echo "That is not a valid address";
    exit;
}

/**
 * 通过feedback中的信息决定收件人
 * 这里是在后面加上i，是忽略大小写的意思
 */
if(preg_match('/shop|customer service|retail/i',$feedback)){
    $toaddress = "retail@example.com";
}elseif(preg_match('/bill|account/',$feedback)){
    $toaddress = "accounts@example.com";
}
echo $toaddress."------address";


//发送邮件
//mail($toaddress,$subject,$mailcontent,$fromaddress);

//返回给浏览器显示

?>