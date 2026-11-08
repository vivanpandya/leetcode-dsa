class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            count += prefix_count.get(remainder, 0)

            prefix_count[remainder] = prefix_count.get(remainder, 0) + 1

        return count
