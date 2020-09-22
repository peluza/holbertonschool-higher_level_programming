#!/usr/bin/node
/*  script that concats 2 files */
const args = process.argv;
const file1 = args[2];
const fs = require('fs');
let str1;
fs.readFile(file1, function (err, res) {
  if (err) {
    return console.error(err);
  }
  str1 = res.toString();
  console.log(str1);
});
