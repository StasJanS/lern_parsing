import requests
from bs4 import BeautifulSoup


def use_pagination():
    url = "https://parsinger.ru/html/index1_page_1.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    pages = soup.find("div", class_="pagen").find_all("a")
    print([page.text for page in pages])  # ['1', '2', '3', '4'] - так можно узнать сколько страниц и какая последняя

    # page["href"] - извлечение ссылки, также можно и для image - image["src"]
    link_pagen = [page["href"] for page in pages]
    print(link_pagen)
    sheme = "https://parsinger.ru/html/"
    list_links = [f"{sheme}{link}" for link in link_pagen]
    print(list_links)


def test_pagination_1():
    # Задание_1
    url = "https://parsinger.ru/html/index3_page_1.html"
    sheme = "https://parsinger.ru/html/"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    pages = soup.find("div", class_="pagen").find_all("a")

    # Решение_1
    list_links = [f"{sheme}{link['href']}" for link in pages]
    all_list = []
    for i in list_links:
        response = requests.get(i)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        names = [i.text for i in soup.find_all("a", "name_item")]
        all_list.append(names)
    print(all_list)

    # Решение_2
    cont_page = int([page.text for page in pages][-1])  # или так len(pages)
    all_list_2 = []
    for x in range(1, cont_page + 1):
        response = requests.get(url=f"https://parsinger.ru/html/index3_page_{x}.html")
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        names = [i.text for i in soup.find_all("a", "name_item")]
        all_list_2.append(names)
    print(all_list_2)


def test_pagination_2():
    # Задание_2
    url = "https://parsinger.ru/html/index3_page_1.html"
    new_scheme = "https://parsinger.ru/html/"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    pages = soup.find("div", class_="pagen").find_all("a")
    cont_page = int([page.text for page in pages][-1])  # или так len(pages)
    all_article_summ = 0
    for x in range(1, cont_page + 1):
        response = requests.get(url=f"https://parsinger.ru/html/index3_page_{x}.html")
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        list_link_detail = soup.find_all("a", "name_item")
        links_detail = [i["href"] for i in list_link_detail]
        for link in links_detail:
            response = requests.get(f"{new_scheme}{link}")
            response.encoding = "utf-8"
            new_soup = BeautifulSoup(response.text, "lxml")
            art = new_soup.find("p", class_="article").text
            all_article_summ += int(art.lstrip("Артикул: "))
    print(all_article_summ)


def test_pagination_3():
    # Задание_3
    start_url = "https://parsinger.ru/html/index1_page_1.html"
    scheme = "https://parsinger.ru/html/"
    list_summ = []
    all_summ = 0

    # определяем колличество разделов
    soup = make_soup(start_url)
    link_menu = soup.find("div", "nav_menu").find_all("a")
    link_menu_prefix = [link["href"] for link in link_menu]
    print(link_menu_prefix)

    # для каждого раздела определяем колличество страниц
    for link_m in link_menu_prefix:
        soup = make_soup(f"{scheme}{link_m}")
        list_pages = soup.find("div", class_="pagen").find_all("a")
        link_pages_prefix = [link["href"] for link in list_pages]
        print(link_pages_prefix)

        # для каждой страницы определяем коллиство товара
        for link_p in link_pages_prefix:
            soup = make_soup(f"{scheme}{link_p}")
            list_link_detail = soup.find_all("a", "name_item")
            links_detail = [detail["href"] for detail in list_link_detail]
            print(links_detail)

            # Переходим на каждый товар и достаём необходимое
            for link_d in links_detail:
                soup = make_soup(f'{scheme}{link_d}')
                detail_price = soup.find("span", id="price")
                in_stock = soup.find("span", id="in_stock")
                list_summ.append(f"{in_stock.text} - {detail_price.text}")
                all_summ += int(in_stock.text.lstrip("В наличии: ")) * int(detail_price.text.rstrip(" руб"))
    print(list_summ)
    print(len(list_summ))
    print(f"ИТОГО общая стоимость товара в наличии - {all_summ} руб")


def make_soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")


if __name__ == '__main__':
    #     use_pagination()
    #     test_pagination_1()
    #     test_pagination_2()
    test_pagination_3()
