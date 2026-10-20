class Solution:
    def minimumSteps(self, s):
        black = 0
        steps = 0

        for ch in s:
            if ch == '1':
                black += 1
            else:
                steps += black

        return steps
 