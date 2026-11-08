class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix_sum += 1

            remainder = prefix_sum % modulo
            target = (remainder - k) % modulo

            result += prefix_count.get(target, 0)

            prefix_count[remainder] = prefix_count.get(remainder, 0) + 1

        return result