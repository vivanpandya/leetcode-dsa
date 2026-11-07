# 1109. Corporate Flight Bookings

[LeetCode Problem](https://leetcode.com/problems/corporate-flight-bookings/)  
**Difficulty:** Medium  
**Pattern:** Difference Array + Prefix Sum

---

## Problem Statement

There are `n` flights numbered from `1` to `n`.

You are given `bookings`, where each booking is:

```text
[first, last, seats]
```

This means `seats` seats are reserved for every flight from `first` to `last`, inclusive.

Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i` (flight numbering in the problem starts at `1`).

## Examples

### Example 1

```text
Input:  bookings = [[1,2,10], [2,3,20], [2,5,25]], n = 5
Output: [10, 55, 45, 25, 25]
```

Explanation:

| Flight | Booking 1 | Booking 2 | Booking 3 | Total |
|---:|---:|---:|---:|---:|
| 1 | 10 | 0 | 0 | 10 |
| 2 | 10 | 20 | 25 | 55 |
| 3 | 0 | 20 | 25 | 45 |
| 4 | 0 | 0 | 25 | 25 |
| 5 | 0 | 0 | 25 | 25 |

### Example 2

```text
Input:  bookings = [[1,2,10], [2,2,15]], n = 2
Output: [10, 25]
```

Explanation:
- Flight 1 receives 10 seats.
- Flight 2 receives 10 + 15 = 25 seats.

## Constraints

- `1 <= n <= 2 * 10^4`
- `1 <= bookings.length <= 2 * 10^4`
- `bookings[i].length == 3`
- `1 <= first_i <= last_i <= n`
- `1 <= seats_i <= 10^4`

---

## Approach: Difference Array + Prefix Sum

A straightforward approach is to add the seats to every flight in each booking range. However, that can take `O(n * m)` time, where `m` is the number of bookings.

We can do better using a **difference array**.

Instead of updating every flight between `first` and `last`, we make only two updates:

- Add `seats` at the beginning of the range.
- Subtract `seats` immediately after the end of the range.

The prefix sum of these updates reconstructs the total seats for every flight.

### Why do we subtract at `last + 1`?

A booking affects flights from `first` through `last`, inclusive.

- At `first`, the booking starts contributing `seats`.
- At `last + 1`, the booking stops contributing, so we subtract `seats`.

We use a difference array of size `n + 1` so that the update at index `n` is safe when a booking ends at the final flight.

### Flight numbering and Python indexing

The problem labels flights from `1` to `n`, but Python arrays use indices from `0` to `n - 1`.

For a booking `[first, last, seats]`, the corresponding difference-array updates are:

```python
diff[first - 1] += seats
diff[last] -= seats
```

The final prefix sum at Python index `i` gives the answer for flight `i + 1`.

## Algorithm

1. Create a difference array `diff` of size `n + 1`, initialized with zeros.
2. For every booking `[first, last, seats]`:
   - Add `seats` at `diff[first - 1]`.
   - Subtract `seats` at `diff[last]`.
3. Create an empty result array and set `total = 0`.
4. Traverse the first `n` positions of `diff`:
   - Add `diff[i]` to `total`.
   - Append `total` to the result.
5. Return the result.

## Python Code

```python
class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        result = []
        total = 0

        for i in range(n):
            total += diff[i]
            result.append(total)

        return result
```

## Dry Run

Input:

```python
bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
```

### Step 1: Initialize the difference array

```text
diff = [0, 0, 0, 0, 0, 0]
```

There are `n + 1` positions to allow an update at index `n`.

### Step 2: Process each booking

**Booking 1: `[1, 2, 10]`**

```text
diff[0] += 10
diff[2] -= 10

diff = [10, 0, -10, 0, 0, 0]
```

**Booking 2: `[2, 3, 20]`**

```text
diff[1] += 20
diff[3] -= 20

diff = [10, 20, -10, -20, 0, 0]
```

**Booking 3: `[2, 5, 25]`**

```text
diff[1] += 25
diff[5] -= 25

diff = [10, 45, -10, -20, 0, -25]
```

Final difference array:

```text
[10, 45, -10, -20, 0, -25]
```

### Step 3: Calculate the prefix sum

Start with `total = 0`.

| Python index `i` | `diff[i]` | Running `total` | Flight number |
|---:|---:|---:|---:|
| 0 | 10 | 10 | 1 |
| 1 | 45 | 55 | 2 |
| 2 | -10 | 45 | 3 |
| 3 | -20 | 25 | 4 |
| 4 | 0 | 25 | 5 |

The result is:

```text
[10, 55, 45, 25, 25]
```

## Why This Works

For every booking, the difference array records exactly where its contribution starts and where it stops.

Taking the prefix sum applies each starting contribution to all positions in its range. The subtraction at `last` cancels that contribution beginning with the first position after the booking ends.

After processing all bookings, the running prefix sum at each flight is therefore the sum of all seats booked for that flight.

## Complexity Analysis

Let:
- `n` = number of flights
- `m` = number of bookings

| Complexity | Value | Reason |
|---|---|---|
| Time | `O(n + m)` | Process every booking once, then traverse the flights once |
| Space | `O(n)` | Difference array and result array |

## Pattern

**Difference Array + Prefix Sum**

Use this pattern when:
- Many operations add a value to a continuous range.
- You need the final value at every index after all range updates.
- Updating every element in every range would be too slow.

**Key takeaway:** For a range update `[left, right]` by `value`, add at the start and subtract immediately after the end. A prefix sum reconstructs the final array efficiently.
