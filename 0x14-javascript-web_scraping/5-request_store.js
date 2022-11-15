#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const endpoint = process.argv[2];
const file = process.argv[3];

request(endpoint, (err, res, body) => {
  if (err) throw err;

  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
