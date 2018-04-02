import requests
from bs4 import BeautifulSoup


base_url = "https://udn.com"
start_url = base_url + "/news/index"

req = requests.get(start_url)

soupObj = BeautifulSoup(req.text, 'html.parser')

# print(soup.a)
sports = ""
for link in soupObj.find_all('a'):
    s = set(link.contents)
    if u'運動' in s:
        temp = link.get('href')
        sports = temp
        print("sports >>>>>" + temp)
        print("link >>>>>> " + base_url+temp)
        break

sports_url = base_url + sports
print(sports_url)
req2 = requests.get(sports_url)
print(req2.status_code)
soupObj2 = BeautifulSoup(req2.text, 'html.parser')

# for dl in soupObj2.find_all("dl", attrs={"class": "listing"} ):
#     print(dl.find_next("dt").find_all_next("h2"))
print("==================")
ob = soupObj2.find_all("div", attrs={'class': 'area'})
for i in ob:
    x = i.find_next("h3")
    print(x.contents)
    if u"最新文章" in x.contents:
        # print("there") 
        print("==================")
        top_news = x.next_sibling
        for item in top_news.find_all("h2"):
            print(item.get_text())
        # t = x.find_next("dl", attrs={"class": "listing"} )
        
        # for child in t.descendants:
        #     print(child)
            # print(t)
        break

