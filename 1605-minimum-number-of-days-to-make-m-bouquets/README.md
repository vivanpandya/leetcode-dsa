# 1482. Minimum Number of Days to Make m Bouquets

[LeetCode Problem](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Binary Search
- Greedy

---

## 1. Problem Statement

You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.

You want to make `m` bouquets. Each bouquet requires exactly `k` **adjacent flowers**. The `i`th flower blooms on day `bloomDay[i]` and can be used in exactly one bouquet.

Return the **minimum number of days** needed to make `m` bouquets. If it is impossible, return `-1`.

### Example 1

**Input:**
```python
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
```

**Output:**
```python
3
```

**Explanation:**
- After day 1: `[x, _, _, _, _]` — one bouquet.
- After day 2: `[x, _, _, _, x]` — two bouquets.
- After day 3: `[x, _, x, _, x]` — three bouquets.

The minimum number of days is `3`.

### Example 2

**Input:**
```python
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
```

**Output:**
```python
-1
```

**Explanation:** We need `3 * 2 = 6` flowers, but there are only 5.

### Example 3

**Input:**
```python
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
```

**Output:**
```python
12
```

**Explanation:**
- After day 7: `[x, x, x, x, _, x, x]`. Only one bouquet of three adjacent flowers can be made.
- After day 12: all flowers have bloomed, so two bouquets can be made.

### Constraints
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`

---

## 2. Approach: Binary Search on Answer + Greedy

We need the **minimum day** on which at least `m` bouquets can be made.

Instead of checking every day, use binary search over the possible answer.

### Step 1: Check whether making the bouquets is possible

Each bouquet needs `k` flowers, and we need `m` bouquets. Therefore, the total number of flowers required is `m * k`.

```python
if m * k > len(bloomDay):
    return -1
```

If the required number is greater than the number of flowers available, return `-1`.

### Step 2: Set the binary search range

The earliest possible day is the minimum bloom day. The latest possible day is the maximum bloom day.

```python
left = min(bloomDay)
right = max(bloomDay)
```

### Step 3: Check whether a candidate day works

For a candidate day `mid`, a flower is bloomed if:

```python
day <= mid
```

Traverse the array and maintain:
- `count`: number of consecutive bloomed flowers in the current group.
- `bouquets`: number of bouquets made so far.

When `count` reaches `k`, make one bouquet and reset `count` to zero. This ensures that no flower is reused.

If a flower has not bloomed, reset `count` to zero because the consecutive sequence is broken.

### Step 4: Adjust binary search

- If `bouquets >= m`, the candidate day works. Save it and search for an earlier day.
- Otherwise, more days are needed, so search to the right.

---

## 3. Algorithm

1. If `m * k > len(bloomDay)`, return `-1`.
2. Set `left = min(bloomDay)` and `right = max(bloomDay)`.
3. Initialize `ans = -1`.
4. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. Set `bouquets = 0` and `count = 0`.
   3. Traverse each `day` in `bloomDay`:
      - If `day <= mid`, increment `count`.
      - If `count == k`, increment `bouquets` and reset `count = 0`.
      - Otherwise, reset `count = 0` because the flower has not bloomed.
   4. If `bouquets >= m`, save `mid` as the answer and set `right = mid - 1`.
   5. Otherwise, set `left = mid + 1`.
5. Return `ans`.

---

## 4. Python Code

```python
class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            bouquets = 0
            count = 0

            for day in bloomDay:
                if day <= mid:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            if bouquets >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```

---

## 5. Dry Run

**Input:**
```python
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
```

First, check whether enough flowers exist:

```text
m * k = 3 * 1 = 3
n = 5
```

Since `3 <= 5`, making the bouquets is possible.

Initial range:

```text
left = 1
right = 10
ans = -1
```

### Iteration 1

```text
mid = (1 + 10) // 2 = 5
```

By day 5:

| Flower bloom day | Bloomed by day 5? | Bouquets made |
|---:|---|---:|
| 1 | Yes | 1 |
| 10 | No | 1 |
| 3 | Yes | 2 |
| 10 | No | 2 |
| 2 | Yes | 3 |

We can make 3 bouquets.

```text
ans = 5
right = 4
```

### Iteration 2

```text
mid = (1 + 4) // 2 = 2
```

By day 2:

```text
bloomDay = [1, 10, 3, 10, 2]
bloomed  = [x, _, _, _, x]
```

Only 2 bouquets can be made. We need 3.

```text
left = 3
```

### Iteration 3

```text
mid = (3 + 4) // 2 = 3
```

By day 3:

```text
bloomed = [x, _, x, _, x]
```

We can make 3 bouquets.

```text
ans = 3
right = 2
```

Now `left > right`, so binary search stops.

**Final Output:**
```python
3
```

### Dry Run Summary

| Iteration | Left | Right | Mid | Bouquets possible | Decision |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 10 | 5 | 3 | Save answer; search left |
| 2 | 1 | 4 | 2 | 2 | Search right |
| 3 | 3 | 4 | 3 | 3 | Save answer; search left |

---

## 6. Why This Works

For a fixed day, the greedy traversal makes a bouquet as soon as it finds `k` consecutive bloomed flowers. It resets the counter after using those flowers, so no flower is reused.

Feasibility is monotonic: if we can make the required bouquets on a particular day, we can also make them on every later day because flowers remain bloomed.

Therefore, binary search can find the **first feasible day**, which is the minimum number of days required.

---

## 7. Complexity Analysis

Let:
- `n` = number of flowers.
- `D = max(bloomDay) - min(bloomDay) + 1` = size of the candidate-day range.

| Operation | Time Complexity |
|---|---|
| Check `m * k > n` | `O(1)` |
| Find minimum and maximum bloom days | `O(n)` |
| Check one candidate day | `O(n)` |
| Binary search iterations | `O(log D)` |

**Total Time Complexity:**

```text
O(n * log D)
```

Equivalently:

```text
O(n * log(max(bloomDay) - min(bloomDay) + 1))
```

**Space Complexity:**

```text
O(1)
```

Only a constant number of variables are used. The input array is not modified.

---

## 8. Pattern and Related Problems

**Main Pattern: Binary Search on Answer + Greedy**

Recognize this pattern when:
- The problem asks for a minimum or maximum possible value.
- You can check whether a candidate answer is feasible.
- If a candidate day is feasible, all later days are also feasible.
- You need to find the first feasible value.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Koko Eating Bananas | 875 | Binary Search on Answer |
| Capacity To Ship Packages Within D Days | 1011 | Binary Search on Answer |
| Minimum Speed to Arrive on Time | 1870 | Binary Search on Answer |
| Magnetic Force Between Two Balls | 1552 | Binary Search on Answer |
| Split Array Largest Sum | 410 | Binary Search on Answer |

### Important Lines to Remember

**1. Impossible case**
```python
if m * k > len(bloomDay):
    return -1
```

**2. Check whether a flower has bloomed**
```python
if day <= mid:
    count += 1
```

**3. Make a bouquet when we have `k` adjacent flowers**
```python
if count == k:
    bouquets += 1
    count = 0
```

**4. Find the minimum feasible day**
```python
if bouquets >= m:
    ans = mid
    right = mid - 1
else:
    left = mid + 1
```

**Key takeaway:** Binary search chooses the candidate day, and greedy counting checks how many bouquets can be made on that day.
