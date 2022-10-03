#!/usr/bin/node

if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const count = Math.round(process.argv[2]);
  for (let rows = 0; rows < count; rows++) {
    let row = '';
    for (let col = 0; col < count; col++) row += 'X';
    console.log(row);
  }
}
