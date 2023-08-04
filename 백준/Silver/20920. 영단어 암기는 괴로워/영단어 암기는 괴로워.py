import sys

n, m = map(int, sys.stdin.readline().split())

cnt = []
word_dict = {} # 단어 : [등장 횟수, 단어 길이]

# 배치 기준 우선순위
# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 단어의 길이가 길수록 앞에 배치
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치 (A -> Z 순)

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:                      # 길이가 m 이상인 경우만 딕셔너리에 추가
        if word not in word_dict:           # 단어의 등장 횟수를 세기 위한 조건문
            word_dict[word] = [1]
            word_dict[word].append(len(word))
        else:
            word_dict[word][0] += 1

# x[0]    : 단어
# x[1][0] : 등장 횟수
# x[1][1] : 단어 길이
ans = sorted(word_dict.items(), key = lambda x: (-x[1][0], -x[1][1], x[0]))

for i in range(len(ans)):
    print(ans[i][0])