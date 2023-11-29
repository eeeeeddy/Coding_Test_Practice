def solution(n):
    answer, i = [], 1

    while len(answer) < 101:    # n의 범위가 1부터 100까지 이므로 answer 리스트의 크기가 100이 될 때까지 진행
        if i % 3 != 0:          # n이 3의 배수가 아닐 경우 answer 리스트에 추가
            answer.append(i)
            if '3' in str(i):   # n에 '3'이 포함되어 있을 경우 answer에서 pop
                answer.pop()
        i += 1

    return answer[n-1]