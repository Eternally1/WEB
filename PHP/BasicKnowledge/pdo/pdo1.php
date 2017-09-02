<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/13
 * Time: 20:10
 */

//phpinfo();

//if(extension_loaded("PDO")){
//    echo "nothing";
//}else{
//    echo "yes";
//}
$dbms = 'mysql';//数据库类型
$host = 'localhost';
$dbname = 'myphp';
$user = 'root';
$pass = 'root';
//这里切记要使用双引号，否则不能识别出来。
$dsn = "$dbms: host= $host;dbname=$dbname";
echo $dsn;

try{
    $dbh = new PDO($dsn,$user,$pass);//初始化一个PDO对象
    echo "连接成功<br />";
    //进行一次搜索
    foreach($dbh->query('SELECT * FROM myguest')as $row){
        print_r($row);
    }
}catch(PDOException $e){
    die("Error!:".$e->getMessage().'<br />');
}