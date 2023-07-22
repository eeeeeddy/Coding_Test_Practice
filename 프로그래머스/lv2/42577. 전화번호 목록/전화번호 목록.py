def solution(phone_book):

    # phone_book 정렬 -> 숫자로 된 문자열의 정렬은 사전식을 따른다.
    # ["1", "2", "3", "10"] -> ["1", "10", "2", "3"]
    phone_book.sort()

    # 반복문을 수행하면서 현재 번호와 다음 번호만 접두사 비교를 해줌 -> 하나라도 겹치면 False를 반환하기 때문에 가능
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True