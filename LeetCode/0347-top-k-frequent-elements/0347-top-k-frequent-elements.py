class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []

         # nums를 set으로 만들어 중복을 제거해준다.
        unique_nums = list(set(nums))    

        # 갯수를 담을 변수 count 생성
        count = [0 for i in range(len(unique_nums))]

        # set의 원소별로 nums에 있는 갯수를 구해 count에 추가
        for i in range(len(unique_nums)):
            count[i] = nums.count(unique_nums[i])

        # unique_nums와 count를 합쳐 딕셔너리로 생성
        tmp = dict(zip(unique_nums, count))

        # 딕셔너리 tmp를 갯수(count)값으로 내림차순
        tmp = sorted(tmp.items(), key = lambda item: item[1], reverse=True)

        # 딕셔너리의 key값을 answer에 추가 - key가 nums의 값임.
        for i in tmp:
            answer.append(i[0])

        # k개 만큼 출력
        return answer[:k] 
