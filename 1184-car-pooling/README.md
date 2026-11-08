# 1094. Car Pooling

[LeetCode Problem](https://leetcode.com/problems/car-pooling/)  
**Difficulty:** Medium  
**Pattern:** Difference Array + Prefix Sum

---

## 1. Question

There is a car with `capacity` empty seats. The car only travels east.

You are given `trips`, where `trips[i] = [numPassengers, from, to]` means:
- `numPassengers` passengers get into the car at location `from`.
- Those passengers get out at location `to`.

Passengers are dropped off before new passengers are picked up at the same location.

Return `True` if all trips can be completed without exceeding the car's capacity. Otherwise, return `False`.

## 2. Examples

### Example 1

```python
Input:
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4

Output: False
```

At location 1, two passengers enter. At location 3, three more enter, making five passengers. Since `5 > 4`, capacity is exceeded.

### Example 2

```python
Input:
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5

Output: True
```

The maximum occupancy is 5, which does not exceed the capacity.

## 3. Approach – Difference Array + Prefix Sum

Use a **difference array** to record where the passenger count changes.

For each trip `[passengers, start, end]`:

- Add `passengers` at `start`, because passengers enter there.
- Subtract `passengers` at `end`, because passengers leave there.

```python
diff[start] += passengers
diff[end] -= passengers
```

Then calculate the running (prefix) sum of the difference array. This gives the number of passengers currently in the car at each location.

**Important:** The running sum must be updated using `total += diff[i]`. Writing `total = diff[i]` only reads the change at the current location and forgets all earlier passengers.

At a location where passengers leave and others enter, the negative and positive changes are both applied. This correctly models drop-offs before pickups and checks the occupancy after both events.

## 4. Algorithm

1. Find the maximum destination location.
2. Create a difference array of size `max_location + 1`.
3. For every trip:
   - Add passengers at the pickup location.
   - Subtract passengers at the drop-off location.
4. Initialize `total = 0`.
5. Traverse the difference array from location `0` to `max_location`.
6. Add `diff[i]` to `total`.
7. If `total > capacity`, return `False`.
8. If no location exceeds capacity, return `True`.

## 5. Code

```python
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
```

## 6. Dry Run

Input:

```python
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
```

### Step 1: Build the difference array

For `[2, 1, 5]`:

```text
diff[1] += 2
diff[5] -= 2
```

For `[3, 3, 7]`:

```text
diff[3] += 3
diff[7] -= 3
```

The resulting difference array is:

```text
Location:  0  1  2  3  4  5  6  7
diff:      0  2  0  3  0 -2  0 -3
```

### Step 2: Calculate the running sum

| Location | Change (`diff[i]`) | Passengers in car (`total`) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | +2 | 2 |
| 2 | 0 | 2 |
| 3 | +3 | 5 |
| 4 | 0 | 5 |
| 5 | -2 | 3 |
| 6 | 0 | 3 |
| 7 | -3 | 0 |

At location 3:

```text
total = 2 + 3 = 5
capacity = 4

5 > 4
```

Therefore, return:

```python
False
```

If `capacity = 5`, the maximum occupancy is exactly 5, so the answer is `True`.

## 7. Complexity

Let:
- `m` = number of trips.
- `L` = maximum destination location.

**Time Complexity: `O(m + L)`**
- Finding the maximum location takes `O(m)`.
- Building the difference array takes `O(m)`.
- Calculating the running sum takes `O(L)`.

**Space Complexity: `O(L)`**
- The difference array stores passenger-count changes for each location.

Since the constraints specify `to <= 1000`, this solution is efficient.

## 8. Pattern

**Difference Array + Prefix Sum**

Related problems:
- LeetCode 1109 – Corporate Flight Bookings.
- LeetCode 1094 – Car Pooling.

**Key takeaway:** For a range `[start, end)`, add the value at `start` and subtract it at `end`. A prefix sum reconstructs the value at every position.

Remember:

```python
total += diff[i]
```

Do not use `total = diff[i]`, because that discards all previous changes.
