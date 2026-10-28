class Solution:
    def numSubarraysWithSum(self, nums, goal):

        def atMost(k):
            if k < 0:
                return 0

            left = 0
            current_sum = 0
            count = 0

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)


