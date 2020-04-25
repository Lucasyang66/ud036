import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                                            "A story of a boy and his toys that come to life",
                                            "https://i.redd.it/t7iz1ymdafg31.png",
                                            "https://www.youtube.com/watch?v=wmiIUN-7qhE")

the_emoji_movie=movie.Movie("The Emoji Movie",
                                                         "Hidden inside a smartphone, the bustling city of Textopolis is home to all emojis. Each emoji has only one facial expression, except for Gene, an exuberant emoji with multiple expressions. Determined to become normal like the other emojis, Gene enlists the help of his best friend Hi-5 and a notorious code breaker called Jailbreak. During their travels through the other apps, the three emojis discover a great danger that could threaten their phone's very existence",
                                                         "https://images-na.ssl-images-amazon.com/images/I/716TqWqWQzL._AC_SY679_.jpg",
                                                         "https://www.youtube.com/watch?v=r8pJt4dK_s4")

the_angry_brids_movie2=movie.Movie("The Angry Brids Movie 2",
                                                                     "Red, Chuck, Bomb and the rest of their feathered friends are surprised when a green pig suggests that they put aside their differences and unite to fight a common threat. Aggressive birds from an island covered in ice are planning to use an elaborate weapon to destroy the fowl and swine way of life. After picking their best and brightest, the birds and pigs come up with a scheme to infiltrate the island, deactivate the device and return to their respective paradises intact",
                                                                     "https://mrlib.org/wp-content/uploads/2020/01/THE_ANGRY_BIRDS_MOVIE_2_poster-scaled.jpg",
                                                                     "https://www.youtube.com/watch?v=RSKQ-lVsMdg")

movies=[toy_story ,the_emoji_movie,the_angry_brids_movie2]
fresh_tomatoes.open_movies_page(movies)
