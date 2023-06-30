def solution(array):

    arraySet = set(array)
    arrayList = list(arraySet)
    modeList = []

    for i in arraySet:
        modeList.append(array.count(i))

    mode = max(modeList)
    modeIndex = modeList.index(mode)

    for i in modeList:
        if modeList.count(mode) >= 2:
            answer = -1
        else:
            answer = arrayList[modeIndex]
    
    return answer