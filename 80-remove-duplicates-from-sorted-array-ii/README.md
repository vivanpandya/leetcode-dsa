# LeetCode 80: Remove Duplicates from Sorted Array II

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
[![LeetCode](https://img.shields.io/badge/LeetCode-80-blue)](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

**Problem link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

---

## 1. Question

Given an integer array `nums` sorted in non-decreasing order, remove duplicates **in-place** so that each unique element appears at most twice. Keep the relative order of the elements the same.

If `k` elements remain, place them in the first `k` positions of `nums` and return `k`. Do not allocate another array; use `O(1)` extra memory.

### Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## 2. Examples

### Example 1

```python
nums = [1, 1, 1, 2, 2, 3]
# Return: 5
# First 5 elements: [1, 1, 2, 2, 3]
```

### Example 2

```python
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Return: 7
# First 7 elements: [0, 0, 1, 1, 2, 3, 3]
```

## 3. Approach

Use **Two Pointers** to modify the array in-place.

- `i` scans the input array.
- `k` points to the position where the next valid element should be written.
- The first two elements can always be kept.
- For every later element, keep it only if it differs from `nums[k - 2]`.
- If it equals `nums[k - 2]`, two copies of that value are already in the result, so skip it.

Because the array is sorted, equal values appear next to each other. Comparing with the element two positions behind the write pointer ensures that no value appears more than twice.

## 4. Algorithm

1. If `len(nums) <= 2`, return `len(nums)`.
2. Initialize `k = 2`.
3. Iterate `i` from index `2` to the end of `nums`.
4. If `nums[i] != nums[k - 2]`:
   - Write `nums[i]` at `nums[k]`.
   - Increment `k`.
5. Return `k`.

## 5. Code

```python
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
```

## 6. Dry Run

Input: `nums = [1, 1, 1, 2, 2, 3]`

Initially, the first two elements `[1, 1]` are kept, so `k = 2`.

| `i` | `nums[i]` | `nums[k - 2]` | Action | `k` after action |
|---:|---:|---:|---|---:|
| 2 | 1 | 1 | Skip: two `1`s are already kept | 2 |
| 3 | 2 | 1 | Write `2` at index 2 | 3 |
| 4 | 2 | 1 | Write `2` at index 3 | 4 |
| 5 | 3 | 2 | Write `3` at index 4 | 5 |

The first `k = 5` elements are `[1, 1, 2, 2, 3]`.

**Output:** `5`

## 7. Complexity

- **Time Complexity:** `O(n)` — each element is examined once.
- **Auxiliary Space Complexity:** `O(1)` — the input array is modified in-place, using only a fixed number of variables.

## 8. Pattern

**Two Pointers — In-Place Array Modification**

Use this pattern when working with sorted arrays where you need to remove or limit duplicates without creating another array.
