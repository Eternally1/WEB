<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/16
 * Time: 18:54
 */
    namespace myProject;
    header("Content-Type:text/html;charset=utf-8");
    echo "8个常用的魔术常量";
    echo "<br>";
    //1、输出文件当前行号;
    echo "这是第'".__LINE__."'行"."<br >";
    //2、文件的完整路径和文件名
    echo "文件位于'".__FILE__."<br >";
    //3、文件所在的目录
    echo "文件所在的目录是".__DIR__."<br >";
    //4、函数名
    function test(){
        echo "该函数的名字是".__FUNCTION__."<br >";
    }
    //5、命名空间为
    echo "命名空间为".__NAMESPACE__."<br >";
?>