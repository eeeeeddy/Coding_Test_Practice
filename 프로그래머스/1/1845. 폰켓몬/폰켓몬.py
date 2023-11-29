def solution(nums):
    answer = 0
    pokemon = {}

    # key : 포켓몬 번호, value : 해당 번호를 가진 포켓몬 수
    for i in nums:
        if i not in pokemon:
            pokemon[i] = 1
        else:
            pokemon[i] += 1

    if len(nums)//2 < len(pokemon):
        return len(nums)//2
    else:
        return len(pokemon)