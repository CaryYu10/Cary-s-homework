from random import random


def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    A = [2, 2, 2, 2]
    B = [2, 2, 2, 2]
    a = eval(input("请输入选手A的能力值(0-1): "))
    a1 = eval(input("请输入选手A失误的概率(0-1): "))
    print("比赛天气:\n 1.晴天 \n 2.雨天 \n 3.多云 \n 4.雪天")
    for i in range(4):
        A[i] = eval(input("请按顺序选择选手A是否擅长该天气，1为擅长，0为不擅长，2为选手不受该天气影响\n"))
    b = eval(input("请输入选手B的能力值(0-1): "))
    b1 = eval(input("请输入选手B失误的概率(0-1):"))
    print("比赛天气:\n 1.晴天 \n 2.雨天 \n 3.多云 \n 4.雪天")
    for i in range(4):
        B[i] = eval(input("请按顺序选择选手A是否擅长该天气，1为擅长，0为不擅长，2为选手不受该天气影响\n"))
    c = eval(input("请选择比赛天气:\n 1.晴天 \n 2.雨天 \n 3.多云 \n 4.雪天\n"))
    n = eval(input("模拟比赛的场次: "))
    return a, a1, A, b, b1, B, c, n


def simNGames(n, probA, probB, misA, misB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, misA, misB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def Weather(w, wA, wB, pA, pB):
    if wA[w-1] == 0:
        pA = pA - 0.05
    elif wA[w-1] == 1:
        pA = pA + 0.05
    else:
        pA = pA

    if wB[w-1] == 0:
        pB = pB - 0.05
    elif wB[w-1] == 1:
        pB = pB + 0.05
    else:
        pB = pB
    return pA, pB


def gameOver(a, b):
    return a == 15 or b == 15


def simOneGame(probA, probB, misA, misB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < misA:
                scoreB += 1
                serving = "B"
            else:
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
        else:
            if random() < misB:
                scoreA += 1
                serving = "A"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
    return scoreA, scoreB


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))


def run():
    printIntro()
    probA, misA, weatherA, probB, misB, weatherB, weather, n = getInputs()
    probA, probB = Weather(weather, weatherA, weatherB, probA, probB)
    winsA, winsB = simNGames(n, probA, probB, misA, misB)
    printSummary(winsA, winsB)


if __name__ == '__main__':
    run()
