#!/usr/bin/node
// Second biggest!
const argv = process.argv.slice(2);
const number = parseInt(argv[0], 10);
if (!number) {
  console.log(0);
} else {
  argv.sort();
  const len = argv.length;
  const result = len - 2;
  console.log(parseInt(argv[result], 10));
}
