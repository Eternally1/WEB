<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/22
 * Time: 19:22
 * Desc:通过foreach()取出一个对象的所有属性
 */
class person{
    public $name = "Tom";
    protected $age = 22;
    private $gender = "male";

    public function __toString(){
        return (var_export($this,TRUE));
    }
}
$p = new person();
//这里调用类中定义的__toString()方法，然后
//打印输出所有的类中的属性
echo $p;
foreach($p as $attr){
    //可以发现私有属性，以及受保护属性没有输出
    echo "$attr <br>";
}