#!/usr/bin/node
const sortedArray = process.argv.slice(2).sort((a, b) => { return a - b; });
const secondToLast = sortedArray[sortedArray.length - 2];
console.log(isNaN(secondToLast) ? 0 : secondToLast);
