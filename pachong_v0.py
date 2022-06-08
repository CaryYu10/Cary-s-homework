import requests
from bs4 import BeautifulSoup
allUniv = []


def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    else:
        return False


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("error")
        return ""


def fillClubList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleClub = []
        for td in ltd:
            lspan = td.find_all('span')
            if lspan:
                for ch in lspan:
                    ch = ch.string
                    if is_Chinese(ch):
                        singleClub.append(ch)
            else:
                td = td.string
                singleClub.append(td)
        allUniv.append(singleClub)


def printClubList(num):
    for i in range(num):
        u = allUniv[i]
        # print(u)
        print(u[0], u[1], u[2], u[3], u[11])


def run():
    url = 'https://data.qtx.com/jifenbang/Jnlj4Y2624_mV6o3Q06GR.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillClubList(soup)
    printClubList(22)


if __name__ == '__main__':
    run()
