from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status()
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
anchor_tags = soup.find_all(name="a", class_="titlelink")
article_text = []
article_link = []
for tag in anchor_tags:
    text = tag.getText()
    article_text.append(text)
    link = tag.get("href")
    article_link.append(link)

article_upvotes = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name="span", class_="score")]   # for id use .select instead of find all

print(article_text)
print(article_link)
print(article_upvotes)
pos = article_upvotes.index(max(article_upvotes))
article = article_text[pos]
link = article_link[pos]
print(max(article_upvotes), article, link)
