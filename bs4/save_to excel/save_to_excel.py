import csv
import requests
from bs4 import BeautifulSoup

lst = ["one", "two", "three"]

"""
    newline="" - указывается всегда, для правильной работы интерпритатора;
    delimiter=";" - указывае, каким будет разделитель между элементами списка;
"""


def get_soup(url):
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def test_save_csv_1():
    with open("save_to_excel_1.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(lst)


def test_save_csv_2():
    with open("save_to_excel_2.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["Наименование", "Артикул", "Бренд", "Модель", "Тип", "Игровая", "Размер", "Подсветка", "Разрешение",
             "Сайт производителя", " В наличии", "Цена"])

    url = "http://parsinger.ru/html/mouse/3/3_11.html"
    soup = get_soup(url)

    name = soup.find("p", id="p_header").text
    article = soup.find("p", class_="article").text.split(": ")[1]
    brand = soup.find("li", id="brand").text.split(": ")[1]
    model = soup.find("li", id="model").text.split(": ")[1]
    type = soup.find("li", id="type").text.split(": ")[1]
    purpose = soup.find("li", id="purpose").text.split(": ")[1]
    light = soup.find("li", id="light").text.split(": ")[1]
    size = soup.find("li", id="size").text.split(": ")[1]
    dpi = soup.find("li", id="dpi").text.split(": ")[1]
    site = soup.find("li", id="site").text.split(": ")[1]
    in_stock = soup.find("span", id="in_stock").text.split(": ")[1]
    price = soup.find("span", id="price").text.split(" ")[0]

    with open("save_to_excel_2.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            [name, article, brand, model, type, purpose, light, size, dpi, site, in_stock, price])


if __name__ == '__main__':
    # test_save_csv_1()
    test_save_csv_2()
