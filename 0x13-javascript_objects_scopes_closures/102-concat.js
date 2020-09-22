#!/usr/bin/node
/*  script that concats 2 files */
const args = process.argv;
const file1 = args[2];
const file2 = args[3];
const newfile = args[4];
const fs = require('fs');
let str1;
let str2;
fs.readFile(file1, function (err, res) {
  if (err) {
    return console.error(err);
  }
  str1 = res.toString();
  fs.appendFile(newfile, str1, function (err) {
    if (err) throw err;
  });
});
fs.readFile(file2, function (err, res) {
  if (err) {
    return console.error(err);
  }
  str2 = res.toString();
  fs.appendFile(newfile, str2, function (err) {
    if (err) throw err;
  });
});
