#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
let newdict;
let i;
let count = 0;
let j;
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  newdict = JSON.parse(body).results;
  for (i = 0; i < newdict.length; i++) {
    for (j = 0; j < newdict[i].characters.length; j++) {
      if (newdict[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
