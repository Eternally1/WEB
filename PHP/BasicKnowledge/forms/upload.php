<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/17
 * Time: 20:54
 * Desc:文件上传
 */
header("Content-Type:text/html;charset=utf-8");
//require('upload.html');
//if($_FILES["file"]["error"]>0){
//    //文件上传出错
//    echo "错误".$_FILES["file"]["error"]."<br>";
//}else{
//    echo "上传的文件名:".$_FILES["file"]["name"]."<br>";
//    echo "文件类型:".$_FILES["file"]["type"]."<br>";
//    echo "文件大小:".($_FILES["file"]["size"]/1024)."KB<br>";
//    echo "文件临时存储位置:".$_FILES["file"]["tmp_name"]."<br>";
//}

/**
 * 上传限制  图片格式如下，大小小于200KB
 */
//1、允许上传的图片后缀格式
$allowedExts = array('gif','jpeg','png','jpg');
//2、将文件名以"."来分隔开，形成数组
$temp = explode(".",$_FILES["file"]["name"]);
//print_r($temp);
//3、获取数组的最后面的一个值，也就是获取文件的后缀名
$extension = end($temp);
//4、判断文件类型
if(($_FILES["file"]["type"] == "image/gif")
    ||($_FILES["file"]["type"] == "image/jpeg")
    ||($_FILES["file"]["type"] == "image/jpg")
    ||($_FILES["file"]["type"] == "image/pjpeg")
    ||($_FILES["file"]["type"] == "image/x-png")
    ||($_FILES["file"]["type"] == "image/png")
    //文件大小小于200KB
    &&($_FILES["file"]["size"] < 200*1024)
    //搜索后缀名数组中是否包含对应的后缀名
    && (in_array($extension,$allowedExts))){
        if($_FILES["file"]["error"]>0){
        //文件上传出错
        echo "错误".$_FILES["file"]["error"]."<br>";
    }else{
        echo "上传的文件名:".$_FILES["file"]["name"]."<br>";
        echo "文件类型:".$_FILES["file"]["type"]."<br>";
        echo "文件大小:".($_FILES["file"]["size"]/1024)."KB<br>";
        echo "文件临时存储位置:".$_FILES["file"]["tmp_name"]."<br>";
        /**
         * 将文件保存在upload中
         * 判断upload中是否已经存在此文件
         */
        if(file_exists("upload/".$_FILES["file"]["name"])){
            echo $_FILES["file"]["name"]."文件已经存在";
        }else{
            //当遇到中文文件名的时候，对文件名进行强制转码iconv("UTF-8", "gbk",$name)，将UTF8转换成gbk，这样就不会出现乱码了
            move_uploaded_file($_FILES["file"]["tmp_name"],
                "upload/".iconv("UTF-8","gbk",$_FILES["file"]["name"]));
            echo "文件存储在"."upload/".$_FILES["file"]["name"];
        }
    }
}else{
    echo "文件格式不符合要求";
    echo "只能上传png jpg gif jpeg格式的文件并且文件大小要小于200kB";
}



?>