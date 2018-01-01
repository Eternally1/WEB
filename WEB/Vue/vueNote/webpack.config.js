module.exports = {
	entry:__dirname+"/src/main.js",
	output:{
		path:__dirname+"/dist",
		filename:"build.js"
	},
	module:{
		rules:[
			{
				test:/\.vue$/,
				use:{
					loader:"vue-loader"
				},
				// exclude:/node_modules/
			},
			{
				test:/(\.js|\.jsx)$/,
				exclude:/node_modules/,
				use:{
					loader:"babel-loader"
				},
				
			},
			{
				test:/\.css$/,
				use:[
					{
						loader:"style-loader"
					},
					{
						loader:"css-loader"
					}
				],
				// exclude:/node_modules/
			}
		]
	},
	resolve:{
		alias:{
			'vue':'vue/dist/vue.js'
		}
	}
}