import keyword


def load_file():
    while True:
        filename = input(r"请输入需要检测的文件名:")
        try:
            txt = open(filename, "r", encoding='utf-8').read()
            break
        except:
            print("文件不存在，请重新输入")
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
    for i in range(len(item)):
        word, count = item[i]   # 返回相对应的键值对
        print("{0:<10}{1:>5}".format(word, count))


def run():
    temp_message = load_file()
    words = temp_message.split()
    fre = count(words)
    show_fre(fre)


if __name__ == '__main__':
    run()
