# 875. Koko Eating Bananas

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/koko-eating-bananas/)

- **LeetCode:** [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- **Problem Number:** 875
- **Difficulty:** Medium
- **Topics:** Array, Binary Search

---

## 1. Problem Statement

Koko has `n` piles of bananas. The `i-th` pile contains `piles[i]` bananas, and the guards will return in `h` hours.

Koko chooses an integer eating speed `k` bananas per hour.

- Each hour, she chooses one pile.
- She eats up to `k` bananas from that pile.
- If the pile has fewer than `k` bananas, she eats all of them.
- She cannot eat from another pile during that same hour.

Return the **minimum integer speed `k`** that lets Koko finish all bananas within `h` hours.

## 2. Examples

### Example 1

```text
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
```

At speed 4, the piles take 1, 2, 2, and 3 hours respectively: 8 hours total.

### Example 2

```text
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

Koko must finish each pile in one hour, so the minimum speed is the largest pile size, 30.

### Example 3

```text
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

At speed 23, Koko takes 2 hours for the first pile and 1 hour for each remaining pile: 6 hours total.

## 3. Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## 4. Approach: Binary Search on Answer

We are not searching for an element in the array. We are searching for the **minimum eating speed** that satisfies the time limit. This technique is called **Binary Search on Answer**.

### Step 1: Define the search range

The minimum possible speed is 1 banana per hour:

```python
left = 1
```

The maximum useful speed is the size of the largest pile:

```python
right = max(piles)
```

At speed `max(piles)`, Koko can finish every pile in one hour. Therefore, the answer lies between `1` and `max(piles)`.

### Step 2: Calculate a candidate speed

```python
mid = (left + right) // 2
```

Treat `mid` as the candidate eating speed.

### Step 3: Calculate the hours required

For a pile containing `pile` bananas, the hours required at speed `mid` are:

\[
\left\lceil \frac{pile}{mid} \right\rceil
\]

In Python, use integer ceiling division:

```python
(pile + mid - 1) // mid
```

For example, a pile of 11 bananas at speed 4 takes:

```python
(11 + 4 - 1) // 4  # 3 hours
```

Calculate the total:

```python
hours_needed = 0

for pile in piles:
    hours_needed += (pile + mid - 1) // mid
```

### Step 4: Check whether the speed works

**Case 1: `hours_needed <= h`**

Koko can finish within the deadline. The speed works, but we want the minimum speed, so try a smaller one:

```python
right = mid
```

**Case 2: `hours_needed > h`**

Koko cannot finish in time. She needs a faster speed:

```python
left = mid + 1
```

Continue until `left == right`. That is the minimum valid speed.

---

## 5. Algorithm

1. Set `left = 1`.
2. Set `right = max(piles)`.
3. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - Set `hours_needed = 0`.
   - For each pile, add `(pile + mid - 1) // mid` to `hours_needed`.
   - If `hours_needed <= h`, set `right = mid`.
   - Otherwise, set `left = mid + 1`.
4. Return `left`.

---

## 6. Python Solution

```python
class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours_needed = 0

            for pile in piles:
                hours_needed += (pile + mid - 1) // mid

            if hours_needed <= h:
                right = mid
            else:
                left = mid + 1

        return left
```

### Code Explanation

| Code | Purpose |
|---|---|
| `left = 1` | Minimum possible eating speed |
| `right = max(piles)` | Maximum useful eating speed |
| `mid = (left + right) // 2` | Candidate eating speed |
| `hours_needed = 0` | Track total hours required |
| `(pile + mid - 1) // mid` | Calculate hours for one pile using ceiling division |
| `hours_needed <= h` | Check whether Koko finishes within the deadline |
| `right = mid` | Candidate works; try a smaller speed |
| `left = mid + 1` | Candidate is too slow; try a larger speed |
| `return left` | Return the minimum valid speed |

---

## 7. Dry Run

Consider Example 1:

```python
piles = [3, 6, 7, 11]
h = 8
```

Initial range:

```text
left = 1
right = 11
```

### Iteration 1

```python
mid = (1 + 11) // 2  # 6
```

| Pile | Hours at speed 6 |
|---:|---:|
| 3 | 1 |
| 6 | 1 |
| 7 | 2 |
| 11 | 2 |
| **Total** | **6** |

Since `6 <= 8`, speed 6 works:

```python
right = 6
```

### Iteration 2

```python
mid = (1 + 6) // 2  # 3
```

| Pile | Hours at speed 3 |
|---:|---:|
| 3 | 1 |
| 6 | 2 |
| 7 | 3 |
| 11 | 4 |
| **Total** | **10** |

Since `10 > 8`, speed 3 is too slow:

```python
left = 4
```

### Iteration 3

```python
mid = (4 + 6) // 2  # 5
```

| Pile | Hours at speed 5 |
|---:|---:|
| 3 | 1 |
| 6 | 2 |
| 7 | 2 |
| 11 | 3 |
| **Total** | **8** |

Since `8 <= 8`, speed 5 works:

```python
right = 5
```

### Iteration 4

```python
mid = (4 + 5) // 2  # 4
```

| Pile | Hours at speed 4 |
|---:|---:|
| 3 | 1 |
| 6 | 2 |
| 7 | 2 |
| 11 | 3 |
| **Total** | **8** |

Since `8 <= 8`, speed 4 works:

```python
right = 4
```

Now:

```text
left = 4
right = 4
```

The loop stops. Return `4`.

**Output:**

```text
4
```

---

## 8. Why This Works

The required number of hours never increases when the eating speed increases.

- If a speed is too slow, every smaller speed will also be too slow.
- If a speed is fast enough, every larger speed will also be fast enough.

This creates a monotonic search space: invalid speeds come before valid speeds.

Binary search finds the first valid speed:

- When the candidate works, keep it as a possible answer and search smaller speeds.
- When it fails, discard it and all smaller speeds.

When the search boundaries meet, they point to the minimum speed that satisfies the deadline.

---

## 9. Complexity Analysis

Let:
- `n` = number of piles.
- `M` = maximum pile size.

### Time Complexity: `O(n log M)`

- The binary search range is from `1` to `M`, requiring `O(log M)` iterations.
- Each iteration visits all `n` piles to calculate the required hours, taking `O(n)` time.

Total:

```text
O(n log M)
```

### Space Complexity: `O(1)`

Only a fixed number of variables are used. No extra array or recursion is needed.

```text
Time:  O(n log M)
Space: O(1)
```

---

## 10. Important Edge Cases

### One pile

```python
piles = [10]
h = 1
```

Output: `10`.

### Plenty of hours

```python
piles = [3, 6, 7, 11]
h = 27
```

There are 4 piles and enough hours to eat one banana per hour.

Output: `1`.

### Number of hours equals number of piles

```python
piles = [30, 11, 23, 4, 20]
h = 5
```

Koko must finish each pile in one hour. The minimum speed is the largest pile:

Output: `30`.

### Very large pile values

The constraints allow pile sizes up to `10^9`. Integer arithmetic avoids floating-point precision issues.

---

## 11. Pattern Recognition: Binary Search on Answer

Recognize this pattern when:
- The problem asks for the minimum or maximum possible value.
- You can test whether a candidate answer is valid.
- Validity changes monotonically as the candidate value increases or decreases.

### Related LeetCode Problems

| Problem | Number | Main idea |
|---|---:|---|
| Koko Eating Bananas | 875 | Minimum eating speed |
| Capacity To Ship Packages Within D Days | 1011 | Minimum ship capacity |
| Minimum Number of Days to Make m Bouquets | 1482 | Minimum number of days |
| Split Array Largest Sum | 410 | Minimize the largest subarray sum |
| Find the Smallest Divisor Given a Threshold | 1283 | Minimum valid divisor |

### Koko Eating Bananas vs. Ship Packages

| Feature | LC 875 | LC 1011 |
|---|---|---|
| What are we finding? | Minimum eating speed | Minimum ship capacity |
| Search range | `1` to `max(piles)` | `max(weights)` to `sum(weights)` |
| Feasibility check | Sum of ceiling divisions | Greedy count of required days |
| If candidate works | Search smaller | Search smaller |

---

## 12. Quick Revision

Remember the core code:

```python
left = 1
right = max(piles)

while left < right:
    mid = (left + right) // 2

    hours_needed = 0

    for pile in piles:
        hours_needed += (pile + mid - 1) // mid

    if hours_needed <= h:
        right = mid
    else:
        left = mid + 1

return left
```

Key points:

- Search for the minimum valid eating speed.
- Use `1` and `max(piles)` as the search boundaries.
- Use ceiling division to calculate hours per pile.
- If the speed works, search smaller.
- If the speed fails, search larger.
- Return `left` when the boundaries meet.

**Final Complexity:**
- Time: `O(n log M)`, where `M = max(piles)`.
- Space: `O(1)`.
