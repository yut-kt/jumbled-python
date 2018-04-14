#coding:utf-8
import numpy as np 
import math

fileText = []
numText = []
inNumText = []
numFile = open('data1530.txt', 'r')
#1行目の処理
Text = numFile.readline()
Text = Text.split()
Text = map(int, Text)
for (index, num) in zip (range(len(Text)), Text):
    if index == len(Text) - 1:
        break
    inNumText.append(abs(num - Text[index + 1]))
numText.append(inNumText)

#2行目以降の処理
while True:
    Text = numFile.readline()
    if not Text:
        break
    Text = Text.split()
    fileText.append(map(int, Text))

for (index1,Text) in zip(range(len(fileText)), fileText):
    inNumText = []
    if index1 == len(fileText) - 1:
        break
    for (index2, num) in zip(range(len(Text)), Text):
        if index2 == len(Text) - 1:
            break
        inNumText.append(abs(num - fileText[index1 + 1][index2]))
    numText.append(inNumText)

data = np.array(numText)
print u"平均", data.mean()
print u"分散", data.var()

numerator, denominator = 0, 0
for (index1,Text) in zip(range(len(numText)), numText):
    if index1 == len(numText) - 1:
        break
    for (index2, num) in zip(range(len(Text)), Text):
        if index2 == len(Text) - 1:
            break
        numerator += (num - data.mean()) * (numText[index1 + 1][index2] - data.mean())
        denominator += (num - data.mean()) ** 2
print u"相互相関 = ", 1.0 * numerator / denominator

for num in range(len(numText) - 1):
    numText[1] = numText[0] + numText[1]
    del numText[0]
numerator, denominator = 0, 0
for num in range(len(numText[0]) - 1):
    numerator += (numText[0][num] - data.mean()) * (numText[0][num + 1] - data.mean())
    denominator += (numText[0][num] - data.mean()) ** 2
print u"自己相関　= ", 1.0 * numerator / denominator

num = {} #dictionary初期化
for n in numText[0]: 
    num[n] = num.get(n, 0) + 1 #keyの値の有無でdictionary新規作成かvalueの値をインクリメント
print u"エントロピー = ",
print sum(map(lambda x : -x * math.log(x, 2) , map(lambda x : x / float(len(numText[0])), num.values()))), #エントロピー算出
print "bit"
