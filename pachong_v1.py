import requests
import re


def getInput():
    while True:
        try:
            url = input("请输入需要爬取的网页：\n")
            r = requests.get(url, timeout=10)
            n = eval(input("请输入需要爬取的网页个数: \n"))
            break
        except:
            print("输入错误，请重新输入")
    return url, n


def spiderpage(url):
    r = requests.get(url, timeout=10)
    r.encoding = r.apparent_encoding
    pagetext = r.text
    # 正则表达式筛选出当前页面下所有的链接url,返回列表
    pagelinks = re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')', pagetext)
    return pagelinks


class linkQuence:
    def __init__(self):
        self.visited = []     # 已访问的url集合
        self.unvisited = []   # 待访问的url集合

    def getVisited(self):  # 获取访问过的url队列
        return self.visited

    def getUnvisited(self):  # 获取未访问的url队列
        return self.unvisited

    def addVisited(self, url):   # 添加url到访问过得队列中
        return self.visited.append(url)

    def removeVisited(self, url):   # 移除访问过得url
        return self.visited.remove(url)

    def geturl(self):   # 从未访问队列中取一个url
        try:
            # if self.unvisited[i] is None or self.unvisited == '':
            #     i += 1
            # return self.unvisited[i]
            return self.unvisited.pop(0)
        except:
            return None

    def addUnvisited(self, url):   # 添加url到未访问的队列中
        if url != "" and url not in self.visited and url not in self.unvisited:
            return self.unvisited.insert(0, url)

    def getVisited_num(self):   # 获得已访问的url数目
        return len(self.visited)

    def getUnvisited_num(self):    # 获得未访问的url数目
        return len(self.unvisited)

    def is_empty(self):  # 判断未访问的url队列是否为空
        return len(self.unvisited) == 0


class Spider:
    def __init__(self, url):
        self.linkQuence = linkQuence()     # 将队列引入本类
        self.linkQuence.addUnvisited(url)  # 传入待爬取的url,即爬虫入口

    def crawler(self, urlcount):
        x = 1
        while x <= urlcount:
            # if x > 1:
            visiturl = self.linkQuence.geturl()  # 从未访问列表中pop出一个url
            if visiturl is None or visiturl == '':
                continue
            try:
                initial_links = spiderpage(visiturl)  # 爬出该url页面中所有的链接
                print("开使访问第", x-1, "个url")
                print(visiturl)
            except:
                # print("访问错误，正在重新访问第", x-1, "个url")
                continue
            self.linkQuence.addVisited(visiturl)  # 将该url放到访问过的url队列中
            for link in initial_links:  # 将筛选出的链接放到未访问队列中
                self.linkQuence.addUnvisited(link)
            x += 1
            if self.linkQuence.is_empty():
                break
        print("共访问", self.linkQuence.getVisited_num(), "个url")
        return self.linkQuence.visited


def writetofile(list):
    # 因为第一个爬取的页面为爬虫入口,非需要的博文网址,因此从[1]开始写入
    f = open("urls.txt", "w")
    for row in list:
        f.write(row+'\n')
    f.close()


def run():
    url, num = getInput()
    spider = Spider(url)
    url_list = spider.crawler(num)    # 传入要爬取的总链接数量
    writetofile(url_list)


if __name__ == '__main__':
    run()
