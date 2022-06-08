import turtle
import time
import sys


step = 0


def print_process():
    total = 14
    global step
    step = step + 1
    num_arrow = step
    num_line = total - num_arrow
    percent = step * 100.0 / total
    process_bar = '\r' + '[' + '>' * num_arrow + '-' * num_line + ']' \
                  + '%.2f' % percent + '%'
    sys.stdout.write(process_bar)
    sys.stdout.flush()


def drawLine(x, y, direction, len, angle=0, r=0):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.pendown()
    if angle == 0:
        turtle.fd(len)
    else:
        turtle.circle(r, angle)
    print_process()
    time.sleep(0.01)


def drawLine_continue(direction, len, angle=0, r=0):
    turtle.seth(direction)
    if angle == 0:
        turtle.fd(len)
    else:
        turtle.circle(r, angle)
    print_process()
    time.sleep(0.01)


def drawCharacter():
    print('--------begin to write--------')
    drawLine(-570, 0, 0, 300)                    # 横
    drawLine(-400, 150, -90, 0, 45, -500)        # 撇
    drawLine(-420, -50, -45, 200)                # 捺
    drawLine(-100, 150, -45, 21)                 # 点
    drawLine(-50, 150, -60, 23)                  # 点
    drawLine(20, 150, -150, 23)                  # 点
    drawLine(-160, 120, -90, 30)                 # 竖
    drawLine(-160, 120, 0, 220)                  # 横折
    drawLine_continue(-90, 30)
    drawLine(-100, 50, 0, 100)                   # 横折竖钩
    drawLine_continue(-135, 80)
    drawLine_continue(-90, 180)
    drawLine_continue(135, 40)
    drawLine(-180, -30, 0, 260)                  # 横
    print('\n' + '--------end--------')
    turtle.reset()
    turtle.clear()


def setup():
    turtle.setup(2000, 1000, 0, 0)
    turtle.speed(3)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    drawCharacter()


if __name__ == "__main__":
    setup()
