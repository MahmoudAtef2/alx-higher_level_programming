const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  for (let i = 0; i < data.results.length; i++) {
    $('#list_movies').append(data.results[i].title);
  }
}, 'json');
