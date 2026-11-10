class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        balls = 0
        operations = 0

        for i in range(n):
            answer[i] += operations

            if boxes[i] == '1':
                balls += 1

            operations += balls

        balls = 0
        operations = 0

        for i in range(n - 1, -1, -1):
            answer[i] += operations

            if boxes[i] == '1':
                balls += 1

            operations += balls

        return answer