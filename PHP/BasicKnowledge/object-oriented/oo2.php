<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/21
 * Time: 21:45
 * Desc: Per-Class常量、使用静态方法、类型提示思想。
 */

class math{
    //Per-Class常量
    const pi = 3.1415926;
    static function multiple_input($input){
        /**
         * 在一个静态方法中，不能使用this关键字。因为可能会没有
         * 可以引用的对象实例。
         */
        return $input*$input;
    }
}
class math_child{
    public function print_input(math $m){
        //这里通过将math的对象实例当成参数，类型提示的思想
        return $m::multiple_input($m::pi);
    }
}
echo math::pi;
echo math::multiple_input(5);
$m = new math();
$m_c = new math_child();
//这里传递的参数就必须是math类的实例，否则会报错
echo $m_c->print_input($m);
/**
 * 克隆一个math对象
 */
$m1 = clone $m;
echo "-------------".$m1::pi;


?>