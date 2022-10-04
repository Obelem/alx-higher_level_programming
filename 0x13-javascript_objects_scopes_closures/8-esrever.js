#!/usr/bin/node
exports.esrever = function (list) {
  const revArray = [];
  list.forEach(element => { revArray.unshift(element); });
  return revArray;
};
