def solution(brown, yellow):
    answer = []
    y = [] # yellow가 가능한 [가로, 세로]를 저장할 리스트 변수

    # yellow가 가능한 배치를 확인하기 위해 yellow의 약수를 구하는 과정
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if i >= (yellow//i): # 가로 >= 세로인 경우만 y 리스트에 추가
                y.append([i, yellow//i])

    # y 리스트에 대해 반복문을 수행하면서 brown의 값으로 카펫 구성이 가능한지 확인
    for i in y:
        if brown == ((i[0]+2 + i[1]) * 2):
            answer.append([i[0]+2, i[1]+2])

    return answer[0]