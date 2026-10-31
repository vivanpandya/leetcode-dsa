class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_vowels = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1

            if s[right - k] in vowels:
                count -= 1

            max_vowels = max(max_vowels, count)

        return max_vowels
