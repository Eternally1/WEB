/**
 * 1、从第5条开始隐藏后面的品牌，最后一条“其他品牌星级除外”
 * 2、当用户点击“显示全部品牌”的时候，将执行下面操作
 * 2.1、显示隐藏品牌
 * 2.2、“显示全部品牌”按钮文本切换成“精简显示品牌”
 * 2.3、高亮显示推荐品牌
 * 3、当用户单击“精简显示品牌”的时候
 * 3.1、从第5条开始隐藏后面的品牌，最后一条“其他品牌相机除外”
 * 3.2、“精简显示品牌”按钮文本切换成“全部显示推荐品牌”
 * 3.3、去掉高亮显示的推荐品牌。
 */
$(document).ready(function () {

    var $category = $("ul li:gt(5):not(:last)");
    //1、从第5条开始隐藏
    $category.hide();
    //2、用户点击事件处理
    var $toggleBtn = $('div.showmore > a');


    $toggleBtn.click(function () {
        //判断从第5个开始后面的是不是显示的
        if ($category.is(":visible")) {
            $category.hide();
            $("div.showmore a span").text("显示全部品牌");
            //注意下面这个使用filter过滤的函数
            //filter(expr)筛选出与指定表达式匹配的元素集合，其中expr可以是多个选择器的组合
            $("ul li").filter(":contains('佳能'),:contains('尼康'),:contains('奥林巴斯')")
                .removeClass("promoted");
            return false; //超链接不跳转
        } else {
            $category.show();
            $("div.showmore a span").text("精简显示品牌");
            $("ul li").filter(":contains('佳能'),:contains('尼康'),:contains('奥林巴斯')")
                .addClass("promoted");
            return false; //超链接不跳转
        }
    });

    //另一种方式
    //查阅API发现这个toggle()方法从1.8开始已经过时，不在使用
    // $toggleBtn.toggle(function () {
    //     $category.show();
    //     $("div.showmore a span").text("精简显示品牌");
    //     $("ul li").filter(":contains('佳能'),:contains('尼康'),:contains('奥林巴斯')")
    //         .addClass("promoted");
    //     return false; //超链接不跳转
    // }, function () {
    //     $category.hide();
    //     $("div.showmore a span").text("显示全部品牌");
    //     //注意下面这个使用filter过滤的函数
    //     //filter(expr)筛选出与指定表达式匹配的元素集合，其中expr可以是多个选择器的组合
    //     $("ul li").filter(":contains('佳能'),:contains('尼康'),:contains('奥林巴斯')")
    //         .removeClass("promoted");
    //     return false; //超链接不跳转
    // });
});