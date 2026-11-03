class Solution:
    def equalSubstring(self, s, t, maxCost):
        left = 0
        total = 0
        max_length = 0

        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            total += cost

            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
