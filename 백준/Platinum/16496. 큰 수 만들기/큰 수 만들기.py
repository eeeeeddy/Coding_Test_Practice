# 백준 16496
n = int(input())
arr = list(map(str, input().split()))
answer = ''

for i in range(n):
    arr[i] = arr[i]*10

arr.sort(reverse=True)

for i in arr:
    answer += i[:len(i)//10]

if int(answer) == 0:
    print(0)
else:
    print(int(answer))