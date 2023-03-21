"LAB 3"
def p1():
    slovo = ''
    stroka = ''
    while slovo != 'stop':
        slovo = input("Введите слово: ")
        stroka = stroka + (slovo) + ', '

    strokafinal = stroka[:-8]
    print (strokafinal)


def p2():
    stroka=input("Введите слово/фразу: ")
    a=stroka.find("ф")
    if a == -1:
        print ("Эх, это не очень редкое слово")
    else:
        print ("Ого! Это редкое слово!")

def p3():
    from random import randint

    print ("Для завершения игры введите слово stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        while not res.isdigit() and res != "stop":
            print ("Вы ввели что-то не то, повторите ввод: ", end="")
            res = input()
        if res == "stop":
            break
        res = int (res)
        if a+b == res:
            print("Правильно!")
        else:
            print("Ответ неверный!")


p1(), p2(), p3()


