
    <?php
    /**
     * Created by PhpStorm.
     * User: 14259
     * Date: 2017/7/16
     * Time: 21:29
     */
    /**
     * 这里的表单验证并没有完全成果，不知道出错的时候怎么返回给客户端信息，
     * 客户端应该是需要使用ajax，然后通过实时的想服务器端发送请求来实现交互。
     */
    header("Content-Type:text/html;charset=utf-8");
    //定义变量并且设置为空值
    $nameErr = $emailErr = $genderErr = $websiteErr = "";
    $name = $email = $gender = $website = $comment = "";

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        //判断名字输入是否为空
        if(empty($_POST["name"])){
            $nameErr = "名字是必须的";
        }else{
            $name = test_input($_POST["name"]);
            //判断名字是否为6-20位的字母 空格的组合
            if(!preg_match("/^[a-zA-Z ]{6,20}$/",$name)){
                $nameErr = "名字需要为6-20位的字母数字组合。";
            }
        }
        //判断邮箱是否为空
        if(empty($_POST["email"])){
            $emailErr = "邮箱是必须的";
        }else{
            $email = test_input($_POST["email"]);
            //检验邮箱格式是否合法
            if(!preg_match("/[\w-]+\@[\w\-]+\.[\w\-]+/",$email)){
                $emailErr = "邮箱格式不合法";
            }
        }
        //判断URL是否合法
        if(empty($_POST["website"])){
            $website = "";
        }else{
            $website = test_input($_POST["website"]);
            //检测URL地址是否合法
            if(!preg_match("/\b((https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)){
                $websiteErr = "非法的URL的地址";
            }
        }
        //判断评论是否为空
        if(empty($_POST["comment"])){
            $comment = "";
        }else{
            //将comment格式化，然后保存
            $comment = test_input($_POST["comment"]);
        }
        //判断性别
        if(empty($_POST["gender"])){
            $genderErr = "性别是必须的";
        }else{
            $gender = test_input($_POST["gender"]);
        }

    }

    function test_input($data){
        //溢出左右多余空格
        $data = trim($data);
        //删除反斜杠
        $data = stripslashes($data);
        //将预定义的字符转换成实体
        $data = htmlspecialchars($data);
        return $data;
    }


    ?>


