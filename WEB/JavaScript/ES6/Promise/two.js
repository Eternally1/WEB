function loadImageAsync(url) {
    return new Promise(function(resolve, rejected) {
        var img = new Image(); //Image isn't defined.
        // var img = document.createElement('img');
        img.onload = function() {
            resolve(img);
        }
        img.onerror = function() {
            rejected('can not load image from ' + url);
        }
        img.src = url;
    });
}
// loadImageAsync('./lib/2.jpg').then(function(data) {
//     console.log(data);
// }, function(error) {
//     console.log(error);
// })

/**
 * 一种和上面注释等价的写法，但是要更好
 */
loadImageAsync('./lib/2.jpg').then(function(data) {
    console.log(data);
}).catch(function(err) {
    console.log(err);
})