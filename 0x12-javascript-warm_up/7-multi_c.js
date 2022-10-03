#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  let count = Math.round(process.argv[2]);
  while (count > 0) { console.log('C is fun'); count--; }
}
