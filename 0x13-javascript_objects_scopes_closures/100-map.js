#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const map1 = list.map((value, index) => { return value * index; });
console.log(map1);
