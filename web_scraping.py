import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.content, "lxml")

titles = soup.find_all("h2", {"class": "post-title"})

# print(title)
for title in titles:
    print(title.getText(), end="")