<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/1
 * Time: 19:22
 */
//使用Smarty特性
include 'Smarty.inc.php';
//$name的值为 world
$smarty->assign("name","world");
//这个helloworld.php文件的默认展示文件时helloworld.html
$smarty->display('helloworld.html');
?>