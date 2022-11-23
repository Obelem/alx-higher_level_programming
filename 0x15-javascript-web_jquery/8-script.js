const endpoint = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(endpoint, data => {
  data.results.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
