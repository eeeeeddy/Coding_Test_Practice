def solution(s):
    answer = ''

    for i in range(len(s)):
        # 문자가 숫자인지 아닌지 확인
        if ord(s[i]) >= 48 and ord(s[i]) <= 57: # 숫자일 경우
            answer += s[i]
        else: # 문자일 경우 -> 공백 다음에 존재하는지 확인
            if i == 0 or s[i-1] == ' ': # 문장의 첫 글자가 문자인 경우 또는 문자 앞에 공백이 존재할 경우
                answer += s[i].upper()
            else:
                answer += s[i].lower()

    return answer