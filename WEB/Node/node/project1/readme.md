---
layout:default
title:服务端客户端简单交互
---

1、首先运行index.js,之后再次打开一个新的窗口，运行客户端client.js文件，就可以看到服务器端返回的string格式的数据
		首先是因为res.write()函数的参数第一个数值一定要是字符串，因此这里采用了JSON.stringify()方法将JSON格式的数据转换成字符串，然后返回给客户端。客户端可以在通过JSON.parse()来转换成JSON格式的数据。

