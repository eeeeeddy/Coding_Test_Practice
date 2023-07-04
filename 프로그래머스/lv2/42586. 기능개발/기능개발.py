import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    tmp = deque()
    cnt = 1

    # 작업별로 배포까지 걸리는 일수 계산
    for i in range(len(progresses)):
        tmp.append(math.ceil((100-progresses[i])/speeds[i]))

    Max = tmp[0]
    for i in range(1, len(tmp)):
        if Max >= tmp[i]:
            cnt += 1
        else:
            Max = tmp[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer