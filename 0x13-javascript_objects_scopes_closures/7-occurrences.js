#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(current => {
    if (current === searchElement) { counter++; }
  });
  return counter;
};
