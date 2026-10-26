# 1004. Max Consecutive Ones III

**LeetCode:** [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)  
**Difficulty:** Medium  
**Pattern:** Variable-Size Sliding Window

---

## 1. Question

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` zeros into ones.

## 2. Examples

### Example 1

**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`  
**Output:** `6`

We can flip at most two zeros in a window to make six consecutive ones.

### Example 2

**Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]`, `k = 3`  
**Output:** `10`

The longest valid window has length 10 and contains at most three zeros.

## 3. Approach

Use a **variable-size sliding window**.

- `left` marks the beginning of the current window.
- `right` expands the window by moving from left to right.
- `zeros` counts the zeros inside the current window.
- If `zeros` becomes greater than `k`, move `left` forward until the window contains at most `k` zeros.
- Track the largest valid window length.

A window is valid whenever it contains at most `k` zeros, because those zeros can be flipped to ones.

## 4. Algorithm

1. Initialize `left = 0`, `zeros = 0`, and `max_length = 0`.
2. Iterate `right` over every index in `nums`.
3. If `nums[right] == 0`, increment `zeros`.
4. While `zeros > k`:
   - If `nums[left] == 0`, decrement `zeros`.
   - Increment `left`.
5. Update `max_length` with `right - left + 1`.
6. Return `max_length`.

## 5. Code

```python
class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

## 6. Dry Run

For `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`:

| `right` | Value added | Zero count after adjustment | Current window length | `max_length` |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 2 | 2 |
| 2 | 1 | 0 | 3 | 3 |
| 3 | 0 | 1 | 4 | 4 |
| 4 | 0 | 2 | 5 | 5 |
| 5 | 0 | 2 (window shrinks) | 2 | 5 |
| 6 | 1 | 2 | 3 | 5 |
| 7 | 1 | 2 | 4 | 5 |
| 8 | 1 | 2 | 5 | 5 |
| 9 | 1 | 2 | 6 | 6 |
| 10 | 0 | 2 (window shrinks) | 6 | 6 |

**Final output:** `6`

## 7. Complexity

- **Time Complexity:** `O(n)` — each index enters the window once and leaves it at most once.
- **Space Complexity:** `O(1)` — only a few variables are used.

## 8. Pattern

**Sliding Window — Longest Subarray With At Most `k` Zeros**

Use this pattern for problems asking for the longest continuous segment where at most `k` elements can be changed or treated as exceptions.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`
