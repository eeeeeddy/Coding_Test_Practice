def solution(citations):

    # citations 내림차순으로 정렬
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:    # 논문의 인용수가 논문수보다 작아질 때
            return i
        elif citations[i] == i + 1: # 논문의 인용수와 논문수가 같을 때
            return i + 1
        
    return len(citations)            # 논문의 인용수와 논문수가 같거나 작아지지 않을 때
