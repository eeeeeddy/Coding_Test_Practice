n = int(input())

for i in range(n):
    map = {}
    ans = 1
    x = int(input())
    for j in range(x):
        a, b = input().split()
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1
    for k in map.keys():
        ans = ans * (map[k]+1)
    print(ans-1)