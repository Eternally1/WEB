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
require('../config/config.inc.php');
//设定每页显示的条目数
$pagesize = 5;
if (isset($_GET["page"]) && (!empty($_GET["page"]))) {
    //如果传入的是第二页，那么就是从第一页的末尾开始，因此这里需要减去一
    $page = $_GET["page"]-1;
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
//var_dump($result_json);
/**
 * 判断管理员是否登录
 */

if(empty($_SESSION["login"])){
    $isManager = false;
}elseif($_SESSION["login"] == true){
    $isManager = true;
}

$arr_result = array(
    "status"=>"1001",
    "msg"=>"数据返回成功",
    "messages"=>$result_json,
    "totalPages"=>$totalpage,
    "numRecords"=>$numRecords,
    //目前不是管理员登录
    "isManager"=>$isManager
);
echo json_encode($arr_result);
//echo $result_json;
//var_dump($arr_temp);

//echo "--------------------\n";
//echo is_string($result_json)."是string格式";



?>