# LeetCode 15 — 3Sum

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting  
**LeetCode:** https://leetcode.com/problems/3sum/

---

## 1. Question

Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are distinct indices.
- `nums[i] + nums[j] + nums[k] == 0`.
- The answer does not contain duplicate triplets.

The order of the output and the order of the triplets do not matter.

## 2. Examples

### Example 1

**Input**
```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output**
```python
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation:** The distinct triplets `[-1, -1, 2]` and `[-1, 0, 1]` both sum to zero.

### Example 2

**Input**
```python
nums = [0, 1, 1]
```

**Output**
```python
[]
```

**Explanation:** No three elements sum to zero.

### Example 3

**Input**
```python
nums = [0, 0, 0]
```

**Output**
```python
[[0, 0, 0]]
```

**Explanation:** The three zeros sum to zero. The triplet is included only once.

## 3. Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## 4. Approach

Use **Sorting + Two Pointers**.

1. Sort the array.
2. Fix one number at index `i`.
3. Search for two other numbers whose sum is `-nums[i]` using `left` and `right` pointers.
4. If the total is zero, save the triplet.
5. Skip repeated values for the fixed number and both pointers so the result contains only unique triplets.

Because the array is sorted:
- If the sum is too small, move `left` forward to increase it.
- If the sum is too large, move `right` backward to decrease it.

## 5. Algorithm

1. Sort `nums`.
2. Create an empty list `result`.
3. Loop through `i` from `0` to `n - 3`.
   - If `nums[i] > 0`, stop: all following numbers are also positive.
   - If `i > 0` and `nums[i] == nums[i - 1]`, skip this fixed value.
4. Set `left = i + 1` and `right = n - 1`.
5. While `left < right`:
   - Calculate `total = nums[i] + nums[left] + nums[right]`.
   - If `total == 0`, append the triplet, then move both pointers and skip duplicates.
   - If `total < 0`, increment `left`.
   - Otherwise, decrement `right`.
6. Return `result`.

## 6. Python Code

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

## 7. Dry Run

**Input:** `nums = [-1, 0, 1, 2, -1, -4]`

After sorting:

`nums = [-4, -1, -1, 0, 1, 2]`

| Fixed number | Left value | Right value | Sum | Action |
|---:|---:|---:|---:|---|
| -4 | -1 | 2 | -3 | Sum too small; move `left` |
| -4 | -1 | 2 | -3 | Sum too small; move `left` |
| -4 | 0 | 2 | -2 | Sum too small; move `left` |
| -4 | 1 | 2 | -1 | Sum too small; move `left` |
| -1 | -1 | 2 | 0 | Add `[-1, -1, 2]` |
| -1 | 0 | 1 | 0 | Add `[-1, 0, 1]` |

When the next fixed number is the duplicate `-1`, it is skipped to avoid repeating the same triplets.

**Output**
```python
[[-1, -1, 2], [-1, 0, 1]]
```

## 8. Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n^2)` — sorting takes `O(n log n)`, and the two-pointer scan is `O(n)` for each fixed index.
- **Auxiliary Space Complexity:** Typically `O(1)` for the search itself, excluding sorting implementation details and the output list.

## Pattern

**Sorting + Two Pointers + Duplicate Skipping**

This pattern is useful for finding unique triplets whose sum equals a target. The same approach extends to problems such as **3Sum Closest** and **4Sum**.
