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

# 여기서 해당 옷의 종류가 딕셔너리가 없을 때 개수에 대해 2로 지정해주는 이유는 
# 나중에 경우의 수를 뽑기 위해서는 각 옷의 종류 별로 (개수+1) 을 하여 
# 종류 별로 곱셈을 해주고 나온 결과에 1을 빼주어야 하기 때문에 초기 값을 2로 세팅해주었다.
