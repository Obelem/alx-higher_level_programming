#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;

request(endpoint, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
