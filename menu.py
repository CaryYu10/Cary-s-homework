import digit
import character
import HashFunction
import countKeywords
import Game
import pachong_v0
import pachong_v1
import pachong_v2
import grammar_detection
import grammar


def menu():
    intro()
    while True:
        chooseHomework = input('Please choose homework: \n')
        if chooseHomework == '0':
            break
        if chooseHomework == '1':
            print('Show hash function as follow \n')
            HashFunction.Hash()
            intro()
        if chooseHomework == '2':
            print('Show draw character and process bar as follow \n')
            character.setup()
            intro()
        if chooseHomework == '3':
            print('Show draw 7-digit as follow \n')
            digit.setup()
            intro()
        if chooseHomework == '4':
            print('Show count keywords as follow \n')
            countKeywords.run()
            intro()
        if chooseHomework == '5':
            print('Show simulating games as follow\n')
            Game.run()
            intro()
        if chooseHomework == '6':
            print('Show spider as follow \n')
            pachong_v0.run()
            intro()
        if chooseHomework == '7':
            submenu1()
            intro()
        if chooseHomework == '8':
            submenu2()
        else:
            print('No related homework, please try again \n')


def submenu1():
    while True:
        try:
            v = eval(input('Please choose version: \n 1.Auto visit websites with given number \n 2.Auto visit '
                           'websites with given depth'))
            break
        except:
            print("Input error, please choose again")
    if v == 1:
        pachong_v1.run()
        intro()
    elif v == 2:
        pachong_v2.run()
        intro()
    else:
        print('Undefined input, default choose version 1')
        pachong_v2.run()


def submenu2():
    while True:
        try:
            v = eval(input('Please choose version: \n 1.Grammar detection with regularization \n 2.Grammar detection '
                           'without regularization'))
            break
        except:
            print("Input error, please choose again")
    if v == 1:
        grammar.run()
        intro()
    elif v == 2:
        grammar_detection.run()
        intro()
    else:
        print('Undefined input, default choose version 1')
        grammar.run()


def intro():
    print('Homework of Changyuan Yu:\n 1. Hash Function \n 2. Draw Characters \n 3. Draw Digit \n 4. Count Keywords \n '
          '5.Simulate Games \n 6.Spider \n 7.Auto Visit Websites \n 8.Grammar Detection \n  0. Exit \n')


if __name__ == "__main__":
    menu()
