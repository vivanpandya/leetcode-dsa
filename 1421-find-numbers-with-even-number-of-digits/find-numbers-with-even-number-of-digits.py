class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            digits = 0

            while num > 0:
                num //= 10
                digits += 1

            if digits % 2 == 0:
                count += 1

        return count

        