#!/usr/bin/node
const request = require('request');
const endpoint = process.argv[2];
const obj = {};
let testId = 0;

request(endpoint, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).forEach(todo => {
    if (todo.completed === true && testId === todo.userId) {
      if (!obj[todo.userId]) obj[todo.userId] = 0;
      obj[todo.userId] += 1;
    } else if (todo.completed) obj[todo.userId] = 1;
    testId = todo.userId;
  });
  console.log(obj);
});
