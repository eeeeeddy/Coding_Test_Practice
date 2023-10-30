def solution(t, p):
    answer = 0
    temp = []

    for i in range(len(t)-len(p)+1):
        temp.append(int(t[i:i+len(p)]))

    for i in temp:
        if i <= int(p):
            answer += 1

    return answer