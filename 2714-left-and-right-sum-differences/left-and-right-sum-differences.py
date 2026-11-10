class Solution:
    def leftRightDifference(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            difference = abs(left_sum - right_sum)
            answer.append(difference)

            left_sum += nums[i]

        return answer
