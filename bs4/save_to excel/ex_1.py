import csv

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def used_exercise_1():
    postfix_url = "https://parsinger.ru/html/"
    url = "https://parsinger.ru/html/index4_page_1.html"
    soup_all = get_soup(url)
    all_params = []

    # Находим колличество страниц товара (ссылки колличества страниц)
    pagen = soup_all.find("div", class_="pagen").find_all("a")
    list_page_urls = [url["href"] for url in pagen]

    for link in list_page_urls:
        soup_page = get_soup(f"{postfix_url}{link}")

        # для каждой страницы находим ссылки для перехода на каждый товар
        obj_page = [x.text for x in soup_page.find_all("a", class_="name_item")]
        obj_descr = [z.text.split("\n") for z in soup_page.find_all("div", class_="description")]
        price = [x.text for x in soup_page.find_all("p", class_="price")]
        for ind, el in enumerate(obj_descr):
            all_params.append([obj_page[ind], el[1].lstrip("Бренд: "), el[2].lstrip("Форм-фактор: "),
                               el[3].lstrip("Ёмкость: "), el[4].lstrip("Объем буферной памяти: "), price[ind]])

    # Создаём заголовки
    with open("ex_1.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["Наименование", "Бренд", "Форм-фактор", "Ёмкость", "Объём буф.памяти", "Цена"])

    # заполняем таблицу
    for el in all_params:
        with open("ex_1.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(el)


if __name__ == '__main__':
    used_exercise_1()
