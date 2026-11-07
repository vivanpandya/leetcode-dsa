# 238. Product of Array Except Self

[LeetCode Problem](https://leetcode.com/problems/product-of-array-except-self/)  
**Difficulty:** Medium  
**Pattern:** Prefix Product + Suffix Product

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is the product of all elements of `nums` except `nums[i]`.

The algorithm must run in `O(n)` time and must not use division. The follow-up asks for `O(1)` auxiliary space, excluding the output array.

## Examples

### Example 1

```text
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

### Example 2

```text
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- Every `answer[i]` is guaranteed to fit in a 32-bit integer.

---

## Approach: Prefix Product + Suffix Product

For each index `i`, we need the product of all elements to its left multiplied by the product of all elements to its right.

### Prefix product

The prefix product is the product of all elements before the current index.

For `nums = [1, 2, 3, 4]`, the prefix products are:

```text
[1, 1, 2, 6]
```

The first value is `1` because there are no elements to the left of index `0`.

### Suffix product

The suffix product is the product of all elements after the current index.

For the same input, the suffix products are:

```text
[24, 12, 4, 1]
```

The last value is `1` because there are no elements to the right of the last index.

Multiplying the two arrays gives:

```text
Prefix: [1, 1, 2, 6]
Suffix: [24, 12, 4, 1]
Answer: [24, 12, 8, 6]
```

We can achieve `O(1)` auxiliary space by storing prefix products directly in the output array, then multiplying suffix products into it during a reverse traversal. We do not need separate prefix and suffix arrays.

## Algorithm

1. Create `answer` with `n` elements, all initialized to `1`.
2. Set `prefix = 1`.
3. Traverse from left to right:
   - Store `prefix` in `answer[i]`.
   - Multiply `prefix` by `nums[i]`.
4. Set `suffix = 1`.
5. Traverse from right to left:
   - Multiply `answer[i]` by `suffix`.
   - Multiply `suffix` by `nums[i]`.
6. Return `answer`.

## Python Code

```python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

## Dry Run

Input:

```python
nums = [1, 2, 3, 4]
```

### Pass 1: Build prefix products

Initially:

```text
answer = [1, 1, 1, 1]
prefix = 1
```

| `i` | `nums[i]` | Stored in `answer[i]` | Updated `prefix` |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 3 | 2 | 6 |
| 3 | 4 | 6 | 24 |

After the first pass:

```text
answer = [1, 1, 2, 6]
```

### Pass 2: Multiply suffix products

Set `suffix = 1` and traverse from right to left.

| `i` | `nums[i]` | `answer[i]` before | Multiplication | Updated `suffix` |
|---:|---:|---:|---:|---:|
| 3 | 4 | 6 | `6 * 1 = 6` | 4 |
| 2 | 3 | 2 | `2 * 4 = 8` | 12 |
| 1 | 2 | 1 | `1 * 12 = 12` | 24 |
| 0 | 1 | 1 | `1 * 24 = 24` | 24 |

Final output:

```text
[24, 12, 8, 6]
```

## Why This Works

The first pass stores the product of every element before index `i`. The second pass multiplies it by the product of every element after index `i`.

Therefore, `answer[i]` contains the product of all elements except `nums[i]`.

Zeros are handled naturally because the algorithm uses multiplication rather than division.

## Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Value | Reason |
|---|---|---|
| Time | `O(n)` | Two linear traversals |
| Auxiliary space | `O(1)` | Only `prefix` and `suffix` variables |
| Output space | `O(n)` | Required answer array; excluded from auxiliary space |

## Pattern

**Prefix Product + Suffix Product**

Use this pattern when:
- An answer at each index depends on elements on both sides.
- The current element must be excluded.
- Division is not allowed.
- You need a linear-time solution.

**Key takeaway:** Build prefix products from left to right, then multiply suffix products from right to left. Reusing the output array gives `O(1)` auxiliary space.
