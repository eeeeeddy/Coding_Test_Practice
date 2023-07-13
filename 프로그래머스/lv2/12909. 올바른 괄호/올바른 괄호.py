from collections import deque

def solution(s):
    answer = True

    # 인덱스 접근 문제 해결을 위해 tmp에 1을 넣은 채로 생성
    tmp = deque([1])

    # 문자열의 첫 문자가 ')'일 경우에는 무조건 올바른 괄호가 형성되지 않으므로 False 리턴
    if s[0] == ')':
        return False

    # 문자열 s의 길이만큼 반복문 수행
    for i in range(len(s)):
        # '(' 일 경우 tmp 스택에 추가
        if s[i] == '(':
            tmp.append(s[i])
        # ')' 일 경우 스택의 마지막 문자가 '('인지 확인 후 맞다면 tmp 스택에서 '('을 pop
        else:
            if tmp[len(tmp)-1] == '(':
                tmp.pop()
            # '(' 일 경우 tmp 스택에 추가
            else:
                tmp.append(s[i])
    
    # 최종적으로 tmp의 길이가 1일 경우 true 리턴 아닐 경우 false 리턴
    if len(tmp) == 1:
        return True
    else:
        return False