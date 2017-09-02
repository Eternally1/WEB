<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/22
 * Time: 19:57
 * Desc:反射
 */
header("Content-Type:text/html;charset=utf-8");
require_once('./oo4.php');
//这里传递的参数person是引入的文件oo4.php中定义的类
$class = new ReflectionClass("person");
//通过输出可以看到该类的详细信息
echo $class;

?>