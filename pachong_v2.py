import requests
import re
from bs4 import BeautifulSoup


def getInput():
    while True:
        try:
            web = input("请输入需要爬取的网站：")
            r = requests.get(web)
            layer = eval(input("请输入需要爬取的层数："))
            break
        except:
            print("无法访问该网站，请检测格式并重新输入")
    return layer, web


def geturls(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")
    link_list = []
    for link in links:
        link = link.get("href")
        try:
            # r = requests.get(link)
            if re.match('(h)(t){2}(p)', link):
                link_list.append(link)
            else:
                continue
        except:
            # print("访问错误，正在重新访问")
            continue
    return link_list


def getLinks(url, layers):
    l = 0
    havedone = []
    link_list = geturls(url)
    while l < layers:
        l += 1
        havedone.append(url)
        print("当前在爬第 %s 层网址: %s" % (l, url))
        print("该网页内共%s个链接" % len(link_list))
        for item in link_list:
            print(item)
        if l == layers:
            break
        for item in link_list:
            temp = geturls(item)
            if (len(temp) != 0) & (item not in havedone):
                url = item
                link_list = temp
                break
            else:
                continue
    print("访问结束，共爬取 %s 层" % l)


def run():
    layer, url = getInput()
    getLinks(url, layer)


if __name__ == "__main__":
    run()
