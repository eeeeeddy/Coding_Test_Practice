def solution(clothes):
    answer = 1
    c = {}

    # key : 의상의 종류, value : [의상의 수, 의상의 이름]인 딕셔너리 생성
    for i in clothes:
        if i[1] not in c:
            c[i[1]] = [1, i[0]]
        else:
            c[i[1]].append(i[0])
            c[i[1]][0] += 1

    # 딕셔너리로 반복문을 수행하면서 answer에 (의상의 수 + 1)를 곱함 -> 약수의 개수를 이용하기 위해서
    for i in c.values():
        answer *= (i[0]+1)

    return answer-1