# 75. Sort Colors

- **LeetCode:** [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
- **Difficulty:** Medium
- **Topics:** Array, Two Pointers, Sorting

## 1. Question

Given an array `nums` containing only `0`, `1`, and `2`, sort it in-place so that the values appear in the order `0`, `1`, and `2`.

- `0` represents red.
- `1` represents white.
- `2` represents blue.

Do not use the built-in sorting function. The goal is a one-pass solution with `O(1)` auxiliary space.

## 2. Example

### Example 1

**Input**
```python
nums = [2, 0, 2, 1, 1, 0]
```

**Output**
```python
[0, 0, 1, 1, 2, 2]
```

**Explanation:** The array contains two `0`s, two `1`s, and two `2`s. Place all `0`s first, then all `1`s, and finally all `2`s.

### Example 2

**Input**
```python
nums = [2, 0, 1]
```

**Output**
```python
[0, 1, 2]
```

### Constraints
- `n == len(nums)`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## 3. Approach

Use the **Dutch National Flag Algorithm** with three pointers:

- `low`: position where the next `0` should go.
- `mid`: current element being examined.
- `high`: position where the next `2` should go.

There are three cases:

1. If `nums[mid] == 0`, swap it with `nums[low]`, then increment `low` and `mid`.
2. If `nums[mid] == 1`, it is already in the correct middle region, so increment `mid`.
3. If `nums[mid] == 2`, swap it with `nums[high]` and decrement `high`. Do **not** increment `mid`, because the swapped-in element has not been examined yet.

## 4. Algorithm

1. Set `low = 0` and `mid = 0`.
2. Set `high = len(nums) - 1`.
3. While `mid <= high`:
   - If `nums[mid] == 0`, swap `nums[low]` and `nums[mid]`, then increment `low` and `mid`.
   - If `nums[mid] == 1`, increment `mid`.
   - Otherwise, swap `nums[mid]` and `nums[high]`, then decrement `high`.
4. Stop when `mid > high`. The array is sorted in-place.

## 5. Code

```python
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

**Note:** LeetCode expects `nums` to be modified in-place. You do not need to return it.

## 6. Dry Run

Input: `nums = [2, 0, 2, 1, 1, 0]`

| Step | `low` | `mid` | `high` | Action | Array |
|---:|---:|---:|---:|---|---|
| 1 | 0 | 0 | 5 | Current value is `2`; swap positions `0` and `5`, decrement `high` | `[0, 0, 2, 1, 1, 2]` |
| 2 | 0 | 0 | 4 | Current value is `0`; swap positions `0` and `0`, increment `low` and `mid` | `[0, 0, 2, 1, 1, 2]` |
| 3 | 1 | 1 | 4 | Current value is `0`; swap positions `1` and `1`, increment `low` and `mid` | `[0, 0, 2, 1, 1, 2]` |
| 4 | 2 | 2 | 4 | Current value is `2`; swap positions `2` and `4`, decrement `high` | `[0, 0, 1, 1, 2, 2]` |
| 5 | 2 | 2 | 3 | Current value is `1`; increment `mid` | `[0, 0, 1, 1, 2, 2]` |
| 6 | 2 | 3 | 3 | Current value is `1`; increment `mid` | `[0, 0, 1, 1, 2, 2]` |

Now `mid > high`, so the loop stops.

**Final array:** `[0, 0, 1, 1, 2, 2]`

## 7. Complexity

- **Time Complexity: `O(n)`** — each element is examined a constant number of times.
- **Auxiliary Space Complexity: `O(1)`** — only three pointers are used; the original list is modified in-place.

## 8. Pattern

**Three Pointers — Dutch National Flag Algorithm**

Use this pattern when:
- An array contains three categories of values.
- Values must be grouped in a specific order.
- The array must be modified in-place.
- The solution needs one pass and constant extra space.

**Related problems:**
- [Move Zeroes — #283](https://leetcode.com/problems/move-zeroes/)
- [Remove Duplicates from Sorted Array — #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [Sort Array By Parity — #905](https://leetcode.com/problems/sort-array-by-parity/)
