class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        pairs = 0

        for num in nums:
            pairs += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return pairs
