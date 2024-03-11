#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const obj = JSON.parse(body);
  let countChar = 0;
  for (let i = 0; i < obj.results.length; i++) {
    for (let j = 0; j < obj.results[i].characters.length; j++) {
      if (obj.results[i].characters[j].endsWith('/18/')) {
        countChar++;
      }
    }
  }
  console.log(countChar);
});
