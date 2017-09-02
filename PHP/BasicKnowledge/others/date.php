<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/17
 * Time: 20:02
 */
header("Content-Type:text/html;charset=utf-8");
echo "输出当前时间：<br>";
/**
 * 大写的Y输出完整年份2017，
 * 小写的y输出17，不是完整的。
 */
echo "<hr><br>";
echo date("Y-m-d");
echo "<br>";
echo date("Y/m/d");
echo "<br>";
echo date("y.m.d");
echo "<br>";
echo date("y=m=d");
echo "<br>";


?>