def solution(wallpaper):
    lux, luy, rdx, rdy, cnt = 0, 0, 0, 0, 0 # 시작 x, 시작 y, 끝 x, 끝 y, 카운트변수

    for i in range(len(wallpaper)): # 세로길이
        for j in range(len(wallpaper[i])): # 가로길이
            if wallpaper[i][j] == '#' and cnt == 0: # 카운트 변수를 통해 시작점 설정
                lux, luy, rdx, rdy, cnt = i, j, i+1, j+1, 1
            elif wallpaper[i][j] == '#': # 시작점 이후 파일을 만나면 범위 축소
                if i <= lux:
                    lux = i
                if j <= luy:
                    luy = j
                if i+1 >= rdx:
                    rdx = i+1
                if j+1 >= rdy:
                    rdy = j+1
    
    answer = [lux, luy, rdx, rdy]

    return answer