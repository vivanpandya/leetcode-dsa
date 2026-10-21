# 643. Maximum Average Subarray I

[LeetCode Problem](https://leetcode.com/problems/maximum-average-subarray-i/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.

### Example 1

**Input:**
```text
nums = [1,12,-5,-6,50,3], k = 4
```

**Output:**
```text
12.75000
```

**Explanation:** The maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.

### Example 2

**Input:**
```text
nums = [5], k = 1
```

**Output:**
```text
5.00000
```

### Constraints

- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 1. Approach

Use a **fixed-size sliding window**.

Instead of calculating the sum of every subarray of length `k` from scratch, calculate the first window sum once. Then slide the window one position at a time:
- Add the new element entering the window.
- Subtract the element leaving the window.
- Track the maximum window sum.

The maximum average is the maximum window sum divided by `k`.

## 2. Algorithm

1. Calculate the sum of the first `k` elements and store it in `current_sum`.
2. Set `max_sum = current_sum`.
3. For each index `i` from `k` to the end of the array:
   - Add `nums[i]` to the current window sum.
   - Subtract `nums[i - k]`, which has left the window.
   - Update `max_sum` if `current_sum` is larger.
4. Return `max_sum / k`.

## 3. Code

```python
class Solution:
    def findMaxAverage(self, nums, k):
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
```

## 4. Dry Run

Input: `nums = [1, 12, -5, -6, 50, 3]`, `k = 4`

| Window | Calculation | Sum | Average |
|---|---|---:|---:|
| `[1, 12, -5, -6]` | `1 + 12 - 5 - 6` | `2` | `0.5` |
| `[12, -5, -6, 50]` | `2 + 50 - 1` | `51` | `12.75` |
| `[-5, -6, 50, 3]` | `51 + 3 - 12` | `42` | `10.5` |

The maximum sum is `51`, so the maximum average is `51 / 4 = 12.75`.

## 5. Why This Works

Every possible contiguous subarray of length `k` is considered as the window moves from left to right. Each new window sum is calculated from the previous sum by adding the incoming value and removing the outgoing value. Therefore, `max_sum` records the largest sum among all length-`k` windows, and dividing it by the fixed length `k` gives the maximum average.

## 6. Time Complexity

**O(n)** — the first window takes `O(k)` time, and the remaining `n - k` elements are processed once.

## 7. Space Complexity

**O(1)** auxiliary space — only a fixed number of variables are used.

## 8. Pattern

**Fixed-Size Sliding Window**

Use this pattern when the problem asks for the maximum or minimum sum/average of a contiguous subarray with a fixed length `k`.
