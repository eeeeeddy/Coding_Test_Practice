import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    tmp = deque()
    cnt = 1

    # 작업별로 배포까지 걸리는 일수 계산
    for i in range(len(progresses)):
        tmp.append(math.ceil((100-progresses[i])/speeds[i]))

    Max = tmp[0]                    # 첫 번째 작업을 Max로 지정
    for i in range(1, len(tmp)):    # 반복문을 수행하면서 Max보다 작은 수를 만나면 cnt 증가 (한 번에 배포 되기 때문)
        if Max >= tmp[i]:           
            cnt += 1
        else:                       # Max보다 큰 수를 만나면 Max를 변경하고 지금까지의 cnt를 answer에 추가
            Max = tmp[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)              # 마지막까지 계산된 cnt를 answer에 추가 (추가되기 전에 반복문이 종료되기 때문)

    return answer