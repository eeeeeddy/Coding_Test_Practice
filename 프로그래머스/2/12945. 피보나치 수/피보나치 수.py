def solution(n):
    return fib(n)[n-1] % 1234567

# n번째 피보나치 수를 구하는 함수 (동적 계획법 이용)
def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList