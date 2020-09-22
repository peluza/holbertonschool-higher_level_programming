#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    return console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
