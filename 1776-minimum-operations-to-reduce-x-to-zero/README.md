# 1658. Minimum Operations to Reduce X to Zero

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

---

## Problem Statement

You are given an integer array `nums` and an integer `x`.

In one operation, you can remove either the leftmost or the rightmost element from `nums` and subtract its value from `x`.

Return the **minimum number of operations** needed to reduce `x` to exactly `0`. If it is impossible, return `-1`.

## Examples

### Example 1

```text
Input:  nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: Remove the last two elements: 3 and 2.
```

### Example 2

```text
Input:  nums = [5,6,7,8,9], x = 4
Output: -1
```

### Example 3

```text
Input:  nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: Remove the last three elements and the first two elements.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= x <= 10^9`

---

## Approach: Sliding Window (Longest Subarray)

A direct approach would try different combinations of removing elements from the left and right. That can take too much time.

Instead, think about the elements that we **keep**.

Let:

```text
total = sum(nums)
```

If we remove elements whose sum is exactly `x`, the sum of the elements left in the middle must be:

```text
target = total - x
```

Because we only remove elements from the two ends, the elements that remain must form one continuous subarray.

To minimize the number of removed elements, we need to keep as many elements as possible.

Therefore:

- Find the **longest continuous subarray** whose sum is `total - x`.
- The minimum number of operations is `n - longest_length`.

All array elements are positive, so we can find this longest subarray using a sliding window.

## Algorithm

1. Calculate `total = sum(nums)`.
2. Calculate `target = total - x`.
3. If `target < 0`, return `-1`, because the total sum is smaller than `x`.
4. If `target == 0`, all elements must be removed, so return `len(nums)`.
5. Initialize:
   - `left = 0`
   - `current_sum = 0`
   - `max_length = 0`
6. Move `right` through the array:
   - Add `nums[right]` to `current_sum`.
   - While `current_sum > target`, subtract `nums[left]` and move `left` forward.
   - If `current_sum == target`, update `max_length`.
7. If no valid subarray was found, return `-1`.
8. Otherwise, return `len(nums) - max_length`.

## Python Code

```python
class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_length = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == 0:
            return -1

        return len(nums) - max_length
```

## Dry Run

Input:

```text
nums = [1, 1, 4, 2, 3]
x = 5
```

### Step 1: Calculate the target sum

```text
total = 1 + 1 + 4 + 2 + 3 = 11

target = total - x
       = 11 - 5
       = 6
```

We need to find the longest continuous subarray with sum `6`.

### Step 2: Apply the sliding window

| Right | Added value | Current window | Window sum | Maximum length |
|---:|---:|---|---:|---:|
| 0 | 1 | `[1]` | 1 | 0 |
| 1 | 1 | `[1, 1]` | 2 | 0 |
| 2 | 4 | `[1, 1, 4]` | 6 | 3 |
| 3 | 2 | `[1, 4, 2]` | 7, then shrink to `[4, 2]` | 3 |
| 4 | 3 | `[4, 2, 3]` | 9, then shrink to `[2, 3]` | 3 |

The longest valid subarray is `[1, 1, 4]`, with length `3`.

### Step 3: Calculate the minimum operations

```text
Minimum operations = n - maximum subarray length
                   = 5 - 3
                   = 2
```

**Output: `2`**

We remove `2` and `3` from the right side. Their sum is exactly `5`.

## Why This Works

Every valid sequence of removals takes some elements from the left and some from the right. The elements not removed are always one continuous middle subarray.

If the total array sum is `total`, the remaining subarray must have sum `total - x`.

The number of removed elements is:

```text
n - length of the remaining subarray
```

So minimizing removals is the same as maximizing the length of a subarray with sum `total - x`.

Since all elements are positive, expanding the window increases its sum and shrinking it decreases its sum. This makes the sliding window approach correct and efficient.

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity: `O(n)`**
  - Calculating the total sum takes `O(n)`.
  - The right pointer visits each element once.
  - The left pointer also moves forward at most `n` times.
- **Space Complexity: `O(1)`**
  - Only a fixed number of variables are used.

## Pattern

**Sliding Window — Longest Subarray with a Target Sum**

This transformation is useful when:
- You need to remove elements from both ends of an array.
- The remaining elements form a continuous subarray.
- You want to minimize removed elements.
- The array contains positive numbers, allowing a sliding window.

**Key formula:**

```python
target = sum(nums) - x
answer = len(nums) - longest_subarray_length
```

**Important edge cases:**

- If `sum(nums) < x`, return `-1`.
- If `sum(nums) == x`, remove every element and return `len(nums)`.
- If no subarray has sum `sum(nums) - x`, return `-1`.
