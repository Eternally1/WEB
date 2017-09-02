var htmlWebpackPlugin = require('html-webpack-plugin');
var webpack = require('webpack');
//另一种使用绝对路径的方式
var path = require('path');

module.exports = {
	//在配置里面有一个上下文context，默认值就是根目录
	entry:'./src/app.js',
	output:{
		path:__dirname+'/dist',
		filename:'js/[name].bundle.js',
	},
	module:{
		rules:[
		//处理js文件，采用babel
		{
			test:/\.js$/,
			loader:'babel-loader',
			//这个文件夹一般是一些打包之后的文件，所以不用来
			//再次使用babel-loader.使用exclude来排除babel-loader的加载对象
			exclude:__dirname+'/node_modules',
			// include:__dirname+'/src/',
			include:path.resolve(__dirname,"src"),
			query:{
				presets:['latest']
			}
		},{
			test:/\.css$/,
			use:[
			'style-loader','css-loader?importLoaders=1','postcss-loader' 
			] 
		},{
			test:/\.less$/,
			use:[
			'style-loader','css-loader','postcss-loader','less-loader'
			]
		},{
			test:/\.html$/,
			loader:'html-loader'
		},{
			test: /\.(jpe?g|png|gif|svg)$/i,
			use: [
			'url-loader?limit=10000&name=assets/[name]-[hash:5].[ext]',
			'img-loader'
			]
			
		}]
	},
	plugins:[
		//进行初始化
		new htmlWebpackPlugin({
			filename:'index.html',
			template:'index.html',
			inject:'body'
		})
		]
	}