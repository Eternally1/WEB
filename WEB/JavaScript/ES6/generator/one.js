function* helloWorld() {
        console.log("这句执行是否需要调用next？") //答案是需要
        yield 'hello';
        yield 'world';
        return 'ending';
    }
    // const hw = helloWorld();
    // console.log(hw.next());
    // console.log(hw.next());
    //{ value: 'ending', done: true }
    //下面这个执行完了之后就是true了，到这里遍历已经结束，true代表的就是遍历已经结束的意思
    // console.log(hw.next());

/**
 * 通过next传递状态
 */
function* ticketGenetaror() {
    let receiveVal = yield "yes";
    console.log(receiveVal);
}
let ticket = ticketGenetaror();
console.log(ticket.next());
console.log(ticket.next("right"));
/**
 * 先是第一个next使得方法体中运行到yield返回结果，然后暂停
 * 再次调用第二个next的时候，输出传递进去的值，同时表名程序完成。
 */