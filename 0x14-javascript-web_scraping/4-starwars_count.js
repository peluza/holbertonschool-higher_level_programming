#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
const characterID = '18';
let newdict;
let i;
let count = 0;
let j;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  newdict = JSON.parse(body).results;
  for (i = 0; i < newdict.length; i++) {
    for (j = 0; j < newdict[i].characters.length; j++) {
      if (newdict[i].characters[j].includes(characterID)) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
