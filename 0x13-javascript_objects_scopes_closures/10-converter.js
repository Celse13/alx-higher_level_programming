#!/usr/bin/node
exports.converter = function (base) {
  return function (x) {
    return parseInt(x, 10).toString(base);
  };
};
