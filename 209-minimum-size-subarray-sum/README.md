# 209. Minimum Size Subarray Sum

[LeetCode Problem](https://leetcode.com/problems/minimum-size-subarray-sum/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a non-empty subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0`.

### Example 1

**Input:**
```text
target = 7, nums = [2,3,1,2,4,3]
```

**Output:**
```text
2
```

**Explanation:** The subarray `[4,3]` has the minimum length because its sum is `7`.

### Example 2

**Input:**
```text
target = 4, nums = [1,4,4]
```

**Output:**
```text
1
```

### Example 3

**Input:**
```text
target = 11, nums = [1,1,1,1,1,1,1,1]
```

**Output:**
```text
0
```

### Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

**Follow-up:** If you have solved it in `O(n)`, try another solution with `O(n log n)` time complexity.

---

## 1. Approach

Use a **sliding window (two pointers)**. Since every number is positive, expanding the window increases its sum, and shrinking it decreases its sum.

- `left` is the start of the current window.
- `right` moves through the array, adding each number to `current_sum`.
- Whenever `current_sum >= target`, update the shortest length and move `left` forward while the window still meets the target.

## 2. Algorithm

1. Initialize `left = 0`, `current_sum = 0`, and `min_length = infinity`.
2. Loop through `nums` using `right`.
3. Add `nums[right]` to `current_sum`.
4. While `current_sum >= target`:
   - Update `min_length` with `right - left + 1`.
   - Subtract `nums[left]` from `current_sum`.
   - Increment `left`.
5. If `min_length` was never updated, return `0`; otherwise, return `min_length`.

## 3. Code — O(n) Sliding Window

```python
class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length
```

## 4. Dry Run

Input: `target = 7`, `nums = [2,3,1,2,4,3]`

| `right` | Added value | Window sum before shrinking | Action | Best length |
|---:|---:|---:|---|---:|
| 0 | 2 | 2 | Sum is below 7 | infinity |
| 1 | 3 | 5 | Sum is below 7 | infinity |
| 2 | 1 | 6 | Sum is below 7 | infinity |
| 3 | 2 | 8 | Window `[2,3,1,2]` qualifies; shrink from left | 4 |
| 4 | 4 | 10 | Window `[3,1,2,4]` qualifies; shrink from left | 4 |
| 5 | 3 | 9 | Window `[2,4,3]` qualifies; shrink again to `[4,3]` | 2 |

**Answer: `2`**

## 5. Why This Works

All array elements are positive. Therefore, if the current window sum is too small, adding more elements on the right is the way to increase it. Once the sum reaches the target, removing elements from the left can make the window shorter. Each time the sum is at least the target, the algorithm records its length before shrinking. Because both pointers only move forward, the algorithm finds the minimum valid length efficiently.

## 6. Time Complexity

**O(n)** — each element is added to the window once and removed at most once.

## 7. Space Complexity

**O(1)** — only a fixed number of variables are used.

## 8. Pattern

**Sliding Window + Two Pointers**

This pattern is especially useful for contiguous subarray problems when the array contains positive numbers and a running sum can guide window expansion and shrinking.

---

## Follow-up: O(n log n) Alternative

A second solution can use **prefix sums + binary search**. Because all numbers are positive, prefix sums are increasing. For each starting index, binary-search for the earliest prefix sum that reaches `prefix_sum[start] + target`. This takes `O(n log n)` time and `O(n)` space.

The sliding-window solution above is simpler and faster for this problem.
