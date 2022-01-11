from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = [movie.text for movie in soup.find_all(name="h3", class_="title")]
titles_ascending = [titles[i] for i in range(len(titles)-1, -1, -1)]

# with open(file="movies.txt", mode="w") as file:
#     for item in titles_ascending:
#         file.write(f"{item}\n")