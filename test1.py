# 1行コメント
"""
複数行コメント
"""
msg = "hello world"
n = 110
print("挨拶: %s\n数字: %d\n小数: %.2f" %(msg, n, n/33))

score = int(input("score ? "))
if score > 80:
    print("Great")
elif score > 60:
    print("Good!")
else:
    print("So So!")

print("Great!" if score > 80 else "so so! ..")