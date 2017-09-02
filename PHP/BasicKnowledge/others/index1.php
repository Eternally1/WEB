<?php
header("Content-Type:text/html;charset=utf-8");
global $infor;
$infor = "I am global var";
function printInfo(&$name)
{
    $name = $name." Qiu";
}
$var_name = "Tom";
//此时传递的参数就不能是具体的值了
printInfo($var_name);
echo $var_name;

echo <<<strs
    <h1>heredoc</h1>
    <p>这里使用了heredoc</p>
strs;

/**
 * 类型转换
 */
$price = 15;
$new_price  = (float)$price;


/**
 * 可变变量
 */
$var_name = "Tom";
$$var_name = 23;
echo "$var_name  is $Tom years old";

/**
 * 常量的定义和使用
 */
define('TIREPRICE',100);
echo TIREPRICE;

//phpinfo();

/**
 * 执行操作符``
 */
$out = `dir c:`;
//echo $out;

/**
 * 测试和设置变量类型
 */
$pri = 5.0;
echo gettype($pri)."<br>";
settype($pri,"int");
echo gettype($pri);

$name_var = null;
if(isset($name_var)){
    echo "true";
}else{
    echo "false";
}
if(empty($name_var)){
    echo "true";
}else{
    echo "false";
}

$count = 2;
if($count>0):
    echo "yes";
endif;

?>
