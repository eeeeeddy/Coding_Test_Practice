def solution(s):
    answer = 0

    s = s.split(' ') # 공백 제거 후 리스트로 저장

    for i in range(len(s)):
        if s[i] != "Z": # Z가 아닐 경우 answer에 더함
            answer += int(s[i])
        else:           # Z일 경우 Z 앞에 값을 빼줌
            answer -= int(s[i-1])

    return answer