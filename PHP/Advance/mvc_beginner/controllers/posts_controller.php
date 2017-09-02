<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/14
 * Time: 21:40
 */

class PostController{
    public function index(){
        //store all the posts in a variable
        $posts = Post::all();
        require_once('views/posts/index.php');
    }

    public function show(){
        //我们期望这样的一个url  ?controller=posts&action=show&id
        //如果没有id项，就redirect  pages/error.php
        if(!isset($_GET['id'])){
            return call('pages','error');
        }

        //否则根据给定的id获得正确的结果
        $post = Post::find($_GET["id"]);
        require_once('views/posts/show.php');
    }
}