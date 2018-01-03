const path = require("path");

function resolve(dir) {
    // console.log(path.join(__dirname,'..',dir));
    return path.join(__dirname, '..', dir);
}

module.exports = {
	// 添加source map
	devtool:'cheap-source-map',
    entry: __dirname + "/src/main.js",
    output: {
        path: __dirname + "/dist",
        filename: "build.js"
    },
     resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            '@': resolve('src')
        }
    },
    module: {
        rules: [{
                test: /\.vue$/,
                use: {
                    loader: "vue-loader"
                },
                exclude: /node_modules/
            },
            {
                test: /(\.js|\.jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                },

            },
            {
                test: /\.css$/,
                use: [{
                        loader: "style-loader"
                    },
                    {
                        loader: "css-loader"
                    }
                ],
                exclude: /node_modules/
            }
        ]
    }
}