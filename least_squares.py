# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import normal

N = 0 #サンプルのxの個数。あとで標準入力する
M = [0,0,0,0] #求めたい多項式の次数４つ。あとで標準入力する

#データセットを作成
def create_data(M_num):
    dataset = DataFrame(columns = ['x', 'y'])
    for i in range(M_num):
        x = float(i) / float(M_num - 1) #0~1の範囲に指定した数だけのxを等間隔で作成
        y = np.sin(2 * np.pi * x) + normal(scale = 0.7) #正規分布で標準偏差0.7の範囲の雑音をsin(2πx)に付加
        dataset = dataset.append(Series([x, y], index=['x', 'y']), ignore_index = True)

    return dataset

#最小二乗法
def l_s_method(dataset, m):
    t = dataset.y #tベクトルを作成
    phi = DataFrame()
    #Φ行列を作成
    for i in range(0, m+1):
        p = dataset.x ** i
        p.name = "x ** %d" % i
        phi = pd.concat([phi, p], axis = 1)
    #w=(Φ^T*Φ)^(−1)*Φ^T*tを計算
    ws = np.dot(np.dot(np.linalg.inv(np.dot(phi.T,phi)), phi.T), t)
    #関数f(x)を作成
    def f(x):
        y = 0
        for i, w in enumerate(ws):
            y += w * (x ** i)
        return y

    return (f, ws)

#平方根平均二乗誤差の計算
def rm_square_error(dataset, f):
    err = 0.0
    for index, line in dataset.iterrows():
        x, y = line.x, line.y
        err += 0.5 * (y - f(x)) ** 2
    print np.sqrt(2 * err / len(dataset))
    return np.sqrt(2 * err / len(dataset))


def main():
    N = int(raw_input("学習データ数 : "))
    M = [int(i) for i in raw_input("多項式の次数(4つ) : ").split(" ")] #スペース区切りで4つ入力
    
    training_set = create_data(N) #学習用データを作成
    df_ws = DataFrame()

    fig = plt.figure()
        
    for c, m in enumerate(M):
        f, ws = l_s_method(training_set, m)
        df_ws = df_ws.append(Series(ws, name = "M = %d" % m))
        #グラフを４つ表示するためsubplotを利用してグラフを作成
        subplot = fig.add_subplot(2, 2, c + 1)
        subplot.set_xlim(-0.1, 1.1) #グラフが表示するxの範囲
        subplot.set_ylim(-2, 2) #グラフが表示するyの範囲
        subplot.set_title("M:%d" % m) #Mの値
        subplot.scatter(training_set.x, training_set.y, marker='x', color='blue')

        linex = np.linspace(0, 1, 101)
        liney = f(linex)
        Label = "RMS:%.2f" % rm_square_error(training_set, f)
        subplot.plot(linex, liney, color = 'red', label=Label)
        subplot.legend(loc = 1)
    #グラフを表示
    fig.show()
    raw_input("enter.")
        
if __name__ == '__main__':
    main()
