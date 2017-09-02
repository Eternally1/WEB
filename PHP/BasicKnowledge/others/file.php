<?php
/**
 * 关于文件的一些相关操作
 */
header("Content-Type:text/html;charset=utf-8");
//如果fopen()方法无法打开文件，则返回0.
$file1 = fopen('../readme.txt','r') or exit("文件打开失败");

//读取文件,逐行读取文件
while(!feof($file1)){
    /**
     *  从文件中逐行读取文件。
     * 注意事项：读取php文件的话，是不能得到想要的结果，不是很清楚原因。
     */
    echo fgets($file1)."<br>";
}

//关闭文件
fclose($file1);
?>