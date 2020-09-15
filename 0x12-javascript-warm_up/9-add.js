#!/usr/bin/node
// I love C
const argv = process.argv.slice(2);
const a = parseInt(argv[0], 10);
const b = parseInt(argv[1], 10);
function add (a, b) {
  console.log(a + b);
}
add(a, b);
