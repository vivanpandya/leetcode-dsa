class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()

        result = []

        for spell in spells:
            required = (success + spell - 1) // spell

            left = 0
            right = len(potions)

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= required:
                    right = mid
                else:
                    left = mid + 1

            count = len(potions) - left
            result.append(count)

        return result