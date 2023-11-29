from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 우선순위(p), 인덱스(l), 임시(tmp)로 사용하기위한 deque 생성
    p = deque(priorities)
    l = deque(i for i in range(len(p)))
    tmp = deque()

    while len(p) >= 1:
        Max = max(p)                    # 현재 p에서 우선순위가 가장 높은 값 Max로 지정
        if p[0] == Max:                 # p의 가장 앞의 값이 Max라면
            p.popleft()                 # p에서 제거
            tmp.append(l.popleft())     # tmp에 l 값을 넣는다. (해당 값이 인덱스이므로)
        else:                           # deque p, l 회전(가장 앞의 값을 가장 뒤로 이동)
            p.append(p.popleft())
            l.append(l.popleft())
    
    answer = tmp.index(location) + 1    # tmp에서 location 값에 위치하는 숫자+1이 해당 프로세스의 실행 순서

    return answer