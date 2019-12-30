import media
import prompt

Parasite = media.Movie("Parasite",
                        "Bong Joon Ho",
                        "All unemployed, Ki-taek and his family take peculiar interest in the wealthy and glamorous Parks, as they ingratiate themselves into their lives and get entangled in an unexpected incident.",
                        "file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/para.jpg",
                        "https://www.imdb.com/video/imdb/vi1015463705?playlistId=tt6751668&ref_=tt_ov_vi"
)

Irishman = media.Movie('The Irishman',
                    'Martin Scorsese',
                    'A mob hitman recalls his possible involvement with the slaying of Jimmy Hoffa.',
                    'file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/irish.jpg',
                    'https://www.imdb.com/video/imdb/vi2244525849?playlistId=tt1302006&ref_=tt_ov_vi'
)
# print(avatar.storyline)
Burning = media.Movie('Burning',
                    " Chang-dong Lee",
                    "Jong-su bumps into a girl who used to live in the same neighborhood, who asks him to look after her cat while she's on a trip to Africa. When back, she introduces Ben, a mysterious guy she met there, who confesses his secret hobby.",
                    'file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/burning.jpg',
                   'https://www.imdb.com/video/imdb/vi1202305817?playlistId=tt7282468&ref_=tt_ov_vi'
)

movies = [Parasite,Irishman, Burning]
prompt.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)