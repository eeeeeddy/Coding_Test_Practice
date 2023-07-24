tc = int(input())

for i in range(tc):
    
    clothes = {}                        # 딕셔너리 생성을 위한 변수 생성 
    answer = 1                          # 곱셈 연산을 위한 변수 생성

    n = int(input())
    
    for i in range(n):
        a, b = input().split()          # 입력받은 옷, 옷의 종류 변수 저장
        if b in clothes.keys():         # 옷의 종류가 딕셔너리에 있을 경우
            clothes[b] += 1             # 해당 옷의 종류에 대해 갯수 + 1
        else:                           # 옷의 종류가 딕셔너리에 없다면
            clothes[b] = 2              # 해당 옷의 종류에 대해 갯수를 2로 지정
            
    for i in list(clothes.values()):    # 딕셔너리의 value를 list로 뽑아서 원소끼리 곱셈 수행
        answer *= i
    
    print(answer-1)
