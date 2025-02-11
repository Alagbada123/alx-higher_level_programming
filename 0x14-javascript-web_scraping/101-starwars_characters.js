#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = `${baseUrl}${movieId}`;

request(fullUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Create an array of promises for character requests
  const characterPromises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body).name);
      });
    });
  });

  // Resolve all character requests and maintain order
  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((err) => console.error(err));
});
