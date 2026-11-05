# 523. Continuous Subarray Sum

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/continuous-subarray-sum/

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if the array contains a **good subarray**, otherwise return `False`.

A good subarray must satisfy both conditions:

1. Its length is at least `2`.
2. The sum of its elements is a multiple of `k`.

A subarray is a contiguous part of an array. Zero is also considered a multiple of `k`.

## Examples

### Example 1

```text
Input: nums = [23, 2, 4, 6, 7], k = 6
Output: true
```

Explanation: The subarray `[2, 4]` has length `2` and its sum is `6`, which is a multiple of `6`.

### Example 2

```text
Input: nums = [23, 2, 6, 4, 7], k = 6
Output: true
```

Explanation: The entire array has sum `42`, and `42` is a multiple of `6`.

### Example 3

```text
Input: nums = [23, 2, 6, 4, 7], k = 13
Output: false
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

---

## Approach: Prefix Sum + HashMap (Remainder)

We need to find a continuous subarray whose sum is divisible by `k`, and its length must be at least `2`.

A direct approach would check every possible subarray, but that takes O(n²) time and is too slow for an array of up to `10^5` elements.

We can solve this in **O(n)** time using prefix sums and a HashMap.

### Key Idea

Let `prefix_sum` be the sum of the array from index `0` to the current index.

If two prefix sums have the same remainder when divided by `k`, their difference is divisible by `k`.

In other words:

```text
prefix_sum[j] % k == prefix_sum[i] % k

=> (prefix_sum[j] - prefix_sum[i]) % k == 0
```

The difference between these prefix sums is the sum of the subarray from `i + 1` to `j`.

So, if the same remainder appears again and the distance between the two indices is at least `2`, we found a good subarray.

### Why Store the First Index?

For each remainder, we store its **first occurrence** in the HashMap.

This gives us the longest possible distance when that remainder appears again, making it easier to satisfy the minimum subarray length of `2`.

We initialize the HashMap as:

```python
remainder_index = {0: -1}
```

This handles a subarray starting from index `0`. The remainder `0` is considered to have appeared before the array begins, at index `-1`.

## Algorithm

1. Create a HashMap `remainder_index = {0: -1}`.
2. Set `prefix_sum = 0`.
3. Traverse the array using index `i`.
4. Add the current number to `prefix_sum`.
5. Calculate `remainder = prefix_sum % k`.
6. If this remainder is already in the HashMap:
   - Check whether `i - remainder_index[remainder] >= 2`.
   - If yes, return `True`.
7. If the remainder is not in the HashMap, store its first index.
8. If no valid subarray is found, return `False`.

## Python Code

```python
class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False
```

## Dry Run

Input:

```python
nums = [23, 2, 4, 6, 7]
k = 6
```

Initial values:

```text
prefix_sum = 0
remainder_index = {0: -1}
```

| Index `i` | `nums[i]` | Prefix Sum | Remainder (`prefix_sum % 6`) | HashMap / Check |
|---:|---:|---:|---:|---|
| 0 | 23 | 23 | 5 | Store `5: 0` |
| 1 | 2 | 25 | 1 | Store `1: 1` |
| 2 | 4 | 29 | 5 | Remainder `5` seen at index `0`; `2 - 0 = 2` |

The same remainder `5` appears at indices `0` and `2`.

The subarray is from index `0 + 1` to index `2`:

```text
nums[1:3] = [2, 4]
sum = 2 + 4 = 6
6 % 6 = 0
length = 2
```

Both conditions are satisfied, so the function returns:

```text
True
```

## Why This Works

Suppose two prefix sums have the same remainder when divided by `k`.

```text
prefix_sum_1 = a * k + r
prefix_sum_2 = b * k + r
```

Subtracting them:

```text
prefix_sum_2 - prefix_sum_1 = (b - a) * k
```

The difference is a multiple of `k`. That difference is exactly the sum of the subarray between the two prefix positions.

We also check that the index difference is at least `2`, which guarantees the subarray contains at least two elements.

Therefore, the algorithm returns `True` only when a valid good subarray exists.

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** O(n) average — we traverse the array once, and HashMap lookups and insertions take O(1) average time.
- **Space Complexity:** O(min(n, k)) in the usual remainder-map bound, and O(n) in the general upper bound — we store at most one first index for each remainder encountered.

## Pattern

**Prefix Sum + HashMap + Modulo**

Use this pattern when:
- You need to find a subarray whose sum is divisible by a number.
- You need to check whether a subarray sum has a particular remainder.
- You need to solve a contiguous-subarray problem efficiently.

**Important formula:**

```python
remainder = prefix_sum % k
```

If the same remainder occurs at two indices and their difference is at least `2`, the subarray between them has a sum divisible by `k`.

**Key takeaway:** Equal prefix-sum remainders mean the sum between those prefix positions is divisible by `k`. Always check the minimum subarray length.
