from collections import deque

def solution(board, moves):

    answer, m = 0, 0
    tmp = deque()

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                tmp.append(board[j][i-1])
                if len(tmp) >= 2:
                    if tmp[len(tmp)-2] == tmp[len(tmp)-1]:
                        tmp.pop()
                        tmp.pop()
                        answer += 2
                board[j][i-1] = 0
                break
        
    return answer