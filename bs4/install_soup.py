from bs4 import BeautifulSoup
import requests
import lxml

# #Пример_1 - Передача файла HTML напрямую БЕЗ использования менеджера контекста
#
# file = open("index.html", encoding="utf-8")
# soup = BeautifulSoup(file, "lxml")
# file.close()
# print(soup)
#
#
# #Пример_2 - Передача файла HTML напрямую С использованием менеджера контекста
#
# with open("index.html", "r", encoding="utf-8") as file:
#     soup = BeautifulSoup(file, "lxml")
#     print(soup)


#Пример_3 - Передача объекта response прямо из запроса

response = requests.get(url="http://parsinger.ru/html/watch/1/1_1.html")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

print(soup)
