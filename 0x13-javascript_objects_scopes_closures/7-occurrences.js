#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0; let c = 0;
  while (i < list.length) {
    if (searchElement === list[i]) c++;
    i++;
  }
  return c;
};
