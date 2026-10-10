class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num

            count += prefix_count.get(prefix_sum - k, 0)

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count

        