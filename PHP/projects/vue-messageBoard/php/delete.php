<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/4
 * Time: 20:23
 * Desc: 删除留言
 */
//加载数据库配置
require('../config/config.inc.php');
//判断是否登录
if(!isset($_SESSION) || !$_SESSION["login"]){
    $arr  =array(
        "status"=>"3001",
        "msg"=>"没有登录不能删除"
    );
    echo json_encode($arr);
}
$id = $_GET["id"];
/**
 * 同时从两个表中删除会出现错误，虽然显示的删除成功，
 * 但是在数据库中发现数据并没有被删除。原因是，如果数据库中对应的没有
 * 留言回复就会出现问题，因此在删除前可以判断一下。
 */
//$deleteSql = "delete a,b from info a,reply b where a.id= '$id' and a.id = b.info_id";
//从info表中删除留言
$deleteMsg = "delete from info where id= $id";
$selectReply = "select * from reply where info_id= $id ";
if($conn->query($deleteMsg)){
    //接着判断是否有留言回复
    $result = $conn->query($selectReply);
    if($result->num_rows>0){
        $conn->query("delete from reply where info_id= $id");
    }
    $arr = array(
        "status"=>true,
        "msg"=>"删除成功"
    );
    echo json_encode($arr);
}else{
    $arr = array(
        "status"=>false,
        "msg"=>$conn->error
    );
    echo json_encode($arr);
}