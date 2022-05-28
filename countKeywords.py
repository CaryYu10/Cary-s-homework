import keyword


def txt_sort():
    txt = open("Keywords_ex.py", "r").read()
    txt = txt.lower()
    for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(i, " ")
    return txt


def count(message):
    counts = {}
    for word in message:
        if word in keyword.kwlist:
            counts[word] = counts.get(word, 0) + 1  # 对单词出现的频率进行统计
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items


def show_fre(item):
    for i in range(10):
        word, count = item[i]  # 返回相对应的键值对
        print("{0:<10}{1:>5}".format(word, count))


def run():
    temp_message = txt_sort()
    words = temp_message.split()
    fre = count(words)
    show_fre(fre)


if __name__ == '__main__':
    run()
