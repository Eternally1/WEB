<?php
/**
 * Created by PhpStorm.
 * User: 14259
 * Date: 2017/8/13
 * Time: 21:38
 */

class Db{
    private static $instance = NULL;

    /**
     * make __construct() and __clone private so that no one can call
     * new Db();
     */
    private function __construct(){}
    private function __clone(){}

    public static function getInstance(){
        if(!isset(self::$instance)){
            $pdo_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;
            self::$instance = new PDO('mysql:host=localhost;dbname=myphp','root','root');
        }
        return self::$instance;
    }
}