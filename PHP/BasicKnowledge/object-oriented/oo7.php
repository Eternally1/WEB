<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/7/26
 * Time: 20:47
 * Desc: __callStatic()动态创建以及延迟绑定。
 *对于断言函数assert()函数的使用，需要先激活。
 */
header("Content-Type:text/html;charset=utf8");
assert_options(ASSERT_ACTIVE, 1);
assert_options(ASSERT_WARNING, 0);
assert_options(ASSERT_QUIET_EVAL, 1);
/**
 * 定义一个抽象类ActiveRecord
 */
 abstract class ActiveRecord{
    //定义静态属性，只能通过类名::来访问
    protected static $table;
    protected $fieldvalues;
    public $select;

    //定义静态方法
    static function findById($id){
        $query = "select * from ".static::$table." where id = $id";
        //self表示对当前类的静态引用
        echo __CLASS__;//ActiceRecord
        echo "<br>";
        return self::createDomin($query);
    }

    function __get($fieldname){
//        echo "这个方法被调用";
        return $this->fieldvalues[$fieldname];
    }

    static function __callStatic($method, $args)
    {
        echo "__callStatic方法被调用";
        $field = preg_replace('/^findBy(\w*)$/','${1}',$method);
        $query = "select * from ".static::$table." where".$field = '$args[0]';
        return self::createDomin($query);
    }

    private static function createDomin($query){
        //Gets the name of the class the static method is called in.
        /**
         * 这里的类为什么不是Customer。
         */
        $klass = get_called_class();
        //这里输出的是Customer。
        echo "$klass";
        echo "<br>";
        $domain = new $klass();
        $domain->fieldvalues = array();
        $domain->select = $query;
        foreach($klass::$fields as $field=>$type){
            $domain->fieldvalues[$field] = 'TODO: set from sql result';
        }
        return $domain;
    }
}

class Customer extends ActiveRecord{
    protected static $table = 'custdb';
    protected static $fields = array(
        'id'=>'int',
        'email'=>'varchar',
        'lastname'=>'varchar'
    );
}

class Sales extends ActiveRecord{
    protected static $table = 'salesdb';
    protected static $fields = array(
        'id'=>'int',
        'item'=>'varchar',
        'qty'=>'int'
    );
}
//var_dump(Customer::findById(123));
assert("select * from custdb where id=123" == Customer::findById(123)->select);
/**
 * 下面的调用email时，因为Customer的类的实例中，只能访问select属性。因此在调用一个没有的
 * 属性的时候，这时候会调用__get()方法从而访问被保护的fieldvalues数组，取出数据
 */
assert("TODO: set from sql result" == Customer::findById(123)->email);
/**
 * 此时会调用__callStatic()方法，因为在Customer类中没有静态方法findByLastname().
 */
assert("select * from custdb where Lastname = 'Denoncourt'"== Customer::findByLastname('Denoncourt')->select);