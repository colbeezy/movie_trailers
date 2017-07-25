import fresh_tomatoes
import media

# Catch Me If You Can movie: title, poster, trailer
catch_me_if_you_can = media.Movie(
    "Catch Me If You Can",
    "http://www.gstatic.com/tv/thumb/movieposters/31064/p31064_p_v8_af.jpg",    # NOQA
    "https://www.youtube.com/watch?v=xas1UyTiVUw"   # NOQA
    )

# Avatar movie: title, poster, trailer
avatar = media.Movie(
    "Avatar",
    "https://www.movieposter.com/posters/archive/main/98/MPW-49246",    # NOQA
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"   # NOQA
    )

# Ace Ventura movie: title, poster, trailer
ace_ventura = media.Movie(
    "Ace Ventura: Pet Detective",
    "https://images-na.ssl-images-amazon.com/images/I/51W7nq7YztL._SY300_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=QzxDlS6QY1s"   # NOQA
    )

# Planet of the Apes movie: title, poster, trailer
planet_of_the_apes = media.Movie(
    "War for the Planet of the Apes",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=37qT8X9fi14"   # NOQA
    )

# LOTR movie: title, poster, trailer
lord_of_the_rings = media.Movie(
    "Lord of the Rings", "http://www.movieartarena.com/imgs/lotr1final.jpg",    # NOQA
    "https://www.youtube.com/watch?v=Pki6jbSbXIY"   # NOQA
    )

# The Big Sick movie: title, poster, trailer
the_big_sick = media.Movie(
    "The Big Sick",
    "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PJmpSMRQhhs"   # NOQA
    )

# List the movies that will be passed to media.py
movies = [
    catch_me_if_you_can,
    avatar, ace_ventura,
    planet_of_the_apes,
    lord_of_the_rings,
    the_big_sick
    ]

# Launch the HTML file in a web browser via the fresh_tomates.py file
fresh_tomatoes.open_movies_page(movies)
