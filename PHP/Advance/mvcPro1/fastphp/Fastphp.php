<?php

/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/10
 * Time: 21:42
 */
class Fastphp
{
    protected $_config = [];

    public function __construct($config){
        $this->_config = $config;
    }

    //运行程序
    public function run(){
        //碰到没有定义的类，就执行loadClass;
        spl_autoload_register(array($this,'loadClass'));
        $this->setReporting();
        $this->removeMagicQuotes();
        $this->unregisterGlobals();
        $this->setDbConfig();
        $this->route();
    }

    //路由处理
    public function route(){
        $controllerName = $this->_config['defaultController'];
        $actionName = $this->_config['defaultAction'];
        $param = array();

        $url = $_SERVER['REQUEST_URI'];
        //清除?号之后的内容
        $position = strpos($url,'?');
        $url = $position === false?$url:substr($url,0,$position);

        //删除前后的  '/'
        $url = trim($url,'/');
        if($url){
            //使用'/'分割字符串，并保存在数组中
            $urlArray = explode('/',$url);
            //删除空的数组元素
            $urlArray = array_filter($urlArray);

            //获取控制器名
            //将首字母大写，然后返回
            $controllerName = ucfirst($urlArray[0]);

            //获取动作名
            array_shift($urlArray);//删除数组第一个元素
            $actionName = $urlArray?$urlArray[0]:$actionName;

            //获取URL参数
            array_shift($urlArray);
            $param = $urlArray ? $urlArray:array();
        }
        //判断控制器和操作是否存在
        $controller = $controllerName. 'Controller.class';
        if(!class_exists($controller)){
            exit($controller."控制器不存在");
        }
        if(!method_exists($controller,$actionName)){
            exit($actionName."方法不存在");
        }

        //如果控制器和操作名存在，则实例化控制器，因为控制器对象里面还会
        //用到控制器名和操作名，所以实例化的时候把他们的名称也传递进去。结合
        //Controller基类一起看
        $dispatch = new $controller($controllerName,$actionName);

        //$dispatch保存控制器实例化后的对象，我们就可以调用它的方法
        //也可以向方法中传递参数，以下等同于$dispatch->actionName($param)
        call_user_func_array(array($dispatch,$actionName),$param);
    }

    //检测开发环境
    public function setReporting(){
        if(APP_DEBUG === true){
            //报告所有的错误
            error_reporting(E_ALL);
            ini_set('display_errors','On');
        }else{
            error_reporting(E_ALL);
            ini_set('display_errors','Off');
            ini_set('log_errors','On');
        }
    }

    //配置数据库信息
    public function setDbConfig(){
        if($this->_config['db']){
            Model::$dbConfig = $this->_config['db'];
        }
    }

    //删除敏感字符
    public function removeMagicQuotes(){
        //始终返回false，已经从PHP中移除了  php5.4.0
        if(get_magic_quotes_gpc()){
            //因此这里面的就没有必要了
        }
    }

    /**
     * @param $class
     * register_globals()
     */
    public function unregisterGlobals(){
        //里面的是当register_globals设置为on的时候的操作
    }

    //自动加载控制类和模型类
    public static function loadClass($class){
        $frameworks = __DIR__.'/'.$class.'.php';
        $controllers = APP_PATH.'application/controllers/'.$class.'.php';
        $models = APP_PATH.'application/models/'.$class.'.php';

        if(file_exists($frameworks)){
            //加载框架核心类
            include $frameworks;
        }elseif(file_exists($controllers)){
            //加载应用控制类
            include $controllers;
        }elseif(file_exists($models)){
            //加载应用模型类
            include $models;
        }else{
            //错误代码
        }
    }
}
