n,m = map(int,input().split())

se = [0 for i in range(n)]

for i in range(m):
  a,b = map(int,input().split())
  tmp = 1
  for j in range(b,b+a):
    if se[j%n] == 1:
      tmp = 0
  if tmp==1:
    for j in range(b,b+a):
      se[j%n] = 1
      ans+=1

print(ans)