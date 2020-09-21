#!/usr/bin/node
const dict = require('./101-data.js').dict;
console.log(dict);
const newdict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newdict[value] === undefined) {
    newdict[value] = [key];
  } else {
    newdict[value].push(key);
  }
}
console.log(newdict);
