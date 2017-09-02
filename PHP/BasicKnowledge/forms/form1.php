<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/16
 * Time: 20:16
 */
header("Content-Type:text/html;charset=utf-8");
echo "欢迎".$_POST["userName"]."!<br>";
echo "你的年龄是".$_POST["age"]."<br>";

/**
 * 关于下拉菜单的处理
 */
$site = isset($_POST['site'])?htmlspecialchars($_POST['site']):"";
if($site){
    //这里$site获取的就是前端界面中选择的值，然后再通过进一步的判断来得到想要的结果
    if($site == "runoob"){
        echo "菜鸟教程<br>";
    }else if($site == "taobao"){
        echo "淘宝<br>";
    }else if($site == "qiu"){
        echo "邱<br>";
    }
}else{
    echo "未选择符合标准的站点<br>";
}
/**
 * 下拉菜单多选的处理
 */
$interest = isset($_POST["interest"])?$_POST['interest']:"";
if(is_array($interest)){
    $array = array(
        "basketball"=>"Playing basketball",
        "football"=>"Playing football",
        "badminton"=>"Playing badminton"
    );
    echo "你的爱好有:";
    foreach($interest as $value){
        echo $array[$value]."\t";
    }
    echo "<br>";
}else{

}
/**
 * 单选按钮处理
 */
$gender = isset($_POST["gender"])?htmlspecialchars($_POST["gender"]):"";
if($gender){
    if($gender=="male"){
        echo "性别：男<br>";
    }else if($gender == "female"){
        echo "性别：女<br>";
    }
}else{
    echo "没有选择性别";
}
/**
 * 处理复选框
 */
$city = isset($_POST["city"])?$_POST["city"]:"";
if(is_array($city)){
    $cities =array(
        "beijing"=>"北京city",
        "shanghai"=>"上海city",
        "shenzhen"=>"深圳city"
    );
    echo "喜欢的城市有：";
    foreach($city as $value){
        echo $cities[$value]."\t";
    }
}
?>