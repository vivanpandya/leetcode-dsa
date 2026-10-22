class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)

        if k > len(s2):
            return False

        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        for ch in s2[:k]:
            count2[ch] = count2.get(ch, 0) + 1

        if count1 == count2:
            return True

        for i in range(k, len(s2)):
            new_char = s2[i]
            old_char = s2[i - k]

            count2[new_char] = count2.get(new_char, 0) + 1

            count2[old_char] -= 1
            if count2[old_char] == 0:
                del count2[old_char]

            if count1 == count2:
                return True

        return False
