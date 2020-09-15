#!/usr/bin/node
// I love C
const argv = process.argv.slice(2);
const number = parseInt(argv[0], 10);
if (!number) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
