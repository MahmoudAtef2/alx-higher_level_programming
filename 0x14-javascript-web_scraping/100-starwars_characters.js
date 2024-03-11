#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const obj = JSON.parse(body);
  for (let i = 0; i < obj.characters.length; i++) {
    request.get(obj.characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const peopleObject = JSON.parse(body);
      console.log(peopleObject.name);
    });
  }
});
