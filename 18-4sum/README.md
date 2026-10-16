# LeetCode 18 — 4Sum

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting  
**LeetCode:** https://leetcode.com/problems/4sum/

---

## 1. Question

Given an integer array `nums` and an integer `target`, return all **unique quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:

- All four indices are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`.
- The result contains no duplicate quadruplets.

The answer may be returned in any order.

## 2. Examples

### Example 1

**Input**
```python
nums = [1, 0, -1, 0, -2, 2]
target = 0
```

**Output**
```python
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

### Example 2

**Input**
```python
nums = [2, 2, 2, 2, 2]
target = 8
```

**Output**
```python
[[2, 2, 2, 2]]
```

## 3. Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## 4. Approach

Use **Sorting + Two Pointers**.

1. Sort the array.
2. Fix the first number using index `i`.
3. Fix the second number using index `j`.
4. Search for the remaining two numbers using `left` and `right` pointers.
5. If the four-number sum equals `target`, save the quadruplet.
6. Skip duplicate values for `i`, `j`, `left`, and `right` so the result contains only unique quadruplets.
7. Since the numbers can be very large or very small, Python integers safely handle the sum.

## 5. Algorithm

1. Sort `nums` and initialize `result = []`.
2. Loop `i` from `0` to `n - 4`.
   - If `i > 0` and `nums[i] == nums[i - 1]`, skip this duplicate.
3. Loop `j` from `i + 1` to `n - 3`.
   - If `j > i + 1` and `nums[j] == nums[j - 1]`, skip this duplicate.
4. Set `left = j + 1` and `right = n - 1`.
5. While `left < right`:
   - Calculate the sum of `nums[i]`, `nums[j]`, `nums[left]`, and `nums[right]`.
   - If the sum equals `target`, append the quadruplet, move both pointers, and skip duplicates.
   - If the sum is smaller than `target`, increment `left`.
   - If the sum is larger than `target`, decrement `right`.
6. Return `result`.

## 6. Python Code

```python
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i], nums[j], nums[left], nums[right]
                        ])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
```

## 7. Dry Run

**Input:** `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`

After sorting:

`nums = [-2, -1, 0, 0, 1, 2]`

| Fixed `i` | Fixed `j` | Left | Right | Sum | Action |
|---:|---:|---:|---:|---:|---|
| -2 | -1 | 0 | 2 | -1 | Sum too small; move `left` |
| -2 | -1 | 0 | 2 | -1 | Continue moving `left` |
| -2 | -1 | 1 | 2 | 0 | Add `[-2, -1, 1, 2]` |
| -2 | 0 | 0 | 2 | 0 | Add `[-2, 0, 0, 2]` |
| -1 | 0 | 0 | 1 | 0 | Add `[-1, 0, 0, 1]` |

**Output**
```python
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

## 8. Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n^3)` — two fixed-number loops and a linear two-pointer scan.
- **Auxiliary Space Complexity:** Typically `O(1)` for the search itself, excluding sorting implementation details and the output list.

## Pattern

**Sorting + Two Pointers + Duplicate Skipping**

This pattern extends 3Sum by fixing two numbers and searching for the remaining pair. It is useful for finding unique quadruplets whose sum equals a target.
