<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/27
 * Time: 19:10
 * Desc: __toString()方法，如果类定义了__toString()方法，那么在测试的时候，echo打印
 * 对象体，对象就会自动调用它所属类定义的__toString()方法。
 *
 * 接口：interface
 * 通常一个接口的的实现类仅实现改接口所具有的方法，做到专一，当然，这不是一成不变的。
 *
 * Iterator：DirectoryIterator的使用
 */

define("RUN", "run quickly");

interface mobile
{
    /**
     * 接口中的所有方法都是抽象的，没有程序体
     * 接口中可以包含常量
     */
    const CONSTRUN = "run";
    public function run();

}

class plain implements mobile
{
    private $name = "plain";
    public function run()
    {
        echo "I am plate!\n";
    }
    //__toString()方法
    public function __toString(){
            return  "My name is $this->name \n";
    }
}
$p1 = new plain();
echo $p1;
$p1->run();

/**
 * DirectoryIterator的使用
 */
//$arr = array(1,2,3,4,5);
$itera = new DirectoryIterator(dirname(__FILE__));
foreach($itera as $value){
    echo $value->getFilename(),"\t",$value->getSize(),PHP_EOL;
}

?>