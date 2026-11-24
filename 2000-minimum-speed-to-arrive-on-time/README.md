# 1870. Minimum Speed to Arrive on Time

[LeetCode Problem](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Binary Search
- Binary Search on Answer

---

## 1. Problem Statement

You are given an array `dist`, where `dist[i]` is the distance of the `i`th train ride, and a floating-point number `hour`, representing the maximum time available to reach your destination.

The trains must be taken in order. Each train can depart only at an integer hour, so after every train except the last one, you must wait until the next integer hour if necessary.

Return the **minimum positive integer speed** that allows you to complete all train rides within `hour`. If it is impossible, return `-1`.

The problem guarantees that `hour` has at most two digits after the decimal point and that the answer, if it exists, does not exceed `10^7`.

### Example 1
**Input:**
```python
dist = [1, 3, 2]
hour = 6
```
**Output:**
```python
1
```
At speed `1`, the rides take `1`, `3`, and `2` hours, for a total of `6` hours.

### Example 2
**Input:**
```python
dist = [1, 3, 2]
hour = 2.7
```
**Output:**
```python
3
```
At speed `3`, the first ride takes `1/3` hour but requires waiting until hour `1` for the next departure. The second ride takes `1` hour. The last ride takes `2/3` hour, with no waiting afterward. Total time is approximately `2.66667` hours.

### Example 3
**Input:**
```python
dist = [1, 3, 2]
hour = 1.9
```
**Output:**
```python
-1
```
At least `2` hours are needed before the final train can depart, so arriving within `1.9` hours is impossible.

### Constraints
- `n == dist.length`
- `1 <= n <= 10^5`
- `1 <= dist[i] <= 10^5`
- `1 <= hour <= 10^9`
- `hour` has at most two digits after the decimal point.

---

## 2. Approach: Binary Search on Answer

We need the **minimum speed** that makes the total journey time no greater than `hour`.

Trying every speed from `1` to `10^7` would be too slow. Instead, use binary search on the possible speed.

### Search space
```python
left = 1
right = 10**7
```

The minimum possible speed is `1`, and the problem guarantees that a valid answer will not exceed `10^7`.

### Check whether a speed is valid

For a candidate speed `mid`:
- For every train except the last, calculate the travel time and round it up to the next integer hour.
- For the last train, add its exact travel time because there is no following departure to wait for.

Use integer ceiling division for the earlier trains:

```python
(dist[i] + mid - 1) // mid
```

### Avoid floating-point precision errors

Since `hour` has at most two digits after the decimal point, convert it into an integer number of hundredths:

```python
hour_limit = round(hour * 100)
```

For example, `2.7` becomes `270`, and `2.01` becomes `201`.

Let `total_time` be the integer time used by all trains except the last one. The remaining time, in hundredths of an hour, is:

```python
remaining = hour_limit - total_time * 100
```

The last train fits in the remaining time exactly when:

```python
dist[-1] * 100 <= remaining * mid
```

This compares integers rather than floating-point totals.

### Binary search decisions
- If the candidate speed is valid, save it and search for a smaller speed.
- If it is invalid, search for a larger speed.

---

## 3. Algorithm

1. If `hour <= len(dist) - 1`, return `-1`. The first `n - 1` train rides require at least `n - 1` hours before the final train can depart.
2. Set `left = 1` and `right = 10**7`.
3. Convert the allowed time into hundredths using `hour_limit = round(hour * 100)`.
4. Initialize `ans = -1`.
5. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. Set `total_time = 0`.
   3. For every train except the last, add its rounded-up travel time using integer ceiling division.
   4. Calculate the remaining time in hundredths.
   5. Check whether the last train fits using integer arithmetic.
   6. If the speed is valid, set `ans = mid` and `right = mid - 1`.
   7. Otherwise, set `left = mid + 1`.
6. Return `ans`.

---

## 4. Python Code

This integer-arithmetic version avoids floating-point precision issues in the feasibility check.

```python
class Solution:
    def minSpeedOnTime(self, dist, hour):
        if hour <= len(dist) - 1:
            return -1

        left = 1
        right = 10 ** 7
        ans = -1

        hour_limit = round(hour * 100)

        while left <= right:
            mid = (left + right) // 2

            total_time = 0

            for i in range(len(dist) - 1):
                total_time += (dist[i] + mid - 1) // mid

            remaining = hour_limit - total_time * 100

            if remaining >= 0 and dist[-1] * 100 <= remaining * mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```

---

## 5. Dry Run

Consider:

```python
dist = [1, 3, 2]
hour = 2.7
```

Convert the allowed time into hundredths:

```text
hour_limit = round(2.7 * 100)
           = 270
```

Try a candidate speed of `3`.

**First train:**
```text
ceil(1 / 3) = 1 hour
```

**Second train:**
```text
ceil(3 / 3) = 1 hour
```

Therefore:

```text
total_time = 1 + 1 = 2 hours
```

Calculate the remaining time:

```text
remaining = 270 - (2 * 100)
          = 70
```

Check whether the last train fits:

```text
dist[-1] * 100 <= remaining * speed

2 * 100 <= 70 * 3

200 <= 210
```

The condition is true, so speed `3` is valid. Binary search continues toward smaller speeds to find the minimum valid speed.

**Output:**
```python
3
```

### Precision edge case

Consider:

```python
dist = [1, 1, 100000]
hour = 2.01
```

The first two trains require `2` hours, leaving `0.01` hours for the last train.

```text
hour_limit = 201
total_time = 2
remaining = 201 - 200 = 1
```

The final-train condition becomes:

```text
100000 * 100 <= 1 * speed
10000000 <= speed
```

Therefore, the minimum speed is:

```python
10000000
```

---

## 6. Why This Works

The feasibility condition is monotonic:
- If a particular speed is sufficient, every higher speed is also sufficient.
- If a particular speed is insufficient, every lower speed is also insufficient.

Therefore, valid speeds form a continuous range at the high end of the search space. Binary search can find the first valid speed.

For each candidate speed, the first `n - 1` train rides are rounded up because the next train can depart only at an integer hour. The last ride is not rounded because no further departure is needed.

The integer comparison checks the last ride against the exact remaining time in hundredths of an hour. Thus, the feasibility check avoids floating-point comparison errors.

---

## 7. Complexity Analysis

Let `n` be the number of train rides and `S = 10^7` be the maximum speed searched.

| Operation | Time Complexity |
|---|---|
| Binary search over speeds | `O(log S)` |
| Check one candidate speed | `O(n)` |
| Complete algorithm | `O(n log S)` |

**Total Time Complexity:**
```text
O(n log 10^7)
```

**Auxiliary Space Complexity:**
```text
O(1)
```

Only a constant number of variables are used. The input array is not copied or modified.

---

## 8. Pattern and Related Problems

**Pattern: Binary Search on Answer**

Recognize this pattern when:
- The problem asks for the minimum speed, capacity, rate, or time.
- You can check whether a proposed answer is feasible.
- Feasibility is monotonic: once an answer works, larger values also work.
- You need the smallest feasible value.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Koko Eating Bananas | 875 | Binary Search on Answer |
| Capacity To Ship Packages Within D Days | 1011 | Binary Search on Answer |
| Minimum Number of Days to Make m Bouquets | 1482 | Binary Search on Answer |
| Magnetic Force Between Two Balls | 1552 | Binary Search on Answer |
| Minimum Speed to Arrive on Time | 1870 | Binary Search on Answer |

### Important lines to remember

**Integer ceiling division:**
```python
(dist[i] + mid - 1) // mid
```

**Convert the time limit to hundredths:**
```python
hour_limit = round(hour * 100)
```

**Check whether the last train fits:**
```python
remaining = hour_limit - total_time * 100

if remaining >= 0 and dist[-1] * 100 <= remaining * mid:
```

**Binary search for the minimum valid speed:**
```python
if valid:
    ans = mid
    right = mid - 1
else:
    left = mid + 1
```
