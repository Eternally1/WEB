<?php
//首先包含Smarty类文件,如果出错会给出提示，同时继续执行
include_once('./libs/Smarty.class.php');
//实例化Smart类
$smarty = new Smarty();
//选择缓存文件夹
$smarty->cache_dir = "caches";
//关闭缓存，调试的时候建议关闭。实际运行的时候打开，用于减轻服务器压力
$smarty->caching = false;
//设置模板目录
$smarty->template_dir = "templates";
//设置编译目录
$smarty->compile_dir = "compiles";

?>