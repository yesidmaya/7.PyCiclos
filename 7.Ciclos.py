# -*- coding: utf-8 -*-

def my_ciclo(number):
    for i in range(number):
        a = print(i)
    return a

if __name__ == "__main__":
    number = int(input('Dijite un numero: '))

    result = my_ciclo(number)
    print(result)