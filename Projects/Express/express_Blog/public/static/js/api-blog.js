const myApi = {};
(function(exports) {

    let hostname = 'http://localhost:3000';

    //这里直接才用的是json数据格式提交到服务器
    function postJSON(path, params, end, next) {
        let url = hostname + path;
        console.log(url);
        let body = "";
        for (var key in params) {
            body += key + "=" + params[key] + "&";
        }
        let data = body.substring(0, body.length - 1);
        console.log(data);
        const xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        //设置请求头信息
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status === 200) {
                    // console.log(xhr.responseText);
                    // console.log(typeof xhr.responseText);//string
                    success(JSON.parse(xhr.responseText));
                } else {
                    fail(xhr.status);
                }
            }
        }
        xhr.send(data);

        function success(res) {
            switch (res.status) {
                case 0:
                    end(null, res.data);
                    break;
                case 2002:
                    end(new Error(res.msg));
                    break;
                default:
                    next(res);
            }
        }

        function fail(status) {
            let msg;
            if (status >= 400) msg = '客户端错误';
            if (status >= 500) msg = '服务器错误';
            end(new Error(msg));
        }
    }

    /**
     * publish文章界面
     */
    exports.publishArticle = function(info, cb) {
        let path = '/add';
        postJSON(path, info,
            function(err, data) {
                cb(err, data);
            },
            function(res) {
                cb(new Error('未知错误'));
            });
    }


    /**
     * 这里写一个测试方法
     */
    exports.test = function(info, cb) {
        let path = '/test';
        postJSON(path,
            info,
            //end
            function(err, data) {
                cb(err, data)
            },
            //next
            function(res) {
                cb(new Error('未知错误'));
            });
    }


})(myApi)