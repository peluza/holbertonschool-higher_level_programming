#!/usr/bin/node
const args = process.argv;
const url = args[2];
const file = args[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
