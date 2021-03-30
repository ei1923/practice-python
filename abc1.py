import numpy as np

n = int(input())
data = np.array([[int(x) for x in input().split()] for _ in range(n)])
x_t1 = int(input())
x_t2 = int(input())

#係数の計算
X = np.matrix([[data[i][0]**(j+1) for j in range(3)] for i in range(n)])
Y = np.matrix([[data[i][1]**(j+1) for j in range(3)] for i in range(n)])
w = ___

#結果の出力
y_t1 = w * x_t1
y_t2 = w * x_t2

print("{:.0f}".format(round(y_t1)))
print("{:.0f}".format(round(y_t2)))