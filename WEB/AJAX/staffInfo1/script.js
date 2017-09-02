/**
 * 注意事项：
 *  1、使用post请求的时候一定注意使用setRequestHeader()方法设置相应的。
 * 2、post中提交的数据，目前使用的是字符串提交。
 */


//给查询按钮添加时事件
document.getElementById("inquire").onclick = function () {
    //发送Ajax查询请求，并且处理
    //1、实例化XMLHttpRequest对象；
    var request;
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest(); //IE7+,Firefox,Chrome,Opera,Safari
    } else {
        request = new ActiveXObject("Microsoft.XMLHTTP"); //IE5 IE6
    }
    request.open("GET", "staffInfo.php?number=" + document.getElementById("keywords").value);
    //2、发送请求;
    request.send();

    //3、监听事件
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                var data = JSON.parse(request.responseText); //转换成js对象
                console.log(data);
                if (data.success) {
                    document.getElementById("searchResult").innerHTML = data.msg;
                } else {
                    document.getElementById("searchResult").innerHTML = "出现错误," + data.msg
                }
            } else {
                //这个是什么时候发生的。
                alert("发生错误!" + request.status);
            }
        }
    }
}

//新建员工事件
document.getElementById("save").onclick = function () {
    //发送Ajax查询请求，并且处理
    //1、实例化XMLHttpRequest对象；
    var request;
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest(); //IE7+,Firefox,Chrome,Opera,Safari
    } else {
        request = new ActiveXObject("Microsoft.XMLHTTP"); //IE5 IE6
    }
    request.open("POST", "staffInfo.php");
    var data = "name=" + document.getElementById("staffName").value +
        "&number=" + document.getElementById("staffNumber").value +
        "&sex=" + document.getElementById("staffSex").value +
        "&job=" + document.getElementById("staffJob").value
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //2、发送请求;
    request.send(data);

    //3、监听事件
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                var data = JSON.parse(request.responseText); //转换成js对象
                if (data.success) {
                    document.getElementById("createResult").innerHTML = data.msg;
                } else {
                    document.getElementById("createResult").innerHTML = "出现错误," + data.msg
                }
            } else {
                //比如当请求的php文件不存在的时候，就会出现404错误
                alert("发生错误!" + request.status);
            }
        }
    }
}
