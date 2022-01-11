from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    soup = BeautifulSoup(file, "html.parser")

# print(soup.title)
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())    # can use .text .string and getText()
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
class_ex = soup.find_all(name="h3", class_="heading")
print(class_ex)

# can also use css selector
company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(selector=".heading")
print(headings)
