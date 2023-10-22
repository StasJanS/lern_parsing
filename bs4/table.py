from decimal import Decimal
from icecream import ic
import requests
from bs4 import BeautifulSoup


def parse_url(url):
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def test_table_1():  # сумма всей таблицы
    url = "https://parsinger.ru/table/1/index.html"
    soup = parse_url(url)
    all_td = set([Decimal(i.text) for i in soup.find_all("td")])
    print(sum(all_td))  # 1240.096


def test_table_2():  # сумма первого столбца
    url = "https://parsinger.ru/table/2/index.html"
    soup = parse_url(url)
    count_th = len(soup.find_all("th")) #найдём колличество кстолбцов
    first_td = soup.find_all("td")
    list_first_td = [Decimal(first_td[i].text) for i in range(0, len(first_td), count_th)]
    ic(sum(list_first_td))  # 80.726


def test_table_3():  # сумма жирных цифр с жирным шифром
    url = "https://parsinger.ru/table/3/index.html"
    soup = parse_url(url)
    list_b = [Decimal(el.text) for el in soup.find_all("b")]
    ic(sum(list_b))  # 373.329


def test_table_4():  # сумма цифр в зелёных ячейках
    url = "https://parsinger.ru/table/4/index.html"
    soup = parse_url(url)
    list_class_green = [Decimal(el.text) for el in soup.find_all("td", class_="green")]
    ic(sum(list_class_green))  # 425.766


def test_table_5():  # сумма цифр в оранжевых ячейках умноженых на цифру в голубых ячейках
    url = "https://parsinger.ru/table/5/index.html"
    soup = parse_url(url)
    list_class_orange = [Decimal(el.text) for el in soup.find_all("td", class_="orange")]
    count_th = len(soup.find_all("th"))  # найдём колличество кстолбцов
    first_td = soup.find_all("td")
    list_class_blue = [int(first_td[i].text) for i in range(count_th - 1, len(first_td), count_th)]
    new_list = [val*list_class_orange[ind] for ind, val in enumerate(list_class_blue)]
    ic(sum(new_list))  # 2521465.686


def test_table_6():  # сумма цифр в оранжевых ячейках умноженых на цифру в голубых ячейках
    url = "https://parsinger.ru/table/5/index.html"
    soup = parse_url(url)
    count_list_th = len(soup.find_all("th"))
    list_td = [float(i.text) for i in soup.find_all("td")]
    res = {i: 0 for i in range(count_list_th)} # создадим словарь с ключами - порядковым номером столбцов и значением 0
    for ind in range(count_list_th):
        for i in range(ind, len(list_td), count_list_th):
            res[ind] += list_td[i]
    result = {f"{k+1} column": round(v, 3) for k, v in res.items()}
    print(result)


if __name__ == '__main__':
    # test_table_1()
    # test_table_2()
    # test_table_3()
    # test_table_4()
    # test_table_5()
    test_table_6()
