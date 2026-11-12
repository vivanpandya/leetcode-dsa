# 35. Search Insert Position

[LeetCode Problem](https://leetcode.com/problems/search-insert-position/)  
**Difficulty:** Easy  
**Topics:** Array, Binary Search

---

## Question

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

### Example 1

```text
Input: nums = [1,3,5,6], target = 5
Output: 2
```

### Example 2

```text
Input: nums = [1,3,5,6], target = 2
Output: 1
```

### Example 3

```text
Input: nums = [1,3,5,6], target = 7
Output: 4
```

### Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`

---

## 1. Approach – Binary Search

The array is already sorted, so we can use **Binary Search** to find the correct position in `O(log n)` time.

The key idea is to find the **first index where the element is greater than or equal to the target**.

We use two pointers:

- `left = 0`: beginning of the search range.
- `right = len(nums)`: end boundary of the search range (exclusive).

At each iteration:

- If `nums[mid] < target`, the target belongs after `mid`, so move `left` to `mid + 1`.
- Otherwise, the target belongs at `mid` or before it, so move `right` to `mid`.

When the loop ends, `left` is the correct insertion position. If the target exists, this is also its index.

## 2. Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(nums)`.
3. Continue while `left < right`.
4. Calculate `mid = (left + right) // 2`.
5. If `nums[mid] < target`, update `left = mid + 1`.
6. Otherwise, update `right = mid`.
7. When the loop ends, return `left`.

## 3. Code

```python
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
```

## 4. Example / Dry Run

**Input:**

```python
nums = [1, 3, 5, 6]
target = 2
```

| Iteration | left | right | mid | nums[mid] | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 4 | 2 | 5 | `5 >= 2`, set `right = 2` |
| 2 | 0 | 2 | 1 | 3 | `3 >= 2`, set `right = 1` |
| 3 | 0 | 1 | 0 | 1 | `1 < 2`, set `left = 1` |

Now `left == right == 1`, so the loop stops.

**Output:**

```python
1
```

The target `2` should be inserted at index `1`, between `1` and `3`.

### Another Quick Example

```python
nums = [1, 3, 5, 6]
target = 7
```

All elements are smaller than `7`, so `left` moves to the end of the array.

**Output:**

```python
4
```

The target should be inserted after the last element.

## 5. Why This Works

The array is sorted in ascending order.

- If `nums[mid] < target`, the insertion position must be after `mid`. Therefore, we safely discard the range from `left` through `mid`.
- If `nums[mid] >= target`, `mid` could be the answer, or the correct position could be earlier. Therefore, we keep `mid` by setting `right = mid`.

The search ends when `left` and `right` meet. This index is the first position whose value is not smaller than the target. If no such element exists, it is `len(nums)`, the position immediately after the array.

## 6. Complexity Analysis

- **Time Complexity: O(log n)** — The search range is approximately halved in every iteration.
- **Space Complexity: O(1)** — Only a fixed number of variables are used.

## 7. Pattern

**Pattern:** Binary Search – Lower Bound / First Element Greater Than or Equal to Target

This is slightly different from the usual exact-match Binary Search:

| Problem | Main goal |
|---|---|
| 704. Binary Search | Find the exact target |
| 35. Search Insert Position | Find the first position where value is `>= target` |
| 278. First Bad Version | Find the first version satisfying a condition |

### Important Pointer Updates

```python
if nums[mid] < target:
    left = mid + 1
else:
    right = mid
```

**Remember:** We use `right = len(nums)` and `while left < right` because the answer may be `len(nums)` when the target is greater than every element.
