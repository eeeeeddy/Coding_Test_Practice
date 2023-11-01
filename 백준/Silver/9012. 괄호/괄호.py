from collections import deque

n = int(input())

for i in range(n):
    ps = input()
    tmp = deque([1])

    if ps.count('(') != ps.count(')'):
        print('NO')
    else:
        for i in range(len(ps)):
            if ps[i] == '(':
                tmp.append(ps[i])
            else:
                if tmp[len(tmp)-1] == '(':
                    tmp.pop()
                else:
                    tmp.append(ps[i])
        if len(tmp) == 1:
            #print(tmp)
            print('YES')
        else:
            #print(tmp)
            print('NO')