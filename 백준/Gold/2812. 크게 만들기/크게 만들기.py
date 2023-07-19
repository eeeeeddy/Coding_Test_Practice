n, k = map(int,input().split())
Arr = list(input())
stack = []
tmp = k

for i in range(n):
    while  (k > 0) and (stack) and (stack[-1] < Arr[i]):
      stack.pop()
      k -= 1
    stack.append(Arr[i])
 
print(''.join(stack[:n-tmp]))