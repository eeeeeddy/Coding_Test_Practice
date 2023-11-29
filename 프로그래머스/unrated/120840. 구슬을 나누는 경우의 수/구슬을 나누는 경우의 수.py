def solution(balls, share):
    
    B, S = 1, 1
    
    for i in range(1, share+1):
        B *= balls
        S *= share
        balls -= 1
        share -= 1
    
    answer = B // S
    
    return answer