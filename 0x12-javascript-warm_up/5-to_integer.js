#!/usr/bin/node

console.log(parseInt(process.argv[2]) ? 'My number: ' + Math.round(process.argv[2]) : 'Not a number');
