<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/22
 * Time: 19:25
 * Desc:迭代器的使用
 */
/**
 * 编写一个ObjectIterator实现Iterator接口
 */
class ObjectIterator implements Iterator{
    private $obj;
    private $count;
    private $currentIndex;
    function __construct($obj)
    {
        $this->obj = $obj;
        $this->count = count($this->obj->data);
    }
    //将内部数据指针设置回数据开始处
    function rewind(){
        $this->currentIndex = 0;
    }
    //判断数据指针的当前位置是否存在数据
    function valid(){
        return $this->currentIndex < $this->count;
    }
    //返回数据指针的值
    function key(){
        return $this->currentIndex;
    }
    //返回保存在当前数据指针的值
    function current(){
        return $this->obj->data[$this->currentIndex];
    }
    //函数在数据中移动数据指针的位置
    function next(){
        $this->currentIndex++;
    }
}
class Object implements IteratorAggregate{
    public $data = array();
    function __construct($input)
    {
        $this->data = $input;
    }


    public function getIterator()
    {
        // TODO: Implement getIterator() method.
        return new ObjectIterator($this);
    }
}

//此时会报错。因为在上面定义的current中找不到对应索引的值
$obj = new Object(array("Tom"=>2,"mary"=>3,4,57,1,3));
$my_iterator = $obj->getIterator();
for($my_iterator->rewind();$my_iterator->valid();$my_iterator->next()){
    $key = $my_iterator->key();
    $value = $my_iterator->current();
    echo "$key = $value ";
    echo "<br>";
}