function* fibonacci() {
    let [prev, curr] = [0, 1];
    for (;;) {
        [prev, curr] = [curr, prev + curr];
        yield curr;
    }
}

for (let n of fibonacci()) {
    //n接收的就是yield后面的值。
    /**
     * 每一次执行到yield之后就会暂停然后退出fibonacci函数
     * 转到执行下面的判断语句(n>10?),之后再次循环fibonacci()。
     */
    if (n > 10) {
        break;
    }
    console.log(n);
}