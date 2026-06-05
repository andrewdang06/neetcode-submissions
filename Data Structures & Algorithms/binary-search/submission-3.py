class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        found = False

        while l <= r:
            midpoint = (l + r) // 2

            if nums[midpoint] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1

            if nums[midpoint] == target:
                return midpoint
                found = True
        return -1
        