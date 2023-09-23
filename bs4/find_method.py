from bs4 import BeautifulSoup
import requests

url_to_parse = "https://parsinger.ru/html/index1_page_1.html"
response = requests.get(url=url_to_parse)
response.encoding = "utf-8"

# метод - find()
soup = BeautifulSoup(response.text, "lxml")
div = soup.find("div", "item")
# item - название class для div элемента
print(div, "\n")

# метод - find_all()
soup = BeautifulSoup(response.text, "lxml")
div = soup.find("div", "item").find_all("li")
# div = [i.text for i in soup.find("div", "item").find_all("li")]
print(div, "\n")
for txt in div:
    print(txt.text)
print("\n")

# поиск с использованием class_
url = "https://parsinger.ru/html/headphones/5/5_32.html"
# url = "https://parsinger.ru/html/index1_page_1.html"
response = requests.get(url=url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
div = soup.find("p", class_="article").text
# div = soup.find_all("p", class_="price")
print(div, "\n")

# поиск с использованием id
url = "https://parsinger.ru/html/headphones/5/5_32.html"
response = requests.get(url=url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
div = soup.find("p", id="p_header").text
print(div, "\n")

# поиск по атрибуту с использованием id
url = "https://parsinger.ru/html/headphones/5/5_32.html"
response = requests.get(url=url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
div = soup.find("span", {"name": "count"}).text
print(div, "\n")



#Задание

response = requests.get("https://parsinger.ru/html/index1_page_1.html")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
list_price = soup.find_all("p", "price")
print(list_price, "\n")
all_price = sum([int(i.text.rstrip(" руб")) for i in list_price])
print(all_price)

