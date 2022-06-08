import turtle


def drawgap():      # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):     # 绘制单段数码管
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)


def drawDigit(digit):       # 根据数字绘制七段数码管
    drawLine(True) if digit in [2 , 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):     # data为日期，格式为'%Y-%m=%d+'
    turtle.pencolor("red")
    for i in date:
        try:
            if i == '年':
                turtle.write('年', font=("Arial", 24, "normal"))
                turtle.fd(40)
            elif i == '月':
                turtle.write('月', font=("Arial", 24, "normal"))
                turtle.fd(40)
            elif i == '日':
                turtle.write('日', font=("Arial", 24, "normal"))
                turtle.fd(40)
            else:
                drawDigit(eval(i))
        except NameError:
            print('undefined type \n')


def drawTime(time):
    turtle.pencolor("red")
    for i in time:
        try:
            if i == '分':
                turtle.write('分', font=("Arial", 24, "normal"))
                turtle.fd(40)
            elif i == '秒':
                turtle.write('秒', font=("Arial", 24, "normal"))
                turtle.fd(40)
            elif i == '时':
                turtle.write('时', font=("Arial", 24, "normal"))
                turtle.fd(40)
            else:
                drawDigit(eval(i))
        except NameError:
            print('undefined type \n')
            break


def drawNumber(number):
    for i in number:
        try:
            drawDigit(eval(i))
        except NameError:
            print('undefined type \n')


def digit_menu():
    while True:
        type = input('请选择输入类型：\n 1. 时间 \n 2. 日期 \n 3. 任意数字 \n')
        if type == '1':
            drawTime(input('请输入时间，如10时10分10秒 \n'))
            break
        if type == '2':
            drawDate(input('请输入日期，如2022年2月22日 \n'))
            break
        if type == '3':
            drawNumber(input('请输入任意一串数字 \n'))
            break
        else:
            print("输入错误，请重新输入")


def setup():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    digit_menu()
    turtle.reset()
    turtle.clear()


if __name__ == "__main__":
    setup()
