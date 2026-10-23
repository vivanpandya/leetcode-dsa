class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        count_p = {}
        window = {}

        for ch in p:
            count_p[ch] = count_p.get(ch, 0) + 1

        for ch in s[:len(p)]:
            window[ch] = window.get(ch, 0) + 1

        result = []

        if count_p == window:
            result.append(0)

        for right in range(len(p), len(s)):
            new_char = s[right]
            old_char = s[right - len(p)]
 
            window[new_char] = window.get(new_char, 0) + 1

            window[old_char] -= 1

            if window[old_char] == 0:
                del window[old_char]

            if count_p == window:
                result.append(right - len(p) + 1)

        return result

        

        