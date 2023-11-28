def solution(s):
    
    temp = []           # 값을 저장할 빈 스택 생성
    temp.append(s[0])   # 스택에 s의 첫번째 문자열 추가
    
    for i in range(1, len(s)):
        if len(temp) == 0:      # temp가 비어있다면 문자열 추가
            temp.append(s[i])
            continue
        elif temp[-1] == s[i]:    # temp에 넣기 전에 마지막 문자와 비교하여 같으면 temp의 마지막 문자 제거
            temp.pop()
        else:                   # 같지 않으면 temp에 추가
            temp.append(s[i])
    
    print(temp)
    # temp의 길이를 비교하여 0일 경우 1을, 0이 아닐 경우 0을 반환
    if(len(temp) == 0):
        return 1
    else:
        return 0