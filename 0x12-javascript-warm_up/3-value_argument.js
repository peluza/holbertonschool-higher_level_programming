#!/usr/bin/node
// Value of my argument
const argv = process.argv.slice(2);
if (!argv[0]) {
  console.log('No argument');
} else {
  console.log(argv[0]);
}
