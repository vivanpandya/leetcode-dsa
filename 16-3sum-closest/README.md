# LeetCode 16 — 3Sum Closest

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting  
**LeetCode:** https://leetcode.com/problems/3sum-closest/

---

## 1. Question

You are given an integer array `nums` of length `n` and an integer `target`.

Find three integers at distinct indices in `nums` such that their sum is closest to `target`. Return the sum of those three integers.

The problem guarantees exactly one solution.

## 2. Examples

### Example 1

**Input**
```python
nums = [-1, 2, 1, -4]
target = 1
```

**Output**
```python
2
```

**Explanation:** `-1 + 2 + 1 = 2`, which is closest to target `1`.

### Example 2

**Input**
```python
nums = [0, 0, 0]
target = 1
```

**Output**
```python
0
```

**Explanation:** The only possible three-number sum is `0`.

## 3. Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## 4. Approach

Use **Sorting + Two Pointers**, similar to 3Sum.

1. Sort the array.
2. Fix one number using index `i`.
3. Use `left` and `right` pointers to search for two other numbers.
4. Calculate the sum of the three numbers.
5. If this sum is closer to `target` than the current best sum, update `closest`.
6. If the sum is smaller than `target`, move `left` forward to increase the sum.
7. If the sum is larger than `target`, move `right` backward to decrease the sum.
8. If the sum equals `target`, return immediately because no sum can be closer.

## 5. Algorithm

1. Sort `nums`.
2. Initialize `closest` with the sum of the first three numbers.
3. Loop through each possible fixed index `i` from `0` to `n - 3`.
4. Set `left = i + 1` and `right = n - 1`.
5. While `left < right`:
   - Calculate `total = nums[i] + nums[left] + nums[right]`.
   - If `abs(target - total) < abs(target - closest)`, set `closest = total`.
   - If `total == target`, return `total`.
   - If `total < target`, increment `left`.
   - Otherwise, decrement `right`.
6. Return `closest`.

## 6. Python Code

```python
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - closest):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest
```

## 7. Dry Run

**Input:** `nums = [-1, 2, 1, -4]`, `target = 1`

After sorting:

`nums = [-4, -1, 1, 2]`

| Fixed number | Left value | Right value | Sum | Closest sum |
|---:|---:|---:|---:|---:|
| -4 | -1 | 2 | -3 | -3 |
| -4 | 1 | 2 | -1 | -1 |
| -1 | 1 | 2 | 2 | 2 |

The sum `2` has a difference of `|1 - 2| = 1` from the target. No other sum is closer.

**Output:** `2`

## 8. Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n^2)` — sorting takes `O(n log n)`, and the two-pointer scan takes `O(n)` for each fixed index.
- **Auxiliary Space Complexity:** Typically `O(1)` for the search itself, excluding sorting implementation details.

## Pattern

**Sorting + Two Pointers + Closest Difference**

Use this pattern when finding three numbers whose sum is closest to a target. It builds on the same technique as **3Sum**.
