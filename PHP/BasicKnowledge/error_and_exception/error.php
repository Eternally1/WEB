<?php
/**
 * 错误处理
 */
header("Content-Type:text/html;charset=utf-8");
//1、基本的错误处理die()
if(!file_exists('../readme.txt')){
    //如果文件不存在,提示错误信息并且终止脚本的运行。
    die("文件不存在");
}else{
    fopen("../readme.txt",'r');
}

//2、自定义错误处理函数
function customError($errno,$errstr){
    echo "<b>Error:</b>[$errno]  $errstr<br>";
    echo "脚本结束";
    die();
}
//设置错误处理函数
//set_error_handler("customError");
////触发错误
//echo ($test);
//另一种触发方式
/**
 * 这里设置的触发方式中，可以设置针对的错误类型
 * 下面的$test抛出的是E_USER_WARNING错误，可以被自定义错误
 * 处理函数处理，但是如果设置触发方式中的错误类型和抛出的错误类型不一致，则不会
 * 调用自定义的错误处理函数。
 */
set_error_handler("customError",E_USER_WARNING);
$test = 2;
if($test>1){
    trigger_error("变量值必须小于1",E_USER_WARNING);
}

/**
 * 错误记录相关
 */
?>