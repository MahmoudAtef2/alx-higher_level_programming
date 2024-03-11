#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const bodyJson = JSON.parse(body);
  const reptUserId = [];
  let index = 0;
  for (let i = 0; i < bodyJson.length; i++) {
    if (bodyJson[i].completed === true) {
      reptUserId[index] = bodyJson[i].userId;
      index++;
    }
  }
  const countMap = {};
  reptUserId.forEach(number => {
    countMap[number] = (countMap[number] || 0) + 1;
  });
  console.log(countMap);
});
