import re


def del_hash(line):             # 去除代码中所有注释和引用(注释中可能含有关键词，未被除去会导致误判语法错误)
    line = re.sub(r'(#+)(\s+)(.*)', '', line)
    line = re.sub(r'("){1,3}(.*)("){1,3}', '', line)
    line = re.sub(r"('){1}(.*)('){1}", '', line)
    return line


def checkif(line, num):         # 通过正则表达式判断关键词“if”是否符合语法
    e = 0
    result = re.match('^(\s*)(.*)(if)(\s+)(.*)((>| <| ==| !=| >=| <=)?)(\s*)(.*)[:]$', line)
    if result is None:
        # print(line)
        print("第", num, "行错误使用'if'")
        e += 1
    return e


def checkelif(line, num):      # 通过正则表达式判断关键词“elif”是否符合语法
    e = 0
    result = re.match('^(\s*)(.*)(elif)(\s+)(.*)((>| <| ==| !=| >=| <=)*)(\s*)(.*)[:]$', line)
    if result is None:
        print("第", num, "行错误使用'elif'")
        e += 1
    return e


def checkelse(line, num):    # 通过正则表达式判断关键词“else”是否符合语法
    e = 0
    result = re.match("^(\s*)(else)(\s*)[:]$", line)
    if result is None:
        print("第", num, "行错误使用'else'")
        e += 1
    return e


def checkfor(line, num):     # 通过正则表达式判断关键词“for”是否符合语法
    e = 0
    result = re.match("^(\s*)(for)(\s+)(.*)(\s+)(in)(\s+)(.*)[:]$", line)
    if result is None:
        # print(line)
        print("第", num, "行错误使用'for'")
        e += 1
    return e


def checktry(line, num):     # 通过正则表达式判断关键词“try”是否符合语法
    e = 0
    result = re.match("^(\s*)(try)(.*)[:]$", line)
    if result is None:
        print("第", num, "行错误使用'try'")
        e += 1
    return e


def checkexcept(line, num):  # 通过正则表达式判断关键词“except”是否符合语法
    e = 0
    result = re.match("^(\s*)(except)(.*)[:]$", line)
    if result is None:
        print("第", num, "行错误使用'except'")
        e += 1
    return e


def check(text):
    num_line = 1
    num_try = num_if = 0
    errors = 0
    for eachline in text:
        temp = str(eachline).lower()
        eachline = del_hash(eachline)
        eachline = eachline.strip()
        temp = del_hash(temp)
        temp = temp.strip()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            line = temp.replace(i, " ")
        line = line.split()
        for words in line:
            if words == 'for':
                errors += checkfor(eachline, num_line)
            elif words == 'if':
                errors += checkif(eachline, num_line)
                num_if += 1
            elif words == 'elif':
                if num_if != 0:
                    errors += checkelif(eachline, num_line)
                else:
                    errors += 1
                    print("第", num_line, "行错误使用'elif'")
            elif words == 'else':
                if num_if != 0:
                    errors += checkelse(eachline, num_line)
                    num_if -= 1
                elif num_try != 0:
                    errors += checkelse(eachline, num_line)
                else:
                    errors += 1
                    print("第", num_line, "行错误使用'else'")
            elif words == 'try':
                errors += checktry(eachline, num_line)
                num_try += 1
            elif words == 'except':
                if num_try != 0:
                    errors += checkexcept(eachline, num_line)
                else:
                    errors += 1
                    print("第", num_line, "行错误使用'except")
        num_line = num_line + 1
    return errors


def getResult(errors):        # 返回文件语法错误数
    if errors == 0:
        print("未检测到语法错误")
    else:
        print("共发现", errors, "个语法错误")


def loadText():         # 选取需要检测的文件
    while True:
        filename = input("请输入待检测文件名")  # 选定需检测的文件
        try:
            f = open(r'%s' % filename, encoding='utf-8')
            print("正在检测 %s 文件语法错误" % filename)
            data = f.readlines()
            break
        except:
            print("未找到 %s 文件，请重新输入" % filename)
    return data


def run():
    text = loadText()
    error = check(text)
    getResult(error)


if __name__ == '__main__':
    run()
