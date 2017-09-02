/**
 * 用于存储的模块
 * 有两个功能，一个是fetch，一个是save
 */
const STORAGE_KEY = "todos-vuejs";//定义一个常量
export default{
   //相当于module.export，也就是导出去
   //这里导出去的是两个方法
   fetch (){
     //JSON.parse()是转换成JSON对象形式
      return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
   },
   save:function(items){
     //存储的时候是以字符串的形式存储的。
      window.localStorage.setItem(STORAGE_KEY,JSON.stringify(items));
   }
}