#!/usr/bin/node
/*  script that concats 2 files */
const args = process.argv;
const file = args[2];
const str1 = args[3];
const fs = require('fs');
fs.writeFile(file, str1, 'utf-8', function (err) {
  if (err) {
    return console.error(err);
  }
});
