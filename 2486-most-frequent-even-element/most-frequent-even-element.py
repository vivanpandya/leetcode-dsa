class Solution:
    def mostFrequentEven(self, nums):
        count = {}

        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1

        result = -1
        max_freq = 0

        for num, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                result = num
            elif freq == max_freq and num < result:
                result = num

        return result
