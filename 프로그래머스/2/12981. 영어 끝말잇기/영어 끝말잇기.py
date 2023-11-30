import math

def solution(n, words):
    answer = [0, 0] # 번호, 차례
    temp = [] # 같은 단어가 2번 등장하는지 검사하기위한 리스트
    temp.append(words[0])
    
    for i in range(1, len(words)):
        temp.append(words[i])

        # 앞 단어의 마지막 글자와 뒷 단어의 첫 번째 글자가 같은 지 검사
        # 같은 단어가 2번 등장했는 지 검사
        if words[i-1][-1] != words[i][0] or temp.count(words[i]) == 2:
            if (i+1) % n == 0:
                answer[0] += n
                answer[1] += (i+1) // n
            else:
                answer[0] += (i+1) % n
                answer[1] += math.trunc((i+1) / n + 1)
            break

    return answer