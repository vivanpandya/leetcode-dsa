# 525. Contiguous Array

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/contiguous-array/

---

## Problem Statement

Given a binary array `nums`, return the **maximum length of a contiguous subarray** with an equal number of `0`s and `1`s.

## Examples

### Example 1

```text
Input: nums = [0, 1]
Output: 2
```

Explanation: `[0, 1]` is the longest contiguous subarray with an equal number of zeros and ones.

### Example 2

```text
Input: nums = [0, 1, 0]
Output: 2
```

Explanation: `[0, 1]` or `[1, 0]` is a longest contiguous subarray with an equal number of zeros and ones.

### Example 3

```text
Input: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
Output: 6
```

Explanation: `[1, 1, 1, 0, 0, 0]` is the longest contiguous subarray with an equal number of zeros and ones.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach: Prefix Sum + HashMap

The main idea is to convert every `0` into `-1`.

- Treat every `1` as `+1`.
- Treat every `0` as `-1`.

Now, a subarray containing an equal number of zeros and ones will have a sum of `0`.

For example:

```text
Original array:  [0, 1, 1, 0]
Converted array: [-1, 1, 1, -1]

Sum = -1 + 1 + 1 - 1 = 0
```

We use a prefix sum and a HashMap to find the longest subarray whose sum is zero.

### Why Does a Repeated Prefix Sum Help?

If the same prefix sum appears at two different indices, the sum of the elements between those indices is zero.

We store the **first occurrence** of each prefix sum because it gives the longest possible subarray when that sum appears again.

## Algorithm

1. Initialize `prefix_sum = 0` and `max_length = 0`.
2. Create a HashMap `seen = {0: -1}`. This handles a valid subarray that starts at index `0`.
3. Traverse the array using index `i`.
4. If `nums[i] == 1`, add `1` to `prefix_sum`.
5. Otherwise, subtract `1` from `prefix_sum`.
6. If `prefix_sum` already exists in `seen`, calculate `i - seen[prefix_sum]` and update `max_length`.
7. Otherwise, store the current index as the first occurrence of this prefix sum.
8. Return `max_length`.

## Python Code

```python
class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_length = 0
        seen = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in seen:
                max_length = max(max_length, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        return max_length
```

## Dry Run

Input:

```python
nums = [0, 1, 0]
```

Initial values:

```text
prefix_sum = 0
max_length = 0
seen = {0: -1}
```

| Index | Number | Prefix Sum | HashMap Check | Max Length |
|---:|---:|---:|---|---:|
| 0 | 0 | -1 | Not found → store `-1: 0` | 0 |
| 1 | 1 | 0 | Found at index `-1` → length `1 - (-1) = 2` | 2 |
| 2 | 0 | -1 | Found at index `0` → length `2 - 0 = 2` | 2 |

Final answer:

```text
2
```

## Why This Works

After converting `0` to `-1` and keeping `1` as `+1`, equal numbers of zeros and ones produce a total sum of zero.

If two prefix sums are equal, subtracting them gives zero. That difference is the sum of the subarray between the two prefix positions.

Therefore, whenever a prefix sum repeats, the elements between its first occurrence and current occurrence contain an equal number of zeros and ones.

By storing the earliest index for each prefix sum, we get the longest valid subarray for that sum.

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** O(n) — We traverse the array once. HashMap lookup and insertion take O(1) average time.
- **Space Complexity:** O(n) — In the worst case, the HashMap can store up to O(n) different prefix sums.

## Pattern

**Prefix Sum + HashMap**

Use this pattern when:
- A problem asks for a contiguous subarray with an equal number of two types of elements.
- You can convert one type to `+1` and the other to `-1`.
- You need the longest subarray whose sum is zero.

**Important idea:**

```python
# 1 contributes +1
# 0 contributes -1

if prefix_sum in seen:
    length = i - seen[prefix_sum]
else:
    seen[prefix_sum] = i
```

**Key takeaway:** When a prefix sum repeats, the subarray between its two occurrences has a sum of zero. For this problem, that means an equal number of zeros and ones.
