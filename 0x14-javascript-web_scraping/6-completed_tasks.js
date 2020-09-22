#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
const completedtask = true;
let newdict;
let i;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  newdict = JSON.parse(body);
  const complete = {};
  for (i = 0; i < newdict.length; i++) {
    if (newdict[i].completed === completedtask) {
      if (complete[newdict[i].userId]) {
        complete[newdict[i].userId] = complete[newdict[i].userId] + 1;
      } else {
        complete[newdict[i].userId] = 1;
      }
    }
  }
  console.log(complete);
});
