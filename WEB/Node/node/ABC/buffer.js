//创建长度为256字节的buffer实例
var buf = new Buffer(12);
var buf1 = new Buffer(20);

//buf的写入helloworld
var len = buf.write('hello world');
//buf1写入字节 “你好世界”
var len1 = buf1.write('你好，世界');
console.log("buf写入的字节数"+len);
//一个utf8编码的字体占三个字节。
console.log("buf1写入的字节数"+len1)//15
//从缓冲区读取数据，
// console.log(buf.toString('ascii',0,5));
console.log(buf.toString('utf-8',0,5));

//合并buf和buf1
var newBuf = Buffer.concat([buf,buf1], [33]);
//读取合并之后的数据
//因为有中文，所以采用ascii的时候会乱码
// console.log(newBuf.toString("ascii"));
console.log(newBuf.toString("utf8"));
var jsonBuf = newBuf.toJSON();
// console.log(jsonBuf);
// 
// 比较这两个buffer
var result = buf.compare(buf1);
console.log("buf和buf1的比较结果是"+result);

//缓冲区拷贝
var buf2 = new Buffer(10);
buf.copy(buf2,3,2,10);
console.log(buf2.toString('ascii'));