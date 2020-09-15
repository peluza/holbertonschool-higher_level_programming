#!/usr/bin/node
// I love C
const argv = process.argv.slice(2);
const number = parseInt(argv[0], 10);
if (!number) {
  console.log('Missing size');
} else {
  let i;
  const x = 'x';
  for (i = 0; i < number; i++) {
    console.log(x.repeat(number));
  }
}
