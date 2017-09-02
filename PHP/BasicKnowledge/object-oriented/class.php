<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/16
 * Time: 19:42
 */
    header("Content-Type:text/html;charset=utf-8");
    //1、类的定义
    class Site{
        //定义成员变量
        var $url;
        var $title;

        //构造函数
        function __construct($par1,$par2)
        {
            $this->url = $par1;
            $this->title = $par2;
        }

        //析构函数
        function __destruct(){
            echo "销毁".$this->title;
        }

        //成员函数
        function setUrl($par){
            $this->url = $par;
        }
        function getUrl(){
            echo $this->url.PHP_EOL;
        }
        function setTitle($par){
            $this->title = $par;
        }
        function getTitle(){
            echo $this->title.PHP_EOL;
        }
    }

    //2、创建对象
    $runoob = new Site("good","great");
    $taobao = new Site("tao","bao");

    //3、使用该对象
    $runoob->getTitle();
    $taobao->getTitle();


    //3、继承
    class Child_site extends Site{
        var $loc;
        function setLoc($par){
            $this->loc = $par;
        }
        function getLoc(){
            echo $this->loc;
        }
        //4、方法的重写
        function getTitle(){
            echo $this->title."--child";
        }

    }

    /**
     * 此外还有很多其他的使用，
     * 访问控制
     * 接口
     * 抽象类
     * final static等使用
     */
?>