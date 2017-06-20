import media
import fresh_tomatoes

justice_league = media.Movie("Justice league",
                             "Starring Gal Gadot, Amy Adams, Ben Affleck",
                             "http://www.dccomics.com/sites/default/files/video/JLTrailer1_thumb_58d978dbb1ca41.17031807.jpg",
                             "https://www.youtube.com/watch?v=OiAmnKUaNmc")
 
#print(justice_league.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://theredlist.com/media/database/films/cinema/2000/avatar-/027-avatar-theredlist.jpg",
                     "https://www.youtube.com/watch?v=_i2RCBa3l-g")

#print(avatar.storyline)
#avatar.show_trailer()

battleship = media.Movie("Battleship",
                     "when Aliens come to earth",
                     "https://upload.wikimedia.org/wikipedia/commons/8/83/USS_Texas2.jpg",
                     "https://www.youtube.com/watch?v=8NNQqHsIc-4")



Anabelle2 = media.Movie("Annabelle2",
                     "Scarry horror movie",
                     "https://pbs.twimg.com/media/C8NwOLXUAAU96Em.jpg",
                     "https://www.youtube.com/watch?v=yd27oUBi3-I")



Inception = media.Movie("Inception",
                        "A movie of dreams",
                        "http://www.breaknenter.org/wp-content/uploads/2011/09/inception_movie_poster_small.png",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")


Interstellar = media.Movie("Interstellar",
                           "Academy award winner",
                           "https://bfox.files.wordpress.com/2014/11/interstellar-movie.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

movies = [justice_league, avatar, battleship, Anabelle2, Inception, Interstellar]
fresh_tomatoes.open_movies_page(movies)
