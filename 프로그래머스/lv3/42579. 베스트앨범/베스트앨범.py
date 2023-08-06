def solution(genres, plays):
    answer = []
    dic = {}
    temp = list(zip(genres, plays))

# 수록 기준
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

    for i in range(len(temp)):
        if temp[i][0] not in dic:
            dic[temp[i][0]] = [[temp[i][1], i]]
        else:
            dic[temp[i][0]].append([temp[i][1], i]) # dic = {장르 : [재생횟수, 인덱스]}

    for i in dic:
        total = 0
        dic[i].sort(key=lambda x: (-x[0], x[1]))    # 2번, 3번 기준 만족
        for j in dic[i]:
            total += j[0]                           # 총 재생횟수로 정렬하기 위해 total 값 계산

        dic[i].append(total)                        # # dic[장르] 값에 총 재생횟수를 추가

    dic = sorted(dic.items(), key=lambda x: (-x[1][-1])) # 총 재생횟수로 내림차순

    for i in range(len(dic)): # 노래를 수록하기 위해 장르별 2곡씩 선정
        count = 0
        while count < 2:
            if len(dic[i][1]) == 2: # 장르에 속한 곡이 1곡일 경우 처리하기위한 코드
                answer.append(dic[i][1][count][1])
                break
            answer.append(dic[i][1][count][1])
            count += 1
    
    return answer