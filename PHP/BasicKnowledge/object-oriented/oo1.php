<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/21
 * Time: 21:24
 * Desc：重载、final、instanceof
 * __get()  __set()魔术方法
 */
header("Content-Type:text/html;charset=utf-8");
class person{
    public $name = "default value";
    public $age = 30;

    function __get($key){
        return $this->$key;
    }
    function __set($key,$value){
        $this->$key = $value;
    }
    public function print_info(){
        echo "$this->name : $this->age";
        echo "<br >";
    }
    //final
    final function print_hello(){
        echo "hello,$this->name";
    }
}
//禁止student类被继承。
final class student extends person{
    //这里就重载了父类的属性
    public $name = "Tom";
    //重载父类的方法
    public function print_info(){
        //调用父类的print_info()方法
        parent::print_info();
        echo "name = $this->name age= $this->age ";
    }
}
$p1 = new student();
$p1->print_info();
echo $p1->name;
//下面这里会报一个Notice，gender是没有定义的属性
echo $p1->gender;
echo "p1 是student的实例? ";
echo $p1 instanceof student;//输出1