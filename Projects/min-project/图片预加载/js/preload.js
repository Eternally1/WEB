//图片预加载
(function($) {
    //构造函数
    function PreLoad(imgs, options) {
        //如果是一张图片的话，可能传递的是一个字符串，这里需要判断一下
        this.imgs = (typeof imgs === "string" ? [imgs] : imgs);
    }
    PreLoad.DEFAULTS = {
        each: null, //每张图片加载完成之后执行
        all: null //左右图片加载完成之后执行
    };
    // console.log(PreLoad);
})(jQuery);