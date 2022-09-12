#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const axios = require('axios');
const episodio = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/`;

axios.get(url)
  .then(response => {
    const peliculas = response.data.results;
    const actores = peliculas[episodio - 1].characters
    for (let i = 0; i < actores.length; i++) {
      axios.get(actores[i])
        .then(actors => {
          console.log(actors.data.name);
        });
   }})
  .catch(error => {
    console.log(error.response.status);
  });
