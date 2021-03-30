print("五文字以上を入力して")

# 1行の入力(空白も全て入力)
s = input()

print("文字列の長さ: %d" %(len(s)))
print(s)

print("2文字目から4文字目 ",end="")
print(s[1:4])

print("3文字目以降 ",end="")
print(s[2:])

print("3文字目まで ",end="")
print(s[:3])

print("全て大文字 ",end="")
print(s.upper())

print("全て小文字 ",end="")
print(s.lower())