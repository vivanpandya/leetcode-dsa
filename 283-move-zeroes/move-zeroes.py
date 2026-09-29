class Solution:
    def moveZeroes(self, nums):
        index = 0

        for num in nums:
            if num != 0:
                nums[index] = num 
                index += 1

        while index < len (nums):
            nums[index] = 0
            index += 1
        