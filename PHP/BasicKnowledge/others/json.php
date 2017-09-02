<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/18
 * Time: 21:06
 * Desc: JSON编码与解码
 */
//1、定义一个数据
$person = array(
    "name"=>"Tom",
    "age"=>23,
    "height"=>185
);
//编码成json对象格式
$perJson = json_encode($person);
echo $perJson;

//2、对json字符串进行解码
$str = "$perJson";
echo $str;
//输出对象格式
var_dump(json_decode($str));
//输出数组格式
var_dump(json_decode($str,true));
?>