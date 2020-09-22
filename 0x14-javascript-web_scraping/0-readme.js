#!/usr/bin/node
/*  script that concats 2 files */
const fs = require('fs');
const args = process.argv.slice(2, 3);
fs.readFile(args[0], 'utf-8', function (err, res) {
  if (err) {
    return console.log(err);
  }
  console.log(res);
});
