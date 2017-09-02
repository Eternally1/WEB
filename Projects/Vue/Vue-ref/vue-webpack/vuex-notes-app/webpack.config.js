module.exports = {
	entry:'./main.js',
	output:{
		path:__dirname,
		filename:'build.js'
	},
	module:{
		loaders:[
		{
			test:/\.vue$/,
			loader:'vue'
		},{
			test:/\.js$/,
			loader:'babel',
			exclude:/node_modules/
		}]
	},//1.0
	//2.0
	// module:{
	// 	rules:[
	// 	{
	// 		test:/\.vue$/,
	// 		use:['vue-loader']
	// 	},{
	// 		test:/\.js$/,
	// 		use:['babel-loader']
	// 	}]
	// }
	babel:{
		presets:['es2015'],
		plugins:['transform-runtime']
	}
}