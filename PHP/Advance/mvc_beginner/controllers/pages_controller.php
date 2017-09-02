<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/14
 * Time: 21:10
 */

class PagesController{
    public function home(){
        $first_name = "Tim";
        $last_name = "Jhon";
        require_once('views/pages/home.php');
    }
    public function error(){
        require_once('views/pages/error.php');
    }
}