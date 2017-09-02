<template>
    <div class="searchBar">
        <input type="text" v-model="searchString" placeholder="Search your search terms" />
        <ul>
            <li v-for="item in newArticles">
                <a v-bind:href="item.url"><img v-bind:src="item.image" /></a>
                <p v-text="item.title"></p>
            </li>
        </ul>
    </div>

</template>
<script>   
    // 即时搜索
export default{
    data () {
        return{
            articles: [
            {
                "title": "What You Need To Know About CSS Variables",
                "url": "http://tutorialzine.com/2016/03/what-you-need-to-know-about-css-variables/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2016/03/css-variables-100x100.jpg"
            },
            {
                "title": "Freebie: 4 Great Looking Pricing Tables",
                "url": "http://tutorialzine.com/2016/02/freebie-4-great-looking-pricing-tables/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2016/02/great-looking-pricing-tables-100x100.jpg"
            },
            {
                "title": "20 Interesting JavaScript and CSS Libraries for February 2016",
                "url": "http://tutorialzine.com/2016/02/20-interesting-javascript-and-css-libraries-for-february-2016/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2016/02/interesting-resources-february-100x100.jpg"
            },
            {
                "title": "Quick Tip: The Easiest Way To Make Responsive Headers",
                "url": "http://tutorialzine.com/2016/02/quick-tip-easiest-way-to-make-responsive-headers/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2016/02/quick-tip-responsive-headers-100x100.png"
            },
            {
                "title": "Learn SQL In 20 Minutes",
                "url": "http://tutorialzine.com/2016/01/learn-sql-in-20-minutes/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2016/01/learn-sql-20-minutes-100x100.png"
            },
            {
                "title": "Creating Your First Desktop App With HTML, JS and Electron",
                "url": "http://tutorialzine.com/2015/12/creating-your-first-desktop-app-with-html-js-and-electron/",
                "image": "http://cdn.tutorialzine.com/wp-content/uploads/2015/12/creating-your-first-desktop-app-with-electron-100x100.png"
            }],
            searchString:""
        }
    },
    computed:{
        newArticles:function(){
            var result = [];
            if(!this.searchString){
                return this.articles;
            }
            this.searchString = this.searchString.trim().toLowerCase();
            var _this = this;
            result = this.articles.filter(function(item){
                if(item.title.toLowerCase().indexOf(_this.searchString)!==-1){
                    return item;
                }else{
                    //这里当搜索的结果不存在的时候，可以显示一个图片404  和一个标题not found result.
                    // return //
                }
            });
            return result;
        }
    }
}
</script>

<style>
    .searchBar input {
        width: 500px;
        height: 36px;
        border: 1px solid #ccc;
        border-radius: 5px;
        color: #000;
        font-family: "Comic Sans MS", sans-serief;
        font-size: 15px;
        background: transition 0.3s ease-in-out;
    }
    
    .searchBar input:focus {
        outline: none;
        border-color: #9ecaed;
        background-color: #eee;
        text-indent:20px;
    }
    
    .searchBar ul {
        width: 500px;
        margin: 0 auto;
        padding-left: 10px;
    }
    
    .searchBar ul li {
        list-style: none;
        width: 100%;
        text-align: center;
        text-align: left;
        margin-top: 10px;
        border-bottom: 1px solid #ccc;
        padding-bottom: 10px;
    }
    
    .searchBar ul li a {
        display: inline-block;
        width: 70px;
        height: 70px;
    }
    
    .searchBar ul li a img {
        width: 100%;
        height: 100%;
        /*这个是用在图片上的。*/
        vertical-align: middle;
    }
    
    .searchBar ul li p {
        font-family:"Comic Sans MS",sans-serief;
        /*height:50px;*/
        margin-top: 0px;
        margin-bottom:0px;
        /*margin-top:*/
        margin-left: 20px;
        display: inline-block;
        width:300px;
    }
</style>