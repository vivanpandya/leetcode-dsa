class Solution:
    def platesBetweenCandles(self, s, queries):
        n = len(s)

        prefix = [0] * (n + 1)
        left = [-1] * n
        right = [-1] * n

        for i in range(n):
            prefix[i + 1] = prefix[i]

            if s[i] == '*':
                prefix[i + 1] += 1

        last = -1

        for i in range(n):
            if s[i] == '|':
                last = i
            left[i] = last

        last = -1

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i
            right[i] = last

        answer = []

        for l, r in queries:
            start = right[l]
            end = left[r]

            if start != -1 and end != -1 and start < end:
                answer.append(prefix[end] - prefix[start])
            else:
                answer.append(0)

        return answer