import csv

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def used_exercise_4():
    postfix_url = "https://parsinger.ru/html/"
    url = "https://parsinger.ru/html/index4_page_1.html"
    soup_all = get_soup(url)
    all_params = []

    # находим колличество разделов
    list_category_page = [link["href"] for link in soup_all.find("div", class_="nav_menu").find_all("a")]

    for link in list_category_page:
        soup_cat = get_soup(f"{postfix_url}{link}")

        # Находим колличество страниц товара (ссылки колличества страниц)
        pagen = soup_cat.find("div", class_="pagen").find_all("a")
        list_page_urls = [url["href"] for url in pagen]

        for link in list_page_urls:
            soup_page = get_soup(f"{postfix_url}{link}")

            # для каждой страницы находим ссылки для перехода на каждый товар
            obj_page = soup_page.find_all("a", class_="name_item")
            list_object_page = [obj["href"] for obj in obj_page]

            # переходим на каждый товар и достаём необходимые параметры
            for ind, obj_link in enumerate(list_object_page):
                url_obj = f"{postfix_url}{obj_link}"
                soup_obj = get_soup(url_obj)
                name = soup_obj.find("p", id='p_header').text
                article = soup_obj.find("p", class_="article").text.lstrip("Артикул: ")
                brand = soup_obj.find("li", id="brand").text.lstrip("Бренд: ")
                model = soup_obj.find("li", id="model").text.lstrip("Модель: ")
                in_stock = soup_obj.find("span", id="in_stock").text.lstrip("В наличии: ")
                price = soup_obj.find("span", id="price").text
                old_price = soup_obj.find("span", id="old_price").text

                # Формируем общий список по объекту и ложим в общий список
                obj_list = [name, article, brand, model, in_stock, price, old_price, url_obj]
                all_params.append(obj_list)

        # Создаём заголовки
        with open("ex_3_4.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                ["Наименование", "Артикул", "Бренд", "Модел", "Наличие", "Цена", "Старая цена", "Ссылка на крточку"])

        # заполняем таблицу
        for el in all_params:
            with open("ex_3_4.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(el)


if __name__ == '__main__':
    used_exercise_4()
