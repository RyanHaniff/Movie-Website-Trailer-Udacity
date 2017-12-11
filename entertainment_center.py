from media import Movie
import fresh_tomatoes

# Instances of Movie class
the_shawshank_redemption = media.Movie(
  "The Shawshank Redemption",
  "https://images-na.ssl-images-amazon.com/images/I/51SPVi-1rXL._SY450_.jpg",
  "https://www.youtube.com/watch?v=6hB3S9bIaco")

iron_man = media.Movie(
  "Iron Man",
  "http://cdn.collider.com/wp-content/uploads/iron-man-poster.jpg",
  "https://www.youtube.com/watch?v=8hYlB38asDY")

the_pursuit_of_happyness = media.Movie(
  "The Pursuit Of Happyness",
  "https://fontmeme.com/images/The-Pursuit-of-Happyness-Poster.jpg",
  "https://www.youtube.com/watch?v=89Kq8SDyvfg")

rush = media.Movie(
  "Rush",
  "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/08/08aee6276db142f4b8ac98fb8ee0ed1b_500x735.jpg?t=1488638061",
  "https://www.youtube.com/watch?v=MQoUKepg0tA")

thor = media.Movie(
  "Thor",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
  "https://www.youtube.com/watch?v=JOddp-nlNvQ")

the_avengers = media.Movie(
  "The Avengers",
  "https://vignette.wikia.nocookie.net/marvelheroes/images/9/98/Avengers-movie-poster-1.jpg/revision/latest?cb=20170713041606",
  "https://www.youtube.com/watch?v=eOrNdBpGMv8")

movies = [
  the_shawshank_redemption,
  iron_man,
  the_pursuit_of_happyness,
  rush,
  thor,
  the_avengers
]

fresh_tomatoes.open_movies_page(movies)
