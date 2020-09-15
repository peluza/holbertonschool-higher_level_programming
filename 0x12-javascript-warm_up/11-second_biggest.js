#!/usr/bin/node
// Second biggest!
const argv = process.argv.slice(2);
const number1 = parseInt(argv[0], 10);
const number2 = parseInt(argv[1], 10);
if (!number1) {
  console.log(0);
} else if (number1 === 1 && !number2) {
  console.log(0);
} else {
  argv.sort(function (a, b) { return (a - b); });
  const len = argv.length;
  const result = len - 2;
  console.log(parseInt(argv[result], 10));
}
