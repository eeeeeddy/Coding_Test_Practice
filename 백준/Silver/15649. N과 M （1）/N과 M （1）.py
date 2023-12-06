"""
1. 아이디어
- 백트래킹 재귀 함수 안에서, for 문을 수행하면서 숫자 선택 (이때, 방문 여부 확인)
- 재귀 함수에서 M개를 선택할 경우 print

2. 시간복잡도
- N! : 중복이 불가, N이 10까지 가능

3. 자료구조
- 방문 여부 확인 배열 : bool[]
- 선택한 값 입력 배열 : int[]
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
chk = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num+1)
            chk[i] = False
            result.pop()

recur(0)