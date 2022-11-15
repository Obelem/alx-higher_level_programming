#!/usr/bin/node
const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(endpoint, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  });
});
