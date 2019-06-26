import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

conn = MongoClient('180.76.110.178', 27017)
db = conn.weibo
my_set = db.test_set2

page = 1
stop = True
base_url = "https://m.weibo.cn/api/container/getIndex?"

headers = {
            "Host" : "m.weibo.cn",
            "Referer" : "https://m.weibo.cn/u/5118958928",
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
            "X-Requested-With" : "XMLHttpRequest",
          }

def _get_page(page):
    #采集姗姗数据
    pargrms = {
        "type" : "uid",
        "value" : "5118958928",
        "containerid" : "1076035118958928",
        "page": page
        }

    url = base_url + urlencode(pargrms) #https://m.weibo.cn/api/container/getIndex?type=uid&value=5118958928&containerid=1076035118958928&page=1
    reponse = requests.get(url=url,headers=headers)
    try:
        if reponse.status_code == 200:
            return reponse.json(),page
    except requests.ConnectionError as e:
        print("Error",e.args)
    except:
        raise


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
                    yield weibo
        else:
            yield 1

def save_to_mongo(result):
    if my_set.insert(result):
        print('Saved to Mongo success!')


if __name__ == "__main__":
    while stop:
        json = _get_page(page)
        a = _parse_page(*json)
        for i in a:
            if i == 1:
                stop = False
                break
            else:
                save_to_mongo(i)
        page += 1



