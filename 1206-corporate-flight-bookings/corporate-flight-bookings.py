class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        answer = []
        prefix_sum = 0

        for i in range(n):
            prefix_sum += diff[i]
            answer.append(prefix_sum)

        return answer
