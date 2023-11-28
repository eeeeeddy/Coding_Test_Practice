def solution(n):
    num = bin(n)[2:]        # n을 2진수로 변환
    cnt = num.count("1")    # "1"의 갯수 카운트
    tmp = 0                 # "1"의 갯수를 저장할 임시 변수
    
    # 임시 변수와 cnt가 같을 때까지 while문 수행
    # 2진수의 덧셈은 10진수로 변환하여 덧셈 수행 후 다시 2진수로 변환
    while cnt != tmp:
        num = int(num, 2) + 1
        num = bin(num)[2:]
        tmp = str(num).count("1")
    
    return int(num, 2)