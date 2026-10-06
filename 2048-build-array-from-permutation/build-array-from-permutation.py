class Solution:
    def buildArray(self, nums):
        result = []

        for i in range(len(nums)):
            result.append(nums[nums[i]])

        return result

        