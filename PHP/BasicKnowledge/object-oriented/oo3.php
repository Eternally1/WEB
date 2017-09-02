<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/22
 * Time: 19:03
 * Desc: 方法的重载__call()，当调用一个不可访问的方法（如未定义或者不可见）时，
 * __call()方法就会被调用。
 * note: 不能实现任何的display方法
 */

class Disp{
    function displayObject($obj){
        return $obj."-----obj------<br>";
    }
    function displayArray($arr){
        echo "-----------array------------<br>";
        return $arr;
    }
    function displayScalar($oth){
        echo "$oth -------oth-----<br>";
    }

    /**
     * @param $method 要调用的方法名
     * @param $param   是一个数据，包含要传递给方法的参数。
     */
    public function __call($method,$param){
        //可以使用switch结构。
        if($method == "display"){
            if(is_object($param[0])){
                $this->displayObject($param[0]);
            }elseif(is_array($param[0])){
                $this->displayArray($param[0]);
            }else{
                $this->displayScalar($param[0]);
            }
        }
    }
}
$dis = new Disp();
//相当于这里虽然调用了display方法，但是类中并没有定义
//因此回去查找__call()方法。
print_r  ($dis->display(array(1,2,3)));