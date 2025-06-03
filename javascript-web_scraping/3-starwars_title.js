#!/usr/bin/node
const req = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
req.get(url, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(res.body).title);
  }
});
