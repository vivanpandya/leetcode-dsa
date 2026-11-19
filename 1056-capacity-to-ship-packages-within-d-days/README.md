# 1011. Capacity To Ship Packages Within D Days

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

- **LeetCode:** [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- **Problem Number:** 1011
- **Difficulty:** Medium
- **Topics:** Array, Binary Search, Greedy

---

## 1. Problem Statement

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i-th` package has weight `weights[i]`.

Each day:
- Packages must be loaded in the given order.
- We can load consecutive packages onto the ship.
- The total weight loaded that day cannot exceed the ship's capacity.

Return the **minimum ship capacity** that allows all packages to be shipped within `days` days.

## 2. Examples

### Example 1

```text
Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
```

**Explanation:** With capacity 15, the packages can be shipped as follows:

| Day | Packages | Total weight |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 5 | 15 |
| 2 | 6, 7 | 13 |
| 3 | 8 | 8 |
| 4 | 9 | 9 |
| 5 | 10 | 10 |

Capacity 14 is not sufficient to complete the shipment in 5 days while preserving the original package order.

### Example 2

```text
Input:  weights = [3,2,2,4,1,4], days = 3
Output: 6
```

**Explanation:**

| Day | Packages | Total weight |
|---:|---|---:|
| 1 | 3, 2 | 5 |
| 2 | 2, 4 | 6 |
| 3 | 1, 4 | 5 |

### Example 3

```text
Input:  weights = [1,2,3,1,1], days = 4
Output: 3
```

**Explanation:**

| Day | Packages | Total weight |
|---:|---|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 1, 1 | 2 |

## 3. Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

---

## 4. Approach: Binary Search on Answer + Greedy

We are not searching for a particular package. We are searching for the **minimum ship capacity** that makes it possible to deliver all packages within the given number of days.

This is called **Binary Search on Answer**.

For each candidate capacity, we use a greedy simulation to count how many days are needed.

### Step 1: Find the search range

The minimum possible capacity is the weight of the heaviest package:

```python
left = max(weights)
```

The ship must be able to carry every individual package.

The maximum possible capacity is the sum of all package weights:

```python
right = sum(weights)
```

With this capacity, all packages can be shipped in one day.

Therefore:

```python
left = max(weights)
right = sum(weights)
```

### Step 2: Choose a candidate capacity

```python
mid = (left + right) // 2
```

We temporarily assume the ship has capacity `mid`.

### Step 3: Count the days needed

Initialize:

```python
days_needed = 1
current_weight = 0
```

Traverse packages in their original order.

For each package:

**Case 1: The package fits**

If adding the package does not exceed the candidate capacity:

```python
current_weight += weight
```

**Case 2: The package does not fit**

Start a new day and load the current package onto that day:

```python
days_needed += 1
current_weight = weight
```

We do not skip or reorder packages.

### Step 4: Decide which half to search

**Case 1: `days_needed <= days`**

The candidate capacity is sufficient. Since we need the minimum capacity, try a smaller one:

```python
right = mid
```

**Case 2: `days_needed > days`**

The candidate capacity is too small. Increase it:

```python
left = mid + 1
```

Continue until `left == right`. That value is the minimum valid ship capacity.

---

## 5. Algorithm

1. Set `left = max(weights)`.
2. Set `right = sum(weights)`.
3. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - Initialize `days_needed = 1` and `current_weight = 0`.
   - Traverse the packages in their original order:
     - If `current_weight + weight <= mid`, add the package to the current day.
     - Otherwise, start a new day and set `current_weight = weight`.
   - If `days_needed <= days`, set `right = mid`.
   - Otherwise, set `left = mid + 1`.
4. Return `left`.

---

## 6. Python Solution

```python
class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            days_needed = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    days_needed += 1
                    current_weight = weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return left
```

### Code Explanation

| Code | Purpose |
|---|---|
| `left = max(weights)` | Smallest possible capacity |
| `right = sum(weights)` | Largest useful capacity |
| `mid = (left + right) // 2` | Candidate ship capacity |
| `days_needed = 1` | Start with the first day |
| `current_weight = 0` | Track the current day's load |
| `current_weight + weight <= mid` | Check whether the package fits |
| `current_weight += weight` | Add the package to the current day |
| `days_needed += 1` | Start another day |
| `current_weight = weight` | Put the current package on the new day |
| `days_needed <= days` | Check whether the capacity is sufficient |
| `right = mid` | Capacity works; try a smaller one |
| `left = mid + 1` | Capacity is too small; try a larger one |
| `return left` | Return the minimum valid capacity |

---

## 7. Dry Run

Consider Example 1:

```python
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
```

Initial search range:

```text
left = 10
right = 55
```

### Iteration 1

```python
mid = (10 + 55) // 2  # 32
```

Greedy shipping simulation:

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 5, 6, 7 | 28 |
| 2 | 8, 9, 10 | 27 |

`days_needed = 2`.

Since `2 <= 5`, capacity 32 works:

```python
right = 32
```

### Iteration 2

```python
mid = (10 + 32) // 2  # 21
```

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 5, 6 | 21 |
| 2 | 7, 8 | 15 |
| 3 | 9, 10 | 19 |

`days_needed = 3`.

Since `3 <= 5`:

```python
right = 21
```

### Iteration 3

```python
mid = (10 + 21) // 2  # 15
```

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 5 | 15 |
| 2 | 6, 7 | 13 |
| 3 | 8 | 8 |
| 4 | 9 | 9 |
| 5 | 10 | 10 |

`days_needed = 5`.

Since `5 <= 5`:

```python
right = 15
```

### Iteration 4

```python
mid = (10 + 15) // 2  # 12
```

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4 | 10 |
| 2 | 5, 6 | 11 |
| 3 | 7 | 7 |
| 4 | 8 | 8 |
| 5 | 9 | 9 |
| 6 | 10 | 10 |

`days_needed = 6`.

Since `6 > 5`, capacity 12 is too small:

```python
left = 13
```

### Iteration 5

```python
mid = (13 + 15) // 2  # 14
```

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4 | 10 |
| 2 | 5, 6 | 11 |
| 3 | 7, 8 | 15 |

The third day's total in this row would exceed 14, so the correct greedy grouping is:

| Day | Packages | Total |
|---:|---|---:|
| 1 | 1, 2, 3, 4 | 10 |
| 2 | 5, 6 | 11 |
| 3 | 7 | 7 |
| 4 | 8 | 8 |
| 5 | 9 | 9 |
| 6 | 10 | 10 |

`days_needed = 6`.

Since `6 > 5`:

```python
left = 15
```

Now:

```text
left = 15
right = 15
```

The loop stops. Return `15`.

**Output:**

```text
15
```

---

## 8. Why This Works

For a fixed capacity, the greedy simulation loads as many consecutive packages as possible each day without exceeding that capacity.

This uses the fewest possible days for that capacity: moving a package to a later day when it already fits would not help reduce the number of days.

The feasibility condition is monotonic:

- If a capacity is too small, every smaller capacity is also too small.
- If a capacity works, every larger capacity also works.

Therefore, binary search can find the first capacity that ships all packages within the allowed days.

---

## 9. Complexity Analysis

Let:
- `n` = number of packages.
- `S` = sum of all package weights.
- `W` = maximum individual package weight.

### Time Complexity: `O(n log(S - W + 1))`

- The binary search checks capacities from `W` through `S`.
- Each feasibility check visits all `n` packages, taking `O(n)` time.
- The number of candidate capacities checked is logarithmic in the search range.

Therefore:

```text
O(n log(S - W + 1))
```

A commonly used simplified bound is:

```text
O(n log S)
```

### Space Complexity: `O(1)`

Only a fixed number of variables are used. No additional data structure is required.

```text
Space: O(1)
```

---

## 10. Important Edge Cases

### One day

If `days = 1`, the ship must carry every package in one day.

The answer is:

```python
sum(weights)
```

### One package per day

If `days == len(weights)`, the ship only needs to carry the heaviest individual package.

The answer is:

```python
max(weights)
```

### All packages have the same weight

```python
weights = [5, 5, 5, 5]
days = 2
```

A capacity of 10 ships two packages per day, so the answer is `10`.

### Capacity exactly equals a day's total

The condition uses `<=`, because a package can be loaded when the total weight is exactly equal to the ship capacity.

---

## 11. Pattern Recognition: Binary Search on Answer + Greedy

Recognize this pattern when:
- You need the minimum capacity, maximum load, or another optimal numeric limit.
- You can check whether a candidate value is feasible.
- Feasibility is monotonic.
- A greedy pass can validate each candidate.

### Related LeetCode Problems

| Problem | Number | Main idea |
|---|---:|---|
| Koko Eating Bananas | 875 | Minimum eating speed |
| Capacity To Ship Packages Within D Days | 1011 | Minimum ship capacity |
| Minimum Number of Days to Make m Bouquets | 1482 | Minimum number of days |
| Split Array Largest Sum | 410 | Minimize the largest subarray sum |
| Find the Smallest Divisor Given a Threshold | 1283 | Minimum valid divisor |

### LC 875 vs. LC 1011

| Feature | LC 875 – Koko | LC 1011 – Ship Packages |
|---|---|---|
| Search for | Eating speed | Ship capacity |
| Search range | `1` to `max(piles)` | `max(weights)` to `sum(weights)` |
| Feasibility check | Sum of ceiling divisions | Greedy count of required days |
| Candidate works | Search smaller | Search smaller |
| Candidate fails | Search larger | Search larger |

---

## 12. Quick Revision

Remember this core code:

```python
left = max(weights)
right = sum(weights)

while left < right:
    mid = (left + right) // 2

    days_needed = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= mid:
            current_weight += weight
        else:
            days_needed += 1
            current_weight = weight

    if days_needed <= days:
        right = mid
    else:
        left = mid + 1

return left
```

Key points:

- Packages must remain in their original order.
- `max(weights)` is the minimum possible capacity.
- `sum(weights)` is the maximum useful capacity.
- Greedily load as many consecutive packages as fit each day.
- If the candidate works, search for a smaller capacity.
- If it fails, search for a larger capacity.

**Final Complexity:**
- Time: `O(n log S)`, where `S = sum(weights)`.
- Space: `O(1)`.
