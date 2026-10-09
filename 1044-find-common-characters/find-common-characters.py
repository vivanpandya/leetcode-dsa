class Solution:
    def commonChars(self, words):
        common = {}

        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1

        for word in words[1:]:
            count = {}

            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            for ch in common:
                common[ch] = min(common[ch], count.get(ch, 0))

        result = []

        for ch, freq in common.items():
            for _ in range(freq):
                result.append(ch)

        return result
