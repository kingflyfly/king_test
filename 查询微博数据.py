import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

page = 1
base_url = "https://m.weibo.cn/api/container/getIndex?"
headers = {
            "Host" : "m.weibo.cn",
            "Referer" : "https://m.weibo.cn/u/1761179351",
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
            "X-Requested-With" : "XMLHttpRequest",
          }

def _get_page(page):
    pargrms = {
        "type" : "uid",
        "value" : "1761179351"
        ,"containerid" : "1076031761179351",
        "page": page
        }
    url = base_url + urlencode(pargrms)
    reponse = requests.get(url=url,headers=headers)
    if reponse.status_code == 200:
        return reponse.json(),page
    else:
        raise requests.ConnectionError
def _parse_page(items,page:int):
        items = items.get("data").get("cards")
        if items:
            for index,item in enumerate(items):
                if index == 1 and page == 1:
                    continue
                else:
                    item  = item.get("mblog")
                    weibo = {}
                    weibo["page"] = page
                    weibo["index"] = index
                    weibo["created_at"] = item.get("created_at")
                    weibo["source"] = item.get("source")
                    weibo["id"] = item.get("id")
                    weibo["text"]  = pq(item.get("text")).text()
                    weibo["attitudes_count"] = item.get("attitudes_count")
                    weibo["comments_count"] = item.get("comments_count")
                    weibo["reposts_count"] = item.get("reposts_count")
                    print(weibo)
        else:
            return 1

if __name__ == "__main__":
    while True:
        json = _get_page(page)
        a = _parse_page(*json)
        if a == 1:
            break
        else:
            page += 1




