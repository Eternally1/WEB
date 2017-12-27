// const config = require("./config.json");
import config from './config.json';

//导入样式
import styles from "./Greeter.css";
module.exports = function(){
	let greet = document.createElement("div");
	//让styles中名字为root的样式应用到greet这个div中去。
	greet.className = styles.root
	greet.textContent = config.greetText;
	return greet;
};