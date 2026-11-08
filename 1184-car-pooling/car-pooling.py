class Solution:
    def carPooling(self, trips, capacity):
        max_location = 0

        for passengers, start, end in trips:
            max_location = max(max_location, end)

        diff = [0] * (max_location + 1)

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        total = 0

        for i in range(max_location + 1):
            total += diff[i]

            if total > capacity:
                return False

        return True