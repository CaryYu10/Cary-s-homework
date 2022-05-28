def loadText(fileName):         # 逐行打开文件
    try:
        print("正在检测 %s 文件语法错误" % fileName)
        f = open(r'%s' % fileName, encoding='utf-8')
    except:
        fileName = "grammar.py"
        print("正在检测 %s 文件语法错误" % fileName)
        f = open(r'%s' % fileName, encoding='utf-8')
    data = f.readlines()
    return data


def del_space(text):           # 去除缩进造成的大量空格
    text_new = []
    for line in text:
        line = line.strip()
        text_new.append(line)
    return text_new


def del_hash(text):             # 去除代码中以‘#’为开头的注释(注释中可能含有关键词，未被除去会导致误判语法错误)
    text_new = []
    for line in text:
        j = 0
        delet = 0
        for it in line:
            if it == '#' and line[j+1] == ' ':
                line = line[:j]
                text_new.append(line)
                delet += 1
                break
            else:
                j += 1
        if delet == 0:
            text_new.append(line)
    return text_new


def checkparen(line, num):        # 判断关键词后的括号是否符合语法
    left = right = 0
    temp_l = temp_r = 0
    count = 0
    e = 0
    for item in line:
        if item == "(":
            left += 1
            temp_l = count
        elif item == ")":
            right += 1
            temp_r = count
        count += 1
    if left < right:
        e += 1
        print("Missing '(' in line %s" % num)
    elif left > right:
        print("Missing ')' in line %s" % num)
        e += 1
    elif temp_l > temp_r:
        e += 1
        print("Incorrect Parenthesis in line %s" % num)
    return e, left, right


def checkcolon(line):          # 判断关键词后的冒号是否符合语法
    colon = 0
    for item in line:
        if item == ":":
            colon += 1
    return colon


def checkin(line):             # 判断该行代码中是否含有关键词“in”
    count = 0
    for item in line:
        if item == "in":
            count += 1
    return count


def checkif(line, num):         # 判断关键词“if”是否符合语法
    e, l, r = checkparen(line, num)
    num_colon = checkcolon(line)
    if num_colon == 0:
        e += 1
        print("Missing colon in line %s" % num)
    elif num_colon > 1:
        e += 1
        print("Redundant colon in line %s" % num)
    return e


def checkelse(line, num):         # 判断关键词“else”是否符合语法
    e, l, r = checkparen(line, num)
    num_colon = checkcolon(line)
    if (l > 0) | (r > 0):
        print("Unexpected parenthesis after keyword 'try'")
        e += 1
    if num_colon == 0:
        e += 1
        print("Missing colon in line %s" % num)
    elif num_colon > 1:
        e += 1
        print("Redundant colon in line %s" % num)


def checkfor(line, words, num):           # 判断关键词“for”是否符合语法
    e, l, r = checkparen(line, num)
    num_in = checkin(words)
    num_colon = checkcolon(line)
    if num_in == 0:
        e += 1
        print("Missing keyword 'in' after keyword 'for' in line %s" % num)
    elif num_in > 1:
        e += 1
        print("Redundant keyword 'in' after keyword 'for' in line %s" % num)
    if num_colon == 0:
        e += 1
        print("Missing colon after keyword 'for' in line %s" % num)
    elif num_colon > 1:
        e += 1
        print("Redundant colon after keyword 'for' in line %s" % num)
    return e


def checktry(line, num):              # 判断关键词“try”是否符合语法
    e, l, r = checkparen(line, num)
    num_colon = checkcolon(line)
    if (l > 0) | (r > 0):
        print("Unexpected parenthesis after keyword 'try'")
        e += 1
    if num_colon == 0:
        e += 1
        print("Missing colon after keyword 'try' in line %s" % num)
    elif num_colon > 1:
        e += 1
        print("Redundant colon after keyword 'try' in line %s" % num)
    return e


def checkexcept(line, num):             # 判断关键词“except”是否符合语法
    e, l, r = checkparen(line, num)
    num_colon = checkcolon(line)
    if (l > 0) | (r > 0):
        print("Unexpected parenthesis")
        e += 1
    if num_colon == 0:
        e += 1
        print("Missing colon in line %s" % num)
    elif num_colon > 1:
        e += 1
        print("Redundant colon in line %s" % num)
    return e


def findKeywords(strdata):   # 查找代码中关键词并判断语法是否正确
    error = 0                # 记录error数
    num = 1                  # 记录error发生在第几行
    num_if = num_try = 0     # 记录关键词“if”和“try”出现的次数。以判断关键词“except”和关键词“elif”是否符合要求
    for eachline in strdata:
        temp = str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            line = temp.replace(i, " ")
        line = line.split()
        for word in line:
            if word == "if":
                error += checkif(eachline, num)
                num_if += 1
            elif word == "for":
                error += checkfor(eachline, line, num)
            elif word == "try":
                error += checktry(eachline, num)
                num_try += 1
            elif word == "elif":
                if num_if > 0:
                    error += checkif(eachline, num)
                else:
                    print("Expect keyword 'if' in front of 'elif'")
                    error += 1
            elif word == "else":
                if (num_if > 0) | (num_try > 0):
                    error += checkelse(eachline, num)
                else:
                    print("Expect keyword 'if' or 'try' before 'elif'")
                    error += 1
            elif word == "except":
                if num_try > 0:
                    error += checkexcept(eachline, num)
                else:
                    print("Expect keyword 'try' before 'except'")
                    error += 1
            elif word == "finally":
                if num_try > 0:
                    error += checkexcept(eachline, num)
                else:
                    print("Expect keyword 'try' before 'finally'")
                    error += 1
        num += 1
    if error != 0:
        print("Finish checking, there are %s" % error, "in total")
    else:
        print("Finish checking, no error found")


def run():
    filename = input("请输入待检测文件名，若输入错误则默认为检测'grammar.py'文件：")  # 选定需检测的文件
    text = loadText(filename)
    text = del_space(text)
    text = del_hash(text)
    findKeywords(text)


if __name__ == "__main__":
    run()
