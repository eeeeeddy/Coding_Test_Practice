while 1:
    a = int(input())
    ans = []

    if a == -1:
        break

    for i in range(1, a):
        if a % i == 0:
            ans.append(i)

    if a == sum(ans):
        print(a , '= ', end='')
        for i in range(len(ans)-1):
            print(ans[i] , '+ ', end='')
        print(ans[-1])
    else:
        print(a , 'is NOT perfect.')