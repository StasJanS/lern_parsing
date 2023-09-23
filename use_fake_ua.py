# import fake_useragent
# ua = fake_useragent.UserAgent()
from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/user-agent"

for i in range(10):
    ua = UserAgent()
    fake_ua = {"user-agent": ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)
