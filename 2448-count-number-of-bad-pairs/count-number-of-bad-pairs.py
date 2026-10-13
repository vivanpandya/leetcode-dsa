class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        total_pairs = n * (n - 1) // 2

        count = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i

            good_pairs += count.get(key, 0)
            count[key] = count.get(key, 0) + 1

        return total_pairs - good_pairs