def solution(n, lost, reserve):
    answer = 0
    arr = []
    
    for i in range(1, n+1):
        if i in lost and i in reserve:  # 여벌의 체육복이 있는 학생이 옷을 도난 당했을 때 -> 1벌
            arr.append([i, 1])
        elif i in lost:                 # 체육복을 도난 당했을 때 -> 0벌
            arr.append([i, 0])
        elif i in reserve:              # 여분의 체육복이 있는 경우 -> 2벌
            arr.append([i, 2])
        else:                           # 그 외의 경우 -> 1벌
            arr.append([i, 1])

    if arr[0][1] == 2:                  # 리스트의 맨 앞이 2벌일 때 그 뒷번호만 생각함
        if arr[1][1] == 0:
            arr[0][1] = 1
            arr[1][1] = 1

    for i in range(1, len(arr)-1):      # 그 사이의 경우 앞에 확인하고 뒤에 확인함
        if arr[i][1] == 2:
            if arr[i-1][1] == 0:
                arr[i][1] = 1
                arr[i-1][1] = 1
            elif arr[i+1][1] == 0:
                arr[i][1] = 1
                arr[i+1][1] = 1

    if arr[len(arr)-1][1] == 2:         # 리스트의 맨 뒤가 2벌일 때 그 앞번호만 생각함
        if arr[len(arr)-2][1] == 0:
            arr[len(arr)-1][1] = 1
            arr[len(arr)-2][1] = 1

    for i in range(len(arr)):           # 리스트를 돌면서 체육복의 갯수가 1 이상일 때만 카운트
        if arr[i][1] >= 1:
            answer += 1

    return answer 