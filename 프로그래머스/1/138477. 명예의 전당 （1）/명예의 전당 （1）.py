def solution(k, score):
    answer = []
    fame = []

    for i in range(len(score)):
        if len(fame) < k:
            fame.append(score[i])
        else:
            if fame[-1] < score[i]:
                fame.pop()
                fame.append(score[i])
        fame.sort(reverse=True)
        answer.append(fame[-1])

    return answer