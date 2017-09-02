<?php
header("Content-Type:text/html;charset=utf-8");
echo "数组的相关使用";
echo "<br />";
//1、定义一个数组--数值数组
$car = array("volvo", "BMW", "fute");
//获取数组的长度,注意字符串中不能使用$car,否则会报错。
echo "car数组的长度是" . count($car);
//遍历数组
echo "遍历输出数组内容如下:";
echo "<br />";
for ($i = 0; $i < count($car); $i++) {
    echo $car[$i];
    echo "<br />";
}

//2、关联数组
$people = array("peter" => "35", "Tom" => "23", "Mary" => "25");
//遍历关联数组
echo "遍历关联数组如下：";
echo "<br />";
foreach ($people as $key => $value) {
    echo $key . "=" . $value . "Years old";
    echo "<br />";
}
echo "<br>";
echo "使用each  list来循环遍历";
echo "<br>";
reset($people);
while (list($peo, $age) = each($people)) {
    echo $peo . "-" . $age;
}
echo "<br >";

//3、数组进行排序
sort($car);
print_r($car);
echo "<br >";

//4、创建一个多维数组，balls
$balls = array(
    "football" => array(
        "desc" => "足球",
        "like" => "false"
    ),
    "basketball" => array(
        "desc" => "篮球",
        "like" => "true"
    )
);
print_r($balls);
echo "<br >";
echo $balls["football"]["desc"];

//4、range
echo "--------------------------------";
print_r(range(1, 10, 2));

//5、sort的几种不同使用
$prices = array(10, 23, 34, 12, 45, 6);
sort($prices, SORT_STRING);
print_r($prices);

/**
 * 多维数组的排序
 */
$products = array(
    array("Tom", 23),
    array("Jack", 30),
    array("Mary", 25)
);
//按年龄进行排序的比较函数
function compare($x, $y)
{
    if ($x[1] == $y[1]) {
        return 0;
    } elseif ($x[1] < $y[1]) {
        return -1;
    } else {
        return 1;
    }
}
usort($products,'compare');
print_r($products);

/**
 * 对数组进行重新排序 shuffle
 */
$names = array("Tom","Mary","Qiu","Dong","Sun","Liao");
//print_r($names);
//shuffle($names);
//echo "<br>";
//print_r($names);

/**
 * array_reverse(),返回值是原先数组的一个副本，这里将原先的
 * 数组覆盖了。
 */
$names = array_reverse($names);
print_r($names);

/**
 * 将文件中的内容载入数组
 */
$documentRoot = $_SERVER["DOCUMENT_ROOT"];
echo "根目录是".$documentRoot;

//将readme.txt文件加载到数组reader中,文件中每一行
//代表的是数组中的一个项
$reader = file($documentRoot."/readme.txt");
//print_r($reader);


$errors = array("err1"=>"undefined","err2"=>"null");
extract($errors);
echo "$err1   $err2 ";
?>