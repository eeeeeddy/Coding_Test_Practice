def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        elif citations[i] == i+1:
            return i+1
        
    return len(citations)