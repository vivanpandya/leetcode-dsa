# 1493. Longest Subarray of 1's After Deleting One Element

**LeetCode:** [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)  
**Difficulty:** Medium  
**Pattern:** Sliding Window

---

## 1. Question

Given a binary array `nums`, delete exactly one element from it.

Return the length of the longest non-empty subarray containing only `1`s in the resulting array. If there is no such subarray, return `0`.

## 2. Examples

### Example 1

**Input:** `nums = [1,1,0,1]`  
**Output:** `3`

Delete the `0` at index `2`. The remaining consecutive ones are `[1,1,1]`, with length `3`.

### Example 2

**Input:** `nums = [0,1,1,1,0,1,1,0,1]`  
**Output:** `5`

Delete the `0` between the first group of three ones and the next group of two ones. The longest resulting group of ones has length `5`.

### Example 3

**Input:** `nums = [1,1,1]`  
**Output:** `2`

We must delete exactly one element, so one `1` must be removed.

## 3. Approach

Use a **sliding window** that contains at most one zero.

- `left` is the start of the current window.
- `right` expands the window.
- `zeros` counts zeros inside the window.
- If the window contains more than one zero, move `left` forward until only one zero remains.
- The window's length is `right - left + 1`, but we must delete one element. Therefore, the number of consecutive ones after deletion is `right - left`.

Subtracting one handles both cases:
- If the window contains one zero, delete that zero.
- If the window contains no zeros, delete one of the ones.

## 4. Algorithm

1. Initialize `left = 0`, `zeros = 0`, and `max_length = 0`.
2. For each `right` index:
   - If `nums[right] == 0`, increment `zeros`.
   - While `zeros > 1`:
     - If `nums[left] == 0`, decrement `zeros`.
     - Increment `left`.
   - Update `max_length` with `right - left`.
3. Return `max_length`.

## 5. Code

```python
class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length
```

## 6. Dry Run

For `nums = [1,1,0,1]`:

| `right` | Value | Zeros in window | Window | `right - left` | Maximum |
|---:|---:|---:|---|---:|---:|
| 0 | 1 | 0 | `[1]` | 0 | 0 |
| 1 | 1 | 0 | `[1,1]` | 1 | 1 |
| 2 | 0 | 1 | `[1,1,0]` | 2 | 2 |
| 3 | 1 | 1 | `[1,1,0,1]` | 3 | 3 |

Delete the zero from the best window `[1,1,0,1]`. The remaining consecutive ones have length `3`.

**Final output:** `3`

## 7. Complexity

- **Time Complexity:** `O(n)` — each index enters and leaves the window at most once.
- **Space Complexity:** `O(1)` — only a few variables are used.

## 8. Pattern

**Sliding Window — Longest Subarray With At Most One Zero**

For this problem, keep at most one zero in the window and use `right - left` instead of `right - left + 1`, because exactly one element must be deleted.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
