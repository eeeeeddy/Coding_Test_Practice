def solution(numbers):
    answer = ''
    
    # numbers의 원소를 문자열로 변경한 후 3번 반복한 후 numbers에 저장
    numbers = [ str(i)*3 for i in numbers ]

    # numbers 문자열을 내림차순으로 정렬
    numbers.sort(reverse=True)
    
    # 문자열을 합치기 위해 3으로 나눈 후 answer에 추가
    for i in numbers:
        answer += i[:len(i)//3]
    
    # numbers의 모든 원소가 0일 경우
    if int(answer) == 0:
        return '0'

    return answer