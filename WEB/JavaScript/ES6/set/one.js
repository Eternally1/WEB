const set = new Set();

// [2, 1, 3, 4, 1, 2, 3].forEach(function(v) {
//     set.add(v);
// })

[2, 1, 3, 4, 1, 2, 3].forEach(v => { set.add(v) });

for (let i of set) {
    console.log(i);
}