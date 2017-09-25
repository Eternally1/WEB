var myApi = {};
(function (exports) {
    function getCookie(name) {
        var cookieName = encodeURIComponent(name) + '=',
            cookieStart = document.cookie.indexOf(cookieName),
            cookieValue = null;
        if (cookieStart > -1) {
            var cookieEnd = document.cookie.indexOf(';', cookieStart);
            if (cookieEnd == -1) {
                cookieEnd = document.cookie.length;
            }
            cookieValue = decodeURIComponent(document.cookie.substring(cookieStart + cookieName.length, cookieEnd));
        }
        return cookieValue;
    }

    var token = getCookie('token') || "246ad74a45ed6ef5da3caf458bcab965";

    var hostname = 'http://yml666.com/stumanager';
    function postJSON(path, params, end, next) {
        var url = hostname + path;
        var body = 'token=' + token;
        for (var key in params) {
            body += '&' + key + '=' + params[key];
        }

        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                if (xhr.status === 200) {
                    success(JSON.parse(xhr.responseText))
                } else {
                    fail(xhr.status);
                }
            }
        }
        xhr.send(body);

        function success(response) {
            switch (response.status) {
                case 0:
                    end(null, response.data);
                    break;
                case 1003:
                    end(new Error('登陆超时，需要重新进入'));
                    break;
                case 1004:
                    end(new Error('权限不足'));
                    break;
                case 2002:
                    end(null, { contents: [], totalElements: 0, totalPages: 0 });
                    break;
                default: next(response);
            }
        }
        function fail(status) {
            var msg;
            if (status >= 400) msg = '客户端错误';
            if (status >= 500) msg = '服务器错误';
            end(new Error(msg));
        }
    }

    function postForm(path, formData, end, next) {
        var url = hostname + path;
        formData.append('token', token);

        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                if (xhr.status === 200) {
                    success(JSON.parse(xhr.responseText))
                } else {
                    fail(xhr.status);
                }
            }
        }

        xhr.send(formData);

        function success(response) {
            switch (response.status) {
                case 0:
                    end(null, res.data);
                    break;
                case 1003:
                    end(new Error('登陆超时，需要重新进入'));
                    break;
                case 1004:
                    end(new Error('权限不足'));
                    break;
                case 2002:
                    end(null, { contents: [], totalElements: 0, totalPages: 0 });
                    break;
                default: next(res);
            }
        }
        function fail(status) {
            var msg;
            if (status >= 400) msg = '客户端错误';
            if (starus >= 500) msg = '服务器错误';
            end(new Error(msg));
        }
    }

    exports.student = {
        getBetween: function (bound, beginUid, endUid, pageIndex, cb) {
            var path = '/guide/getStudentsByUidBetween.do';
            postJSON(path,
                {
                    bound: bound,
                    beginUid: beginUid,
                    endUid: endUid,
                    page: pageIndex,
                    num: 10
                },
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')); }
            );
        },
        getByUids: function (uids, cb) {
            var path = '/guide/getStudentsByUids.do';
            var str = '';
            uids.forEach(function (uid) { str += ',' + uid; });
            postJSON(path,
                {
                    uids: str.substring(1)
                },
                function (err, data) { cb(err, data) },
                function (res) {
                    cb(new Error('未知错误'))
                }
            );
        },
        getByName: function (bound, name, pageIndex, cb) {
            var path = '/guide/getStudentsByName.do';
            postJSON(path,
                {
                    bound: bound,
                    name: name,
                    page: pageIndex,
                    num: 1000,
                    fuzzy: true
                },
                function (err, data) { cb(err, data) },
                function (res) {
                    cb(new Error('未知错误'))
                }
            );
        },
        bindByUids: function (uids, cb) {
            var path = '/guide/bindStudents.do';
            var str = '';
            uids.forEach(function (uid) { str += ',' + uid; });
            postJSON(path,
                {
                    uids: str.substring(1)
                },
                function (err, data) { cb(err, data) },
                function (res) {
                    cb(new Error('未知错误'))
                }
            );
        },
        update: function (info, cb) {
            var path = '/guide/modifyStudentInfo.do'
            postJSON(
                path,
                info,
                function (err, data) { cb(err, data) },
                function (res) {
                    cb(new Error('未知错误'));
                }
            );
        }
    }

    exports.note = {
        getNotes: function (limits, page, num, cb) {
            var path = '/guide/getLeaveNotes.do';
            var params = JSON.parse(JSON.stringify(limits));
            params.page = page;
            params.num = num;
            postJSON(
                path,
                params,
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')); }
            );
        },
        updateState: function (lid, state, cb) {
            var path = '/guide/setLeaveNoteState.do';
            postJSON(
                path,
                {
                    lid: lid,
                    state: state
                },
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')); }
            );
        }
    }

    exports.sign = {
        add: function (signForm, cb) {
            var path = '/guide/launchSignIn.do';
            postJSON(
                path,
                signForm,
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')); }
            );
        },
        launched: function (page, num, cb) {
            var path = '/guide/getMySignInForms.do';
            postJSON(
                path,
                {
                    page: page,
                    num: num
                },
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')); }
            )
        },
        data: function (sfid, cb) {
            var path = '/guide/getSignInDatas.do';
            postJSON(
                path,
                {
                    sfid: sfid
                },
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')) }
            )
        },
        unsigned: function (sfid, cb) {
            var path = '/guide/getUnsignedStudents.do';
            postJSON(
                path,
                {
                    sfid: sfid
                },
                function (err, data) { cb(err, data) },
                function (res) { cb(new Error('未知错误')) }
            );
        }
    }

    // exports.forms = {
    //     postDynamicForm: function (title, form, pattern, cb) {
    //         var path = '/guide/saveOrUpdateDynamicForm.do';
    //         var params = { title, form, pattern }
    //         postJSON(path, params, cb);
    //     },
    //     getFormList: function (pageIndex, cb) {
    //         var path = '/guide/getMyDynamicForms.do';
    //         postJSON(
    //             path,
    //             {
    //                 pageIndex
    //             },
    //             function(err, data) { cb(err, data) },
    //             function(res)cb(new Error('未知错误'))
    //         )
    //     },
    //     getFormDataList: function (fid, pageIndex, cb) {
    //         var path = '/guide/getDynamicFormDatas.do';
    //         postJSON(path, pageIndex, { fid }, cb);
    //     }
    // }
} (myApi));
