class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_length = 0
        seen = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in seen:
                max_length = max(max_length, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        return max_length

