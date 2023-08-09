class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 입력 배열을 오름차순으로 정렬합니다.
        result = []  # 결과를 담을 리스트를 초기화합니다.

        for i in range(len(nums) - 2):  # 첫 번째 숫자를 선택합니다. 마지막에서 두 번째까지만 반복합니다.
            if i > 0 and nums[i] == nums[i-1]:  # 중복된 첫 번째 숫자는 건너뜁니다.
                continue

            left, right = i + 1, len(nums) - 1  # 두 번째 숫자와 세 번째 숫자를 선택할 인덱스를 지정합니다.

            while left < right:  # 두 번째 숫자와 세 번째 숫자가 만날 때까지 반복합니다.
                total = nums[i] + nums[left] + nums[right]  # 세 숫자의 합을 계산합니다.

                if total < 0:  # 합이 0보다 작으면 두 번째 숫자를 오른쪽으로 이동합니다.
                    left += 1
                elif total > 0:  # 합이 0보다 크면 세 번째 숫자를 왼쪽으로 이동합니다.
                    right -= 1
                else:  # 합이 0이면 세 숫자를 결과 리스트에 추가합니다.
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:  # 중복된 두 번째 숫자는 건너뜁니다.
                        left += 1
                    # while left < right and nums[right] == nums[right-1]:  # 중복된 세 번째 숫자는 건너뜁니다.
                    #     right -= 1
                    left += 1  # 두 번째 숫자를 오른쪽으로 이동합니다.
                    right -= 1  # 세 번째 숫자를 왼쪽으로 이동합니다.

        return result  # 결과 리스트를 반환합니다.