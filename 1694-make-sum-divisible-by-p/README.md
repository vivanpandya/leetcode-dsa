# 1590. Make Sum Divisible by P

[LeetCode Problem](https://leetcode.com/problems/make-sum-divisible-by-p/)  
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum, Modulo

---

## 1. Question

Given an array of positive integers `nums`, remove the **smallest contiguous subarray** (possibly empty) such that the sum of the remaining elements is divisible by `p`.

You cannot remove the entire array.

Return the length of the smallest subarray to remove, or `-1` if it is impossible.

## 2. Examples

### Example 1

```text
Input:  nums = [3,1,4,2], p = 6
Output: 1
```

The total sum is `10`, which is not divisible by `6`. Remove `[4]`. The remaining sum is `3 + 1 + 2 = 6`.

### Example 2

```text
Input:  nums = [6,3,5,2], p = 9
Output: 2
```

Remove `[5,2]`, leaving `[6,3]`, whose sum is `9`.

### Example 3

```text
Input:  nums = [1,2,3], p = 3
Output: 0
```

The total sum is already `6`, which is divisible by `3`. No removal is needed.

## 3. Approach — Prefix Sum + HashMap + Modulo

A brute-force solution checks every possible subarray and can take `O(n²)` time. We can solve this in `O(n)` using prefix remainders and a hash map.

### Step 1: Find the required remainder

Calculate:

```python
target = sum(nums) % p
```

If `target == 0`, the total sum is already divisible by `p`, so return `0`.

Otherwise, we need to remove a subarray whose sum has remainder `target` modulo `p`.

If the total sum is `S` and the removed subarray sum is `R`, then:

```text
(S - R) % p == 0
```

Therefore:

```text
R % p == S % p == target
```

### Step 2: Use prefix remainders

Maintain the running prefix remainder:

```python
prefix = (prefix + nums[i]) % p
```

If the current prefix remainder is `prefix` and an earlier prefix remainder is `previous`, the subarray between those prefix positions has remainder:

```text
(prefix - previous) % p
```

We want this to equal `target`, so:

```python
previous = (prefix - target) % p
```

For each index, look up this required remainder in the hash map.

### Step 3: Store the latest index

Use `last_seen` to store each prefix remainder and its latest index.

We store the latest index because, for a fixed ending index, a later starting boundary produces a shorter subarray.

Initialize:

```python
last_seen = {0: -1}
```

The entry `{0: -1}` represents the empty prefix before the array starts and allows subarrays beginning at index `0` to be found.

### Step 4: Do not remove the whole array

The problem forbids removing all elements. If the best removal length is `len(nums)`, return `-1`.

## 4. Algorithm

1. Calculate `target = sum(nums) % p`.
2. If `target == 0`, return `0`.
3. Initialize `prefix = 0`, `min_length = len(nums)`, and `last_seen = {0: -1}`.
4. Traverse the array:
   - Update the prefix remainder.
   - Calculate `needed = (prefix - target) % p`.
   - If `needed` exists in `last_seen`, update the minimum subarray length.
   - Store the current prefix remainder's index.
5. If `min_length == len(nums)`, return `-1`.
6. Otherwise, return `min_length`.

## 5. Python Code

```python
class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        min_length = len(nums)
        last_seen = {0: -1}

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p

            needed = (prefix - target) % p

            if needed in last_seen:
                min_length = min(min_length, i - last_seen[needed])

            last_seen[prefix] = i

        if min_length == len(nums):
            return -1

        return min_length
```

## 6. Dry Run

Input:

```python
nums = [3, 1, 4, 2]
p = 6
```

First calculate:

```text
total = 3 + 1 + 4 + 2 = 10
target = 10 % 6 = 4
```

Initial values:

```python
prefix = 0
min_length = 4
last_seen = {0: -1}
```

| Index `i` | `nums[i]` | Prefix remainder | `needed = (prefix - 4) % 6` | Previous index | Candidate length | Minimum length |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 3 | 5 | Not found | — | 4 |
| 1 | 1 | 4 | 0 | -1 | 2 | 2 |
| 2 | 4 | 2 | 4 | 1 | 1 | 1 |
| 3 | 2 | 4 | 0 | -1 | 4 | 1 |

At index `2`:

```text
prefix = 2
needed = (2 - 4) % 6 = 4
last_seen[4] = 1

candidate length = 2 - 1 = 1
```

The subarray is `[4]`. Removing it leaves `[3,1,2]`, whose sum is `6`.

**Output:**

```text
1
```

## 7. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity: `O(n)` average**
  - Calculating the total sum takes `O(n)`.
  - The second traversal takes `O(n)`.
  - Hash map lookups and insertions take `O(1)` average time.

- **Space Complexity: `O(min(n, p))`**
  - The hash map stores prefix remainders.
  - It can contain at most `n + 1` entries and at most `p` distinct remainders.

## 8. Pattern

**Prefix Sum + HashMap + Modulo**

The most important formula is:

```python
needed = (prefix - target) % p
```

It finds the earlier prefix remainder that makes the subarray between the two prefix positions have the required remainder.

### Related LeetCode Problems

| Problem | Pattern |
|---|---|
| #523 — Continuous Subarray Sum | Prefix Sum + Modulo + HashMap |
| #560 — Subarray Sum Equals K | Prefix Sum + HashMap |
| #974 — Subarray Sums Divisible by K | Prefix Sum + Modulo + HashMap |
| #2845 — Count of Interesting Subarrays | Prefix Remainder + HashMap |
| #1590 — Make Sum Divisible by P | Prefix Sum + Modulo + HashMap |

---

**Key takeaway:** For a contiguous subarray with a modulo condition, use prefix remainders and a hash map. Store the latest index of each remainder to find the shortest qualifying subarray ending at the current position.
