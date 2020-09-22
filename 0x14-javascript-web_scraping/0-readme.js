#!/usr/bin/node
/*  script that concats 2 files */
const args = process.argv;
const file1 = args[2];
const fs = require('fs');
fs.readFile(file1, 'utf-8', function (err, res) {
  if (err) {
    return console.error(err);
  }
  console.log(res);
});
