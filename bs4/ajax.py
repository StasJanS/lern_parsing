import requests
from icecream import ic

# url = "https://bitality.cc/Home/GetSum?GiveName=Bitcoin%20Cash&GetName=Litecoin&Sum=8.540485&Direction=0"
# headers = {"x-requested-with": "XMLHttpRequest"}
# response = requests.get(url=url, headers=headers).json()
# print(response)

headers = {"x-requested-with": "XMLHttpRequest"}

data = {
    "GiveName": "Monero",
    "GetName": "Dash",
    "Sum": 100,
    "Direction": 0
}

url = "https://bitality.cc/Home/GetSum?"

response = requests.get(url=url, headers=headers, params=data).json()
ic(response)