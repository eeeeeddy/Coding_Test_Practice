n = int(input())
x = list(map(int, input().split()))
v = int(input())

cnt = 0

for i in x:
    if v == i:
        cnt += 1
print(cnt)