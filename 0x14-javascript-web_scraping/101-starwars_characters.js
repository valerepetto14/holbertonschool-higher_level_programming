#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const axios = require('axios');
const episodio = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodio}`;

// axios.get(url)
//   .then(response => {
//     const actores = response.data.characters;
//     for (let i of actores) {
//       axios.get(i)
//         .then(actors => {
//           console.log(actors.data.name);
//         })
//         .catch(err => {
//             console.log(err)
//         })
//    }})
//   .catch(error => {
//     console.log(error.response.status);
//   });

async function actores () {
  try {
    const response = await axios.get(url);
    const actores = response.data.characters;
    for (const i of actores) {
      const actor = await axios.get(i);
      console.log(actor.data.name);
    }
  } catch (error) {
    console.log(error);
  }
}

actores();
