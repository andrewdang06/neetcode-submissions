class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}

        for i, val in enumerate(nums):
            comp = target - val

            if comp in hashy:
                return [hashy[comp], i]
            
            hashy[val] = i
        return False