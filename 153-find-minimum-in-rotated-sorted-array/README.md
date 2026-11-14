# 153. Find Minimum in Rotated Sorted Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- **LeetCode:** [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **Problem Number:** 153
- **Difficulty:** Medium
- **Topics:** Array, Binary Search

---

## 1. Problem Statement

Suppose an array of length `n`, sorted in ascending order, is rotated between `1` and `n` times.

For example, the sorted array:

```text
[0, 1, 2, 4, 5, 6, 7]
```

may become:

```text
[4, 5, 6, 7, 0, 1, 2]
```

or:

```text
[0, 1, 2, 4, 5, 6, 7]
```

Given the rotated sorted array `nums` containing **unique elements**, return the minimum element.

**Requirement:** The algorithm must run in `O(log n)` time.

## 2. Examples

### Example 1

```text
Input:  nums = [3, 4, 5, 1, 2]
Output: 1
```

**Explanation:** The original array was `[1, 2, 3, 4, 5]`, rotated 3 times.

### Example 2

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

**Explanation:** The original array was `[0, 1, 2, 4, 5, 6, 7]`, rotated 4 times.

### Example 3

```text
Input:  nums = [11, 13, 15, 17]
Output: 11
```

**Explanation:** The original array was `[11, 13, 15, 17]`, rotated 4 times.

## 3. Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers in `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.

---

## 4. Approach: Modified Binary Search

A rotated sorted array consists of two individually sorted parts. The minimum element is the first element of the second part, or the first element itself if the array is still in sorted order.

We can find this element using binary search instead of checking every element.

### Two pointers

Initialize:

```python
left = 0
right = len(nums) - 1
```

Calculate the middle index:

```python
mid = (left + right) // 2
```

Compare `nums[mid]` with `nums[right]`.

### Case 1: `nums[mid] > nums[right]`

The minimum element must be to the **right** of `mid`.

```python
left = mid + 1
```

Example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
                 ^
                mid
```

Here, `nums[mid] = 7` and `nums[right] = 2`. Since `7 > 2`, the minimum is in the right part.

### Case 2: `nums[mid] < nums[right]`

The section from `mid` to `right` is sorted. The minimum is at `mid` or to its **left**.

```python
right = mid
```

We keep `mid` because it could itself be the minimum.

### Why does the loop use `left < right`?

When `left == right`, only one candidate index remains. That index contains the minimum, so the search is complete.

---

## 5. Algorithm

1. Set `left = 0`.
2. Set `right = len(nums) - 1`.
3. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`, set `left = mid + 1`.
   - Otherwise, set `right = mid`.
4. Return `nums[left]`.

---

## 6. Python Solution

```python
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
```

### Code Explanation

| Code | Purpose |
|---|---|
| `left = 0` | Start of the search range |
| `right = len(nums) - 1` | End of the search range |
| `while left < right` | Continue while more than one candidate remains |
| `mid = (left + right) // 2` | Find the middle index |
| `nums[mid] > nums[right]` | Minimum must be after `mid` |
| `left = mid + 1` | Discard the left part including `mid` |
| `right = mid` | Keep `mid` and discard the right part |
| `return nums[left]` | Return the remaining minimum element |

---

## 7. Dry Run

Consider:

```python
nums = [4, 5, 6, 7, 0, 1, 2]
```

Initial values:

```text
left = 0
right = 6
```

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[right]` | Decision |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 7 | 2 | `7 > 2`, so `left = 4` |
| 2 | 4 | 6 | 5 | 1 | 2 | `1 < 2`, so `right = 5` |
| 3 | 4 | 5 | 4 | 0 | 1 | `0 < 1`, so `right = 4` |

Now:

```text
left = 4
right = 4
```

The loop stops because `left < right` is false.

Return:

```python
nums[left]  # nums[4] = 0
```

**Output:**

```text
0
```

---

## 8. Why This Works

At every step, we keep a range that is guaranteed to contain the minimum.

- If `nums[mid] > nums[right]`, the rotation point—and therefore the minimum—must be after `mid`. We can safely discard the left side through `mid`.
- If `nums[mid] < nums[right]`, the part from `mid` through `right` is increasing. The minimum cannot be to the right of `mid`, so we keep `mid` and move `right` to it.

Each step reduces the search range by approximately half. Eventually, `left` and `right` point to the same index, which must contain the minimum.

The array contains unique elements, so equality between `nums[mid]` and `nums[right]` does not need a separate case.

---

## 9. Complexity Analysis

### Time Complexity: `O(log n)`

Each iteration reduces the search range by approximately half.

For an array of size `n`, binary search takes logarithmic time:

```text
O(log n)
```

### Space Complexity: `O(1)`

The algorithm uses only a fixed number of variables (`left`, `right`, and `mid`). It does not create another array or use recursion.

```text
Time:  O(log n)
Space: O(1)
```

---

## 10. Important Edge Cases

### Already sorted array

```python
nums = [11, 13, 15, 17]
```

The algorithm keeps moving `right` toward the beginning and returns `11`.

### Minimum at the last index

```python
nums = [3, 4, 5, 1, 2]
```

The algorithm narrows the range to the index containing `1`.

### Two elements

```python
nums = [2, 1]
```

The algorithm returns `1`.

### Single element

```python
nums = [5]
```

The loop does not execute, and the algorithm returns `5`.

---

## 11. Pattern Recognition

**Pattern:** Modified Binary Search on a Rotated Sorted Array.

Recognize this pattern when:
- The array was originally sorted.
- The array has been rotated.
- You need to find the minimum element.
- The required time complexity is `O(log n)`.

### Related LeetCode Problems

| Problem | Number | Main idea |
|---|---:|---|
| Search in Rotated Sorted Array | 33 | Modified binary search to find a target |
| Find Minimum in Rotated Sorted Array | 153 | Modified binary search to find the minimum |
| Search in Rotated Sorted Array II | 81 | Search with duplicates |
| Find Minimum in Rotated Sorted Array II | 154 | Find minimum with duplicates |

### Key Difference: LC 153 vs. LC 154

- **LC 153:** All elements are unique. Each comparison tells us which side can be discarded, giving `O(log n)` time.
- **LC 154:** Duplicates are allowed. When `nums[mid] == nums[right]`, we may only be able to shrink the range by one, so worst-case time can be `O(n)`.

---

## 12. Quick Revision

Remember these two conditions:

```python
if nums[mid] > nums[right]:
    left = mid + 1
else:
    right = mid
```

- `nums[mid] > nums[right]` → minimum is on the right.
- Otherwise → minimum is at `mid` or on the left.
- Stop when `left == right`.
- Return `nums[left]`.

**Final Complexity:**
- Time: `O(log n)`
- Space: `O(1)`
