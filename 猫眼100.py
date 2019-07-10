import re
import requests
a = 10
for i in range(10):
    page = i * a
    url = "https://maoyan.com/board/4?offset={}".format(page)
    text = requests.get(url)
    pat = re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?data-s'
                 'rc="(.*?)".*?alt="(.*?)".*?</a>.*?star.*?>(.*?).*?</p>.*?releasetime">(.*?)</p>.*?</dd>',re.S)
    result = re.findall(pat,text.text)
    for item in result:
         print(item)
