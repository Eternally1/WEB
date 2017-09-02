<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/13
 * Time: 21:38
 */
//加载数据库连接文件
require_once('connection.php');

if(isset($_GET['controller'])&& isset($_GET['action'])){
    $controller = $_GET['controller'];
    $action = $_GET['action'];
}else{
    $controller = 'pages';
    $action = 'home';
}
require_once('views/layout.php');