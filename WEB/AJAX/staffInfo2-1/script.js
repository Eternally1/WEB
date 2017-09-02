/**
 * 使用jQuery的ajax()方法
 */

$(document).ready(function () {
    $("#inquire").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1/staffinfo2-1/staffInfo.php?number=" + $("#keywords").val(),
            // url: "http://localhost/staffinfo2/staffInfo.php?number=" + $("#keywords").val(),
            // url: "staffInfo.php?number=" + $("#keywords").val(),
            dataType: "json",
            success: function (data) {
                //这里的data已经是js的对象了。
                // console.log(data);
                if (data.success) {
                    $("#searchResult").html(data.msg);
                } else {
                    $("#searchResult").html("出现错误," + data.msg);
                }
            },
            error: function (jqXHR) {
                alert("发生错误!" + jqXHR.status);
            }
        });
    });

    $("#save").click(function () {
        $.ajax({
            type: "POST",
            // url: "staffInfo.php",
            // url:"http://localhost/staffinfo2/staffInfo.php",
            url:"http://127.0.0.1/staffinfo2/staffInfo.php",
            dataType: "json",
            data: {
                name: $("#staffName").val(),
                number: $("#staffNumber").val(),
                sex: $("#staffSex").val(),
                job: $("#staffJob").val(),
            },
            success: function (d) {
                //这里的data已经是js的对象了。
                console.log(d);
                if (d.success) {
                    $("#createResult").html(d.msg);
                } else {
                    $("#createResult").html("出现错误," + d.msg);
                }
            },
            error: function (jqXHR) {
                alert("发生错误!" + jqXHR.status);
            }
        });
    });

});