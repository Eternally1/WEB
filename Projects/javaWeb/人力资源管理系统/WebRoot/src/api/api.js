const myApi = {};
(function(api) {
    let hostname = "http://localhost:8080/javaWeb";
    let token = null;

    function postJSON(path, params, end, next) {
        let url = hostname + path;
        var body = 'token=' + token;
        for (var key in params) {
            body += '&' + key + '=' + params[key];
        }
        console.log(body);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status === 200) {
                    // console.log(xhr.responseText);
                    success(JSON.parse(xhr.responseText))
                } else {
                    fail(xhr.status);
                }
            }
        }
        xhr.send(body);

        function success(response) {
            switch (response.status) {
                case "1002":
                    end(null, response.data);
                    break;
                case "1001":
                    end(new Error('用户已存在'));
                    break;
                case 1004:
                    end(new Error('权限不足'));
                    break;
                case 2002:
                    end(null, { contents: [], totalElements: 0, totalPages: 0 });
                    break;
                default:
                    next(response);
            }
        }

        function fail(status) {
            var msg;
            if (status >= 400) msg = '客户端错误';
            if (status >= 500) msg = '服务器错误';
            end(new Error(msg));
        }
    }
    /**
     * 人员信息录入
     */
    api.user = {
            addUser: function(user, cb) {
                let path = "/adduser.action";
                postJSON(path, user,
                    function(err, data) {
                        cb(err, data);
                    },
                    function(res) {
                        cb(new Error("未知错误"));
                    });
            },
            updateUser: function(user, cb) {
                let path = "/updateuser.action";
                postJSON(path, user,
                    function(err, data) {
                        cb(err, data);
                    },
                    function(res) {
                        cb(new Error("未知错误"));
                    });
            }
        },
        api.recruit = {
            addRecruit: function(recruit, cb) {
                let path = "/job/addjob.action";
                postJSON(path, recruit,
                    function(err, data) {
                        cb(err, data);
                    },
                    function(res) {
                        cb(new Error("未知错误"));
                    });
            }
        }
}(myApi));