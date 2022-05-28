import digit
import character
import HashFunction
import countKeywords
import Game
import pachong
import pachong_new
import grammar_detection
import grammar


def menu():
    print('Homework of Changyuan Yu:\n 1. Hash Function \n 2. Draw Characters \n 3. Draw Digit \n 4. Count Keywords \n '
          '5.Simulate Games \n 6.Spider \n 7.Auto Visit Websites \n 8.Grammar Detection \n  0. Exit \n')
    while True:
        chooseHomework = input('Please choose homework: \n')
        if chooseHomework == '0':
            break
        if chooseHomework == '1':
            print('Show hash function as follow \n')
            HashFunction.Hash()
        if chooseHomework == '2':
            print('Show draw character and process bar as follow \n')
            character.setup()
        if chooseHomework == '3':
            print('Show draw 7-digit as follow \n')
            digit.setup()
        if chooseHomework == '4':
            print('Show count keywords as follow \n')
            countKeywords.run()
        if chooseHomework == '5':
            print('Show simulating games as follow\n')
            Game.run()
        if chooseHomework == '6':
            print('Show spider as follow \n')
            pachong.run()
        if chooseHomework == '7':
            print('Show auto visit websites as follow \n')
            pachong_new.run()
        if chooseHomework == '8':
            submenu()
        else:
            print('No related homework, please try again \n')


def submenu():
    v = input('Please choose version: \n 1.Grammar detection with regularization \n 2.Grammar detection without '
              'regularization')
    if v == '1':
        grammar.run()
    elif v == '2':
        grammar_detection.run()
    else:
        print('Undefined input, default choose version 1')
        grammar.run()


def main():
    menu()


main()
