//跨浏览器事件处理程序
var eventUtil = {
            /**
             * 添加句柄
             * element  给谁添加
             * type     事件类型(不带on的)
             * handler  事件处理程序
             */
            addHandler:function(element,type,handler){
                //判断是否支持DOM2级
                if(element.addEventListener){
                    element.addEventListener(type,handler,false);
                }else if(element.attachEvent){
                //判断是否是IE浏览器
                    element.attachEvent("on"+type,handler);
                }else{
                //支持DOM0级
                element["on"+type] = handler;
                }
            },
            //删除句柄
            removeHandler:function(element,type,handler){
                //判断是否支持DOM2级
                if(element.removeEventListener){
                    element.removeEventListener(type,handler,false);
                }else if(element.detachEvent){
                //判断是否是IE浏览器
                    element.detachEvent("on"+type,handler);
                }else{
                //支持DOM0级
                element["on"+type] = null;
                }
            },
            //获取事件对象
            /**
             * 虽然网上说低版本IE和Opera使用window.event，但是通过在
             * IE11中模拟Opera和低版本浏览器，发现使用event或者window.event
             * 并不影响。
             */
            getEvent:function(enent){
                return event? event: window.event;
            },
            //获取事件类型
            getType:function(event){
                return event.type;
            },
            //返回事件元素
            getElement:function(event){
                return event.target || event.srcElement;
            },
            //阻止事件默认行为
            preventDefault:function(event){
                if(event.preventDefault){
                    event.preventDefault();
                }else{
                    event.returnValue = false;
                }
            },
            //阻止冒泡
            stopPropagation:function(event){
                if(event.stopPropagation){
                    event.stopPropagation();
                }else{
                    event.cancelBubble = true;
                }
            }
        };
    //使用
    // eventUtil.addHandler(btn,'click',showMessage);