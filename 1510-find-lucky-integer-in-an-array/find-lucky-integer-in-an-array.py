class Solution:
    def findLucky(self, arr):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        result = -1

        for num, freq in count.items():
            if num == freq and num > result:
                result = num

        return result
