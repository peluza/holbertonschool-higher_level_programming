#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count = count + 1;
    }
  }
  return count;
};
