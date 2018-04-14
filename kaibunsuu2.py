#coding:utf-8

def generator():
    num = 11
    while True:
        yield num
        num += 2

for num in generator():
    num2 = bin(num)
    num2 = num2[2:]
    num8 = '%o' % num
    num10 = str(num)
    if num2 == num2[::-1] and num8 == num8[::-1] and num10 == num10[::-1]:
        print num
        break
