#!/usr/bin/node
// I love C
const argv = process.argv.slice(2);
const number = parseInt(argv[0], 10);
function factorial (a) {
  if (a === 0) {
    return (1);
  } else {
    const b = a - 1;
    return (a * factorial(b));
  }
}
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
