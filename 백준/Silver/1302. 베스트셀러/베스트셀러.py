n = int(input())

books = {}

# 딕셔너리로 {책 제목 : 팔린 수} 저장
# 딕셔너리에 없으면 추가하면서 팔린 횟수 1로, 그 이후 등장 시 딕셔너리에 있다면 value에 1을 더해줌
for i in range(n):
    title = input()
    if title not in books:
        books[title] = 1
    else:
        books[title] += 1

# 책 제목은 사전순으로, 팔린 횟수는 내림차순으로 정렬
ans = sorted(books.items(), key = lambda x: (-x[1], x[0]))

print(ans[0][0])