# 1991. Find the Middle Index in Array

[LeetCode Problem](https://leetcode.com/problems/find-the-middle-index-in-array/)  
**Difficulty:** Easy  
**Topics:** Array, Prefix Sum

---

## 1. Problem Statement

Given a 0-indexed integer array `nums`, find the **leftmost** `middleIndex` (the smallest valid index).

An index `i` is a middle index if the sum of all elements strictly to its left is equal to the sum of all elements strictly to its right.

If `i == 0`, the left sum is `0`. If `i == len(nums) - 1`, the right sum is `0`.

Return the leftmost valid index, or `-1` if no such index exists.

## 2. Examples

### Example 1

```text
Input:  nums = [2,3,-1,8,4]
Output: 3
```

**Explanation:**

At index `3`:

```text
Left sum  = 2 + 3 + (-1) = 4
Right sum = 4
```

Both sums are equal, so return `3`.

### Example 2

```text
Input:  nums = [1,-1,4]
Output: 2
```

**Explanation:**

At index `2`:

```text
Left sum  = 1 + (-1) = 0
Right sum = 0
```

Both sums are equal, so return `2`.

### Example 3

```text
Input:  nums = [2,5]
Output: -1
```

**Explanation:** No index has equal left and right sums.

## 3. Approach — Total Sum + Running Left Sum

We can solve this problem in one pass after calculating the total sum of the array.

First, calculate:

```python
total_sum = sum(nums)
```

Maintain a variable `left_sum`, initially `0`.

For every index `i`:

- `left_sum` is the sum of elements before index `i`.
- The right sum is the total sum minus the left sum and the current element.

Therefore:

```python
right_sum = total_sum - left_sum - nums[i]
```

If `left_sum == right_sum`, the current index is a valid middle index. Return it immediately.

We scan from left to right, so the first valid index is automatically the **leftmost** one.

If no index works, return `-1`.

## 4. Algorithm

1. Calculate `total_sum = sum(nums)`.
2. Initialize `left_sum = 0`.
3. Traverse the array from index `0` to `len(nums) - 1`:
   - Calculate `right_sum = total_sum - left_sum - nums[i]`.
   - If `left_sum == right_sum`, return `i`.
   - Otherwise, update `left_sum += nums[i]`.
4. If the loop finishes without finding a valid index, return `-1`.

## 5. Python Solution

```python
class Solution:
    def findMiddleIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
```

## 6. Dry Run

Consider:

```python
nums = [2, 3, -1, 8, 4]
```

First calculate:

```text
total_sum = 2 + 3 + (-1) + 8 + 4 = 16
left_sum = 0
```

| Index `i` | `nums[i]` | `left_sum` | `right_sum = total_sum - left_sum - nums[i]` | Equal? |
|---:|---:|---:|---:|:---:|
| 0 | 2 | 0 | 16 - 0 - 2 = 14 | No |
| 1 | 3 | 2 | 16 - 2 - 3 = 11 | No |
| 2 | -1 | 5 | 16 - 5 - (-1) = 12 | No |
| 3 | 8 | 4 | 16 - 4 - 8 = 4 | Yes |

At index `3`:

```text
left_sum  = 2 + 3 + (-1) = 4
right_sum = 4

left_sum == right_sum
```

The function returns immediately.

**Final output:**

```text
3
```

## 7. Why This Works

The total sum consists of three parts at every index:

```text
total_sum = left_sum + nums[i] + right_sum
```

Rearranging:

```text
right_sum = total_sum - left_sum - nums[i]
```

This calculates the sum strictly to the right of the current index.

We compare the two sums at every index. Since we traverse from left to right and return at the first match, the returned index is guaranteed to be the leftmost valid middle index.

## 8. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity: O(n)** — Calculating `sum(nums)` takes O(n), and the loop visits each element at most once.
- **Auxiliary Space Complexity: O(1)** — We use only a constant number of variables and do not create extra arrays.

## 9. Pattern

**Prefix Sum + Running Sum**

Key formula:

```python
right_sum = total_sum - left_sum - nums[i]
```

Remember:

- `left_sum` excludes the current element.
- `right_sum` also excludes the current element.
- Update `left_sum` only after checking the current index.
- Return immediately when a match is found to get the leftmost index.

**Related problem:** [LeetCode 724 — Find Pivot Index](https://leetcode.com/problems/find-pivot-index/).
