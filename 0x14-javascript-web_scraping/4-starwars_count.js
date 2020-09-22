#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  let newdict = {};
  newdict = JSON.parse(body).results;
  let i;
  let count = 0;
  for (i = 0; i < newdict.length; i++) {
    let j;
    for (j = 0; j < newdict[i].characters.length; j++) {
      if (newdict[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
