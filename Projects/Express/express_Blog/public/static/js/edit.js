/**
 * markdown格式转换
 */
let rowText = document.getElementsByClassName('rowText')[0];
let markedText = document.getElementsByClassName('markedText')[0];
rowText.oninput = function() {
    markedText.innerHTML = marked(this.value);
};

/**
 * 标签删除事件
 */
let tags = document.getElementsByClassName("tags")[0];
//获得tags下面的所有a标签
let aTags = tags.getElementsByTagName("a");
//获取tags下面的所有li标签
let liTags = tags.getElementsByTagName("li");
//存储当前点击的a标签的索引，初始值为-1;
// let index = -1;
//添加a标签点击事件--除去最后的一个a标签
for (let i = 0; i < aTags.length - 1; i++) {
    liTags[i].style.display = "block";
    aTags[i].onclick = function() {
        {
            {
                //每次删除之后对应的li标签数量也会减少，因此每次点击事件都要重新获取liTags
                //index = i;
                //先将他们隐藏起来
                liTags[i].style.display = "none";
            }
        }
    }
}

/**
 * 创建遮罩层
 */
function createMask() {
    //1、获取body页面的宽度和高度
    let sHeight = document.documentElement.scrollHeight;
    let sWidth = document.documentElement.scrollWidth;
    //2、获取可视区的高度
    let cHeight = document.documentElement.clientHeight;
    //3、创建遮罩层div插入body
    let oMask = document.createElement('div');
    oMask.id = "oMask";
    oMask.style.height = sHeight + "px";
    document.getElementsByClassName('edit-wrap')[0].appendChild(oMask);
}

/**
 * 控制遮罩层和对话框的显示
 */

//获取对话框
let createTags = document.getElementsByClassName('createTags')[0];
//new tag事件监听--tags下面的最后一个a标签
let addTag = document.getElementsByClassName('addTag')[0];
addTag.onclick = function() {
    if (!document.getElementById('oMask')) {
        createMask();
    }
    //如果已经创建了oMask，就将它的display属性设置为block
    document.getElementById("oMask").style.display = "block";
    //显示添加tag的对话框
    if (createTags.style.top == 0 && createTags.style.left == 0) {
        createTags.style.display = "block";
        //如果没有设置top和left就设置，当再次点击的时候就不用再次设置了
        createTags.style.top = (document.documentElement.clientHeight - createTags.offsetHeight) / 2 + "px";
        createTags.style.left = (document.documentElement.scrollWidth - createTags.offsetWidth) / 2 + "px";
        console.log(document.documentElement.clientHeight + "," + document.documentElement.scrollWidth);
        //这里输出的是 0,0
        console.log(createTags.offsetHeight + "," + createTags.offsetWidth);
    }
    createTags.style.display = "block";
    //显示对话框里面的标签
    updateTags();
    /**
     * 弹出框上面标签删除的实现
     */
    let choosedTags = document.getElementsByClassName('choosedTags')[0];
    let aAll = choosedTags.getElementsByTagName('a');
    let liAll = choosedTags.getElementsByTagName('li');
    for (let i = 0; i < aAll.length; i++) {
        aAll[i].onclick = function() {
            liAll[i].style.display = "none";
        }
    }
}

/**
 * 弹出的对话框添加按钮实现
 */
let add = document.getElementsByClassName("add")[0];
let tagCont = document.querySelector(".input-cont");
add.onclick = function() {
    // alert('..')
    //判断input内容是否为空
    if (tagCont.value) {
        //创建li标签
        let liTag = document.createElement("li");
        liTag.innerHTML = tagCont.value + "<a href='#'>X</a>";
        liTag.style.display = "block";
        document.getElementsByClassName("choosedTags")[0].appendChild(liTag);
        //清空输入框
        tagCont.value = "";
    } else {
        //如果input内容为空
        alert("请输入标签内容");
    }
}

/**
 * 弹出框里面的对应的标签应该是页面上显示的标签
 * 获取页面上的标签，然后显示在弹出框中
 */
function updateTags() {
    //获取tags下面的所有li标签
    let liTags = tags.getElementsByTagName("li");
    let choosedTags = document.getElementsByClassName('choosedTags')[0];
    choosedTags.innerHTML = "";
    //判断li标签的display属性值
    for (let i = 0; i < liTags.length; i++) {
        if (liTags[i].style.display == "block") {
            let liTag = document.createElement('li');
            liTag.innerHTML = liTags[i].innerHTML;
            liTag.style.display = "block";
            // console.log(liTag);
            // console.log('...');
            //注意这里要新建一个li标签，直接使用appendChild会将原先页面中的元素移过来。
            choosedTags.appendChild(liTag);
        }
    }
    // console.log(body);
    // choosedTags.innerHTML = body;
}



/**
 * 添加弹出框的关闭按钮事件
 */
let close = document.getElementsByClassName("close")[0];
close.onclick = function() {
    createTags.style.display = "none";
    let oMask = document.getElementById("oMask");
    oMask.style.display = "none";
    //将弹出框中的li标签同步到原先的页面
    let liTags = createTags.getElementsByTagName('li');
    let ulTags = tags.getElementsByTagName('ul')[0];
    ulTags.innerHTML = "";
    for (let i = 0; i < liTags.length; i++) {
        if (liTags[i].style.display == "block") {
            let liTag = document.createElement('li');
            liTag.innerHTML = liTags[i].innerHTML;
            liTag.style.display = "block";
            ulTags.appendChild(liTag);
            liTag.getElementsByTagName('a')[0].onclick =
                function() {
                    liTag.style.display = "none";
                }
        }
    }
}


/**
 * 文章发布按钮事件
 */
let publish = document.getElementsByClassName("publish")[0];
publish.onclick = function() {
    let title = document.getElementById("title");
    let tag = "Vue.js,javascript,java";
    let abstract = document.getElementById("abstract");
    let rowText = document.getElementById("rowText");
    let markedText = document.getElementById("markedText");

    let data = {
            title: title.value,
            tags: tag,
            abstract: abstract.value,
            rowtext: rowText.value,
            markedtext: markedText.innerHTML
        }
        //数据已经取得，接下来就是提交到服务器
    myApi.publishArticle(data, function(err, data) {
        if (err) {
            console.log(err)
        }
        console.log(data);
    })
}