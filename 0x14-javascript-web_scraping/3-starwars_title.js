#!/usr/bin/node
const args = process.argv;
const id = args[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  console.log(JSON.parse(body).title);
});
