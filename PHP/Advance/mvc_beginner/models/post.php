<?php

/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/14
 * Time: 21:51
 */
class Post
{
    //定义三个属性
    public $id;
    public $author;
    public $content;

    public function __construct($id, $author, $content)
    {
        $this->id = $id;
        $this->author = $author;
        $this->content = $content;
    }

    public static function all()
    {
        $list = [];
        $db = Db::getInstance();

        $result = $db->query("SELECT * FROM posts");

        //$reqult->fetchAll()得到的是一个结果数组。使用foreach循环数组
        foreach ($result->fetchAll() as $post) {
            //它会在每次循环的时候自动加到里面去
            $list[] = new Post($post["id"], $post["author"], $post["content"]);
        }
        print_r($list);
        return $list;
    }

    public static function find($id)
    {
        $db = Db::getInstance();
        $id = intval($id);
        //将会使用$id  替换:id
        $req = $db->prepare("SELECT * FROM posts WHERE id =:id");
        $req->execute(array(':id'=>$id));
        $post = $req->fetch();

        return new Post($post["id"], $post["author"], $post["content"]);
    }

}