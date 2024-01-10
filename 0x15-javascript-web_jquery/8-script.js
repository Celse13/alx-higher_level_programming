$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", (content) => {
  const moviesList = $('#list_movies');
  content.results.forEach((movie) => {
    moviesList.append($('<li>').text(movie.title));
  });
});
