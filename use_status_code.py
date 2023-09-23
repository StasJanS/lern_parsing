import requests

#Задание

url = "https://parsinger.ru/task/1/{}.html"
for i in range(1, 501):
    url = f"https://parsinger.ru/task/1/{i}.html"
    response = requests.get(url=url)
    if response.status_code == 200:
        print(url)
    else:
        print(i)
