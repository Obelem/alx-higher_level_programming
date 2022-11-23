const endpoint = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(endpoint, (actor) => {
  $('DIV#character').text(actor.name);
});
