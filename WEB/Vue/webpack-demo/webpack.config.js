module.exports = {
	/**
	 * __dirname 是node.js中的一个全局变量，指向当前执行脚本所在目录
	 * source map  是一个有助于调试的工具
	 */
	devtool:"eval-source-map",
	entry:__dirname+"/app/main.js",//入口文件
	output:{
		path:__dirname+"/public",//打包后文件存放地址
		filename:"bundle.js"  //打包后输出文件的文件名
	},

	/**
	 * 配置本地服务器，在代码改变时，自动刷新显示修改之后的结果
	 */
	devServer:{
		contentBase:"./public", //本地服务器所加载的页面所在目录
		historyApiFallback:true, //不跳转
		inline:true  //实时刷新
	},

	/**
	 * 配置babel
	 * @type {Object}
	 */
	module:{
		rules:[
			{
				test:/(\.jsx|\.js)$/,
				use:{
					loader:"babel-loader"
				},
				//屏蔽不需要处理的文件夹
				exclude:/node_modules/
			},

			{
				test:/\.css$/,
				use:[
				//同一个文件引入多个loader的方法
					{
						loader:"style-loader"
					},{
						loader:"css-loader",
						options:{
							modules:true,
							localIdentName:'[name]__[local]--[hash:base64:5]'//指定CSS的类名格式
						}
					}
				]
			}
		]
	},
}