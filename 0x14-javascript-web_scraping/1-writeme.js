#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

fs.writeFile(file, text, 'utf8', (err) => {
  if (err) throw err;
});
