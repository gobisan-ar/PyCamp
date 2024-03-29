from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.string)

# print(soup.a)
# print(soup.p)
# print(soup.li)


# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))


# heading = soup.find(name="h1", id="name")
# print(heading)


# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.getText())
# print(section_heading.get("class"))


# resume_url = soup.select_one(selector="p a")
# print(resume_url)

# name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(selector=".heading")
print(headings)
