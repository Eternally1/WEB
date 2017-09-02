<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/10
 * Time: 21:14
 */
//应用目录为当前目录
define("APP_PATH",__DIR__."/");

//开启调试模式
define('APP_DEBUG',true);

//加载框架文件
require(APP_PATH.'fastphp/Fastphp.php');

//加载配置文件
$config = require(APP_PATH.'config/config.php');

//实例化框架类
(new Fastphp($config))->run();



