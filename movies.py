import media
import prompt

Parasite = media.Movie("Parasite",
                        "Bong Joon Ho",
                        "All unemployed, Ki-taek and his family take peculiar interest in the wealthy and glamorous Parks, as they ingratiate themselves into their lives and get entangled in an unexpected incident.",
                        "file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/para.jpg",
                        "https://www.youtube.com/watch?v=isOGD_7hNIY"
)

Irishman = media.Movie('The Irishman',
                    'Martin Scorsese',
                    'A mob hitman recalls his possible involvement with the slaying of Jimmy Hoffa.',
                    'file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/irish.jpg',
                    'https://www.youtube.com/watch?v=RS3aHkkfuEI'
)
# print(avatar.storyline)
Burning = media.Movie('Burning',
                    " Chang-dong Lee",
                    "Jong-su bumps into a girl who used to live in the same neighborhood, who asks him to look after her cat while she's on a trip to Africa. When back, she introduces Ben, a mysterious guy she met there, who confesses his secret hobby.",
                    'file:///home/bideen/Desktop/Web%20Development%20-%20Udacity/Movies/img/burning.jpg',
                   'https://www.youtube.com/watch?v=wi6Kw7V8gXk'
)

movies = [Parasite,Irishman, Burning]
prompt.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)