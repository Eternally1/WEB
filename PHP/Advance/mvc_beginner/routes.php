<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/13
 * Time: 21:58
 */
//echo $controller . " controller " . $action . "action";
function call($controller, $action)
{
    //require the file that matches the controller name
    require_once('controllers/' . $controller . '_controller.php');

    //create a new instance of the needed controller
    switch ($controller) {
        case 'pages':
            $controller = new PagesController();
            break;
        case 'posts':
            require_once('models/post.php');
            $controller = new PostController();
            break;
    }
    //call the action
//    $controller->$action();//这种貌似也可以
    $controller->{$action}();
}

//一个用于控制器和action的列表
$controllers = array("pages" => ['home', 'error'],
                    "posts"=>['index','show']);

if (array_key_exists($controller, $controllers)) {
    if (in_array($action, $controllers[$controller])) {
        call($controller, $action);
    } else {
        call('pages', 'error');
    }
} else {
    call("pages", "error");
}