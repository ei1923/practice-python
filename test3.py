msg = "Hello World"

def out(name="guest",age=24):
  global msg
  print(msg)
  msg = "chege"
  print("Hi! {0} age({1})" .format(name, age))

out("ei1923", 17)
out()

# numpyモジュールをnpと言う名前でimport
import numpy as np
data = np.array([[int(x) for x in range(3)] for _ in range(3)])
print(data[:1]) # 1列目の要素を抽出

n = int(input())
x = np.zeros(n)
y = np.zeros(n)
for i in range(n):
    x[i] = int(input())
np.average(x) # x(リスト)の平均
np.var(x)     # x(リスト)の分散
np.std(x)     # x(リスト)の標準偏差
np.cov(x,y)   # x,yの共分散
"""
array([[xの不偏分散  , 不偏共分散 ],　　　　
       [不偏共分散 ,  yの不偏分散]])
"""
# 標本の共分散  (n)->(n-1)で不偏共分散
np.sum((data[:,0] - data[:,0].mean())*(data[:,1] - data[:,1].mean())) / n
