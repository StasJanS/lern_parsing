import time
from random import choice

import requests

url = "http://httpbin.org/user-agent"

while line := open("user_agent.txt").read().split("\n"):
    user_agent = {"user-agent": choice(line)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)
    time.sleep(10)
