def solution(s):
    answer = [0, 0] # [변환 횟수, 제거된 0의 갯수]

    # s가 "1"이 될 때까지 while문 수행
    while int(s, 2) > 1:
        # 1. x의 모든 0을 제거
        answer[1] += s.count("0") # "0"의 갯수를 세고 answer[1]에 더해줌
        s = s.replace("0", "") # "0" 제거

        # 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 변환
        s = bin(len(s))[2:] # s의 길이를 2진수로 변환
        answer[0] += 1

    return answer