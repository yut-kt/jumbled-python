#coding:utf-8

def generator():
    num = 10
    while True:
        yield num
        num += 1

for num in generator():
    num10, num8, num2 = [], [], []

    tnum = num
    while tnum != 0:
        num10.append(tnum % 10)
        tnum /= 10

    tnum = num
    while tnum != 0:
        num8.append(tnum % 8)
        tnum /= 8

    tnum = num
    while tnum != 0:
        num2.append(tnum % 2)
        tnum /= 2

    num10l = num10
    num10r = list(num10)
    num10r.reverse()

    num8l = num8
    num8r = list(num8)
    num8.reverse()

    num2l = num2
    num2r = list(num2)
    num2r.reverse()
    if num10l == num10r and num8l == num8r and num2l == num2r:
        print num
        break
