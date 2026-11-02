class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        window = 0

        if k > 0:
            for i in range(1, k + 1):
                window += code[i % n]

            for i in range(n):
                result[i] = window

                window -= code[(i + 1) % n]
                window += code[(i + k + 1) % n]

        else:
            k = -k

            for i in range(1, k + 1):
                window += code[-i]

            for i in range(n):
                result[i] = window

                window -= code[(i - k) % n]
                window += code[i]

        return result
