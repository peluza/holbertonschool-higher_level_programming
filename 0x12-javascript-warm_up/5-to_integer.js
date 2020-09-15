#!/usr/bin/node
// Value of my argument
const argv = process.argv.slice(2);
const number = parseInt(argv[0], 10);
if (!number) {
  console.log('Not a number');
} else {
  console.log("My number: " + number);
}
