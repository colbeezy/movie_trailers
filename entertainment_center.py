import fresh_tomatoes
import media

# The movies that will appear
catch_me_if_you_can = media.Movie ("Catch Me If You Can", "http://www.gstatic.com/tv/thumb/movieposters/31064/p31064_p_v8_af.jpg", "https://www.youtube.com/watch?v=xas1UyTiVUw")
avatar = media.Movie ("Avatar", "https://www.movieposter.com/posters/archive/main/98/MPW-49246", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
ace_ventura = media.Movie ("Ace Ventura: Pet Detective", "https://images-na.ssl-images-amazon.com/images/I/51W7nq7YztL._SY300_.jpg", "https://www.youtube.com/watch?v=QzxDlS6QY1s")
planet_of_the_apes = media.Movie ("War for the Planet of the Apes", "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg", "https://www.youtube.com/watch?v=37qT8X9fi14")
lord_of_the_rings = media.Movie ("Lord of the Rings", "http://www.movieartarena.com/imgs/lotr1final.jpg", "https://www.youtube.com/watch?v=Pki6jbSbXIY")
the_big_sick = media.Movie ("The Big Sick", "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg", "https://www.youtube.com/watch?v=PJmpSMRQhhs")

# List of the movies
movies = [catch_me_if_you_can, avatar, ace_ventura, planet_of_the_apes, lord_of_the_rings, the_big_sick]

# This launches the program
fresh_tomatoes.open_movies_page (movies)
