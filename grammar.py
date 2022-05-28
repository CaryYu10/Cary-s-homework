import re


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


def loadText(fileName):         # 逐行打开文件
    try:
        print("正在检测 %s 文件语法错误" % fileName)
        f = open(r'%s' % fileName, encoding='utf-8')
    except:
        fileName = 'grammar_detection.py'
        print("正在检测 %s 文件语法错误" % fileName)
        f = open(r'%s' % fileName, encoding='utf-8')
    data = f.readlines()
    return data


def run():
    filename = input("请输入待检测文件名，若输入错误则默认为检测'grammar_detection.py'文件：")  # 选定需检测的文件
    text = loadText(filename)
    text = del_hash(text)
    text = del_space(text)
    error = check(text)
    getResult(error)


if __name__ == '__main__':
    run()
