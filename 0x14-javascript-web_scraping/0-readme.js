#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf-8', function (err, res) {
  if (err) {
    return console.error(err);
  }
  console.log(res);
});
