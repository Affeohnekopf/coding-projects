from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")

# with open("filme.txt", "w") as file:
#     file.write("Your text goes here")

yc_web_page = request.text
soup = BeautifulSoup(yc_web_page, "html.parser")
liste = soup.find_all(class_="lister-item-header")

number = 1
for film in liste:
    movie = film.find("a")
    movie = movie.text
    with open("filme.txt", "a") as file:
        file.write(str(number) + ". " + movie + "\n")
    number += 1

