class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        temp = []
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                nums[k] = nums[i]
                k += 1

        return k
