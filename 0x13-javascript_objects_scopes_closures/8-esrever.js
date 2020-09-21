#!/usr/bin/node
exports.esrever = function (list) {
  const lista = list.sort(function (a, b) { return (a - b); });
  let i;
  const arr = [];
  for (i = 0; i < lista.length; i++) {
    arr.unshift(lista[i]);
  }
  return arr;
};
