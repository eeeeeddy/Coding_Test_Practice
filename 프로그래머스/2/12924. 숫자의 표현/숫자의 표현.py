def solution(n):
    answer = 0

    for i in range(1, n+1):
        sum = 0 # n까지의 연속된 자연수의 합을 관리하기 위한 변수
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
            elif sum > n:
                break

    return answer