# 1248. Count Number of Nice Subarrays

**LeetCode:** https://leetcode.com/problems/count-number-of-nice-subarrays/  
**Difficulty:** Medium  
**Pattern:** Sliding Window — At Most Trick

## Question

Given an integer array `nums` and an integer `k`, a continuous subarray is called **nice** if it contains exactly `k` odd numbers. Return the number of nice subarrays.

## Examples

### Example 1
**Input**
```python
nums = [1, 1, 2, 1, 1]
k = 3
```
**Output:** `2`

**Explanation:** The only subarrays with exactly 3 odd numbers are `[1, 1, 2, 1]` and `[1, 2, 1, 1]`.

### Example 2
**Input**
```python
nums = [2, 4, 6]
k = 1
```
**Output:** `0`

**Explanation:** There are no odd numbers in the array.

### Example 3
**Input**
```python
nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
```
**Output:** `16`

## Constraints
- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

---

## Approach

Use the **Sliding Window + At Most Trick**.

Count subarrays with at most `k` odd numbers and subtract the count of subarrays with at most `k - 1` odd numbers:

`exactly(k) = atMost(k) - atMost(k - 1)`

For each right endpoint, after shrinking the window until it contains at most `k` odd numbers, every subarray starting from `left` through `right` is valid. Add `right - left + 1` to the count.

## Algorithm
1. Define a helper function `atMost(k)`.
2. Initialize `left = 0`, `odd_count = 0`, and `count = 0`.
3. Move `right` through every index of `nums`.
4. If `nums[right]` is odd, increment `odd_count`.
5. While `odd_count > k`, remove `nums[left]` from the window, decrementing `odd_count` if it is odd, then move `left` forward.
6. Add `right - left + 1` to `count`.
7. Return `atMost(k) - atMost(k - 1)`.

## Code
```python
class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            left = 0
            odd_count = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1

                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)
```

## Dry Run

For `nums = [1, 1, 2, 1, 1]`, `k = 3`, first calculate `atMost(3)`.

| `right` | Value | Odd count | Valid subarrays ending here | Running count |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 2 | 2 | 3 |
| 2 | 2 | 2 | 3 | 6 |
| 3 | 1 | 3 | 4 | 10 |
| 4 | 1 | 3 | 4 | 14 |

So `atMost(3) = 14`. For `atMost(2)`, the count is `12`.

`14 - 12 = 2`

**Output:** `2`

## Why This Works

Every subarray with exactly `k` odd numbers is included in `atMost(k)`, but not in `atMost(k - 1)`. Subarrays with fewer than `k` odd numbers are counted by both and cancel out when subtracted. The difference is therefore the number of nice subarrays.

## Complexity
- **Time:** `O(n)` — each pointer moves forward at most `n` times per helper call; the helper is called twice.
- **Space:** `O(1)` — only a fixed number of variables are used.

## Pattern

**Sliding Window + At Most Trick**

- `exactly(k) = atMost(k) - atMost(k - 1)`
- `count += right - left + 1` counts valid subarrays ending at `right`.
- Useful for subarray problems asking for exactly `k` qualifying elements.
