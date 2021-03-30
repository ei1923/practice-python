i = 0
name = "ei1923"

while i < 3:
  print("%d:%s" %(i, name))
  i += 1
else:
  print("finish!")

for i in range(0, 10):
  if i == 5:
    continue
  print(i)
else:
  # 正常終了した場合に実行
  # break等で途中離脱した場合は実行されない
  print("Finish!")