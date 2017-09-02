<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/19
 * Time: 20:25
 */
//存储数据时调用
$res = addslashes(trim("great 'boy'"));
echo $res;
echo "<br>";
//显示数据时，调用stripslashes
echo stripslashes($res);

?>