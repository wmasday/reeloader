import requests, re, os
from colorama import Fore, Style
# from requests import Session
# s = Session()

banner = """

.___  ________         __________              .__
|   |/  _____/         \______   \ ____   ____ |  |   ______
|   /   \  ___   ______ |       _// __ \_/ __ \|  |  /  ___/
|   \    \_\  \ /_____/ |    |   \  ___/\  ___/|  |__\___ \ 
|___|\______  /         |____|_  /\___  >\___  >____/____  >
            \/                 \/     \/     \/          \/ 

               ---[ github.com/akuhidayat ]---
"""

headers = {
    'user-agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
print(f"{Fore.CYAN}{banner}")
url = input(f"{Fore.CYAN}Url : {Style.RESET_ALL}")
req = requests.get(url, headers=headers).text
video_url = re.findall('"video_url":"(.*?)"', req)[0]
extract_url = video_url.replace("\\u0026","&")
download = requests.get(extract_url, headers=headers)
name = input(f"{Fore.CYAN}Filename : {Style.RESET_ALL}")
with open(f"{name}.mp4", "wb") as result:
     result.write(download.content)
     print (f"{Fore.GREEN} Download Success!", Style.RESET_ALL)
# req = s.get(url, headers=headers).text
