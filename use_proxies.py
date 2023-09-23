import time
from random import choice

import requests

url = "http://httpbin.org/ip"

# proxy = {
#     "http": "http://80.179.140.189",
#     "https": "http://80.179.140.189",
# }
# proxy_socks4 = {
#     "http": "socks4://184.181.217.201",
#     "https": "socks4://184.181.217.201",
# }
#
# response = requests.get(url=url, proxies=proxy)
# print(response.json())


# with open("proxy.txt") as file:
#     proxy_file = file.read().split("\n")
#     for _ in range(1000):
#         try:
#             ip = choice(proxy_file).strip()
#             proxy = {
#                 "http": f"http://{ip}",
#                 "https": f"http://{ip}"
#             }
#             response = requests.get(url=url, proxies=proxy)
#             print(response.json(), "Всё получилось!!!")
#         except Exception as _ex:
#             continue


proxy = {
    "http": "http://185.162.228.32",
    "https": "http://185.162.228.32",
}
start = time.perf_counter()  #Счетчик производительности для бенчмаркинга
try:
    requests.get(url=url, proxies=proxy, timeout=1)
except Exception as _ex:
    print(_ex)
    print(time.perf_counter() - start, "!!!")

