<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/18
 * Time: 19:17
 * Desc: 异常处理
 */
header("Content-Type:text/html;charset=utf-8");
//1、创建一个有异常处理的函数
function checkNum($num){
    if($num>1){
        throw new Exception("Value must be 1 or below<br>");
    }
    return true;
}
//触发异常
//checkNum(2);
//在try块里面触发异常
try{
    checkNum(2);
    echo "没有异常";
}catch(Exception $e ){
    echo "Message:".$e->getMessage();
}
/**
 * 创建一个自定义的Exception类。
 */
class customException extends Exception{
    //$this->getMessage()获取的是throw new customException("$email");中$email的值。
    public function errorMessage(){
        $errorMsg = "错误行号: ".$this->getLine()." in ".$this->getFile().":<b>"
            .$this->getMessage()."</b>不是一个合法的邮件地址";
        return $errorMsg;
    }
}
$email = "someone@qiu.com";
try{
    if(filter_var($email,FILTER_VALIDATE_EMAIL)=== FALSE){
        throw new customException("$email");
    }
    //检测qiu是否在邮箱地址中
    if(strpos($email,"qiu")!==FALSE){
        //说明邮箱地址中有qiu,
        throw new Exception("$email 是qiu的邮箱<br>");
    }
}catch(customException $e){
    echo $e->errorMessage();
}catch(Exception $e){
    echo $e->getMessage();
}
/**
 * 还有一些其余的使用方法可以查看菜鸟教程
 */
?>

