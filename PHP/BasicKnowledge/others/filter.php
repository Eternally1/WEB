<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/18
 * Time: 20:00
 * Desc: 过滤器
 */
header("Content-Type:text/html;charset=utf-8");
//1、验证一个整数,验证年林是否在指定范围
$age = 45;
$age_option = array(
    "options"=>array(
        "min_range"=>16,
        "max_range"=>40
    )
);
if(!filter_var($age,FILTER_VALIDATE_INT,$age_option)){
    //如果成果，返回过滤的数据，否则返回FALSE
    echo "不是一个合法的年龄<br>";
}else{
    echo "是一个合法的年龄<br>";
}

//2、判断一个邮箱地址是否正确，通过在URL中输入参数传递
if(!filter_has_var(INPUT_GET,"email")){
    //如果URL中没有email变量
    echo "没有 email  参数<br>";
}else{
    //判断email的格式是否合法
    if(!filter_input(INPUT_GET,"email",FILTER_VALIDATE_EMAIL)){
        //如果不合法
        echo "邮箱地址不合法<br>";
    }else{
        echo "邮箱地址合法<br>";
    }
}
/**
 * 在FILTER_VALIDATE_URL和 FILTER_SANITIZE_URL比较，
 */


//3、判断是否有url参数，并对其进行净化
if(!filter_has_var(INPUT_GET,"url")){
    echo "没有 url 参数";
}else{
    //净化输入
    $url = filter_input(INPUT_GET,"url",FILTER_SANITIZE_URL);
    echo $url;
}

//4、过滤多个输入
//首先，定义一个过滤器
$filter = array(
    "name"=>array(
        "filter"=>FILTER_SANITIZE_STRING
    ),
    "age"=>array(
        "filter"=>FILTER_VALIDATE_INT,
        "options"=>array(
            "min_range"=>18,
            "max_range"=>40
        )
    ),
    "email"=>FILTER_VALIDATE_EMAIL
);
//将过滤结果存储在result中
$result = filter_input_array(INPUT_GET,$filter);
print_r($result);
if(!$result["age"]){
    echo "年龄不符合范围18~40";
}elseif(!$result["email"]){
    echo "邮箱地址不合法";
}else{
    echo "输入正确";
}

//5、使用filter_callback
//通过自定义函数作为一个过滤器来使用
function convertSpace($str){
    return str_replace("_",".",$str);
}
$string = "www_runoob_com";
echo filter_var($string,FILTER_CALLBACK,array("options"=>"convertSpace"));

//6、判断url中是否存在查询字符串
$myUrl = "www.runoob.com";
if(!filter_var($myUrl,FILTER_VALIDATE_URL,FILTER_FLAG_QUERY_REQUIRED)){
    echo "不包含查询字符串";
}else{
    echo "包含查询字符串";
}
?>