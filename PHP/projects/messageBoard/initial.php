<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/31
 * Time: 20:09
 * Desc: 入口文件
 * 注意这里的分页技术的实现
 */
//加载数据库配置文件
require('./config.inc.php');
include('./Smarty.inc.php');
//设定每页显示的条目数
$pagesize = 5;
if (isset($_GET["page"]) && (!empty($_GET["page"]))) {
    $page = $_GET["page"];
} else {
    $page = 0;
}
//连表组合查询sql语句
$sql = "select c1.* , c2.reply_time,c2.reply from info c1 LEFT JOIN reply c2 on (c1.id = c2.info_id) ORDER BY c1.id DESC";
//从数据库中取出结果集并赋值给$result
$result = $conn->query($sql);
//获得结果集中的总条数
$numRecords = $result->num_rows;
//获得总页数
$totalpage = ceil($numRecords / $pagesize);
//拼接翻页的SQL语句
$recordSql = $sql . " LIMIT " . $page * $pagesize . "," . $pagesize;
//将结果集保存在$result中
//echo "$recordSql";
//此时的结果集中只有5条数据。
$result = $conn->query($recordSql);
//var_dump($result);
//将从数据库中取出的数据储在数组中
$arr_temp = array();
if ($result->num_rows > 0) {
    //输出数据
    while ($row = $result->fetch_assoc()) {
        array_push($arr_temp,$row);
    }
} else {
    echo "0 结果";
}
//var_dump($arr_temp);
//将数组编码成JSON格式,返回值是json编码的string格式
$result_json = json_encode($arr_temp);
//echo $result_json;
//var_dump($arr_temp);
/**
 * 因为这里返回的数据相当于二维数组，在前端界面中直接使用二维数组格式
 * 如果转换成json字符串格式，那么到前端界面还需要进一步的修改成json对象格式。
 */
$smarty->assign("comments",$arr_temp);
$smarty->display("helloworld.html");
//echo "--------------------\n";
//echo is_string($result_json)."是string格式";



?>