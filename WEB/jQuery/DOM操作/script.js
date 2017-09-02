//1、查找元素节点
var $li = $("#id1 ul li:eq(1)");//获取ul里的第二个li
console.log($li.text());
//2、查找属性节点
//先是查找到元素节点，然后通过attr()方法来获取它的属性
var $p = $("#id1 p");
console.log($p.attr("title"));

var p = document.getElementById("id1");
var $p = $(p);
