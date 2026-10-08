class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[]for _ in range(len(nums) + 1)]

        for num, frq in count.items():
            buckets[frq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

            if len(result) == k:
                return result

        