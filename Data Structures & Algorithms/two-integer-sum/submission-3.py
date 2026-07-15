class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionar = {}
        for i, num in enumerate(nums):
            d = target - num
            if d in dictionar:
                return [dictionar[d], i]
            dictionar[num] = i
        return []