var htmlWebpackPlugin = require('html-webpack-plugin');
var webpack = require('webpack');
module.exports = {
	//在配置里面有一个上下文context，默认值就是根目录
	entry: {
		//这是是用来处理多页面应用。
		main: "./src/script/main.js",
		a: "./src/script/a.js",
		b: "./src/script/b.js",
		c: "./src/script/c.js"
	},
	output: {
		path: __dirname + '/dist',
		filename: 'js/[name]-[chunkhash].js',
		//这个值需要在上线的时候使用
		publicPath: 'http://cdn.com/'
	},
	plugins: [
		//进行初始化
		new htmlWebpackPlugin({
			//根目录下面的index.html。这里路径就是可以直接
			//这样书写的，因为默认的上下文就是根目录
			template: 'index.html',
			//也可以指定生成的文件的名字
			filename: 'index.html',
			//将script文件注射到head标签中
			inject: false,
			//这里的参数可以传递到根目录下面的index.html文件
			//也就是所谓了参数传递。
			title: 'Webpack is good',
			//也可以传递参数。
			date: new Date(),
			minify: {
				//对生成的html文件进行压缩（上线的话）
				removeComments: true,//删除注释
				collapseWhitespace: true//删除空格
			}
		}),
		new htmlWebpackPlugin({
			filename: 'a.html',
			template: 'index.html',
			title: 'this is a.html',
			inject: false,
			excludeChunks: ['c', 'b']
		}),
		new htmlWebpackPlugin({
			filename: 'b.html',
			template: 'index.html',
			title: 'this is b.html',
			inject: false,
			excludeChunks: ['c']
		}),
		new htmlWebpackPlugin({
			filename: 'c.html',
			template: 'index.html',
			title: 'this is c.html',
			inject: false,
			chunks: ['c', 'main']
		})
	]
}