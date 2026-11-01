class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        satisfied = 0
        extra = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        for i in range(minutes):
            if grumpy[i] ==  1:
                extra += customers[i]

        max_extra = extra

        for right in range(minutes, len(customers)):
            if grumpy[right] == 1:
                extra += customers[right]
            
            if grumpy[right - minutes] == 1:
                extra -= customers[right - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra


        