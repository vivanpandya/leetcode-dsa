# 162. Find Peak Element

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-peak-element/)

- **LeetCode:** [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- **Problem Number:** 162
- **Difficulty:** Medium
- **Topics:** Array, Binary Search

---

## 1. Problem Statement

A **peak element** is an element that is strictly greater than its neighboring elements.

Given a 0-indexed integer array `nums`, find a peak element and return its index. If the array contains multiple peaks, you may return the index of **any** peak.

You may imagine that:

```text
nums[-1] = nums[n] = -infinity
```

This means an element at either end of the array is considered greater than a neighbor outside the array.

**Requirement:** The algorithm must run in `O(log n)` time.

## 2. Examples

### Example 1

```text
Input:  nums = [1, 2, 3, 1]
Output: 2
```

**Explanation:** `nums[2] = 3` is greater than both its neighbors, `2` and `1`. Therefore, index `2` is a peak.

### Example 2

```text
Input:  nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

**Explanation:** There are two peaks:
- Index `1`, where the value is `2`.
- Index `5`, where the value is `6`.

Returning either index is correct. The output shown is `5`.

## 3. Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

---

## 4. Approach: Binary Search on the Slope

Normally, binary search is used on a sorted array. In this problem, the array is not necessarily sorted, but we can still use binary search by looking at the **direction of the slope** around the middle index.

Initialize two pointers:

```python
left = 0
right = len(nums) - 1
```

Calculate the middle index:

```python
mid = (left + right) // 2
```

Compare `nums[mid]` with its next element, `nums[mid + 1]`.

There are two cases.

### Case 1: `nums[mid] < nums[mid + 1]`

The slope is increasing. The next element is greater than the middle element. A peak must exist somewhere to the right:

- The values may continue increasing, eventually reaching the right boundary, which is a peak because the outside neighbor is negative infinity.
- Or the values may start decreasing, creating a peak before the decrease.

Therefore, move right:

```python
left = mid + 1
```

### Case 2: `nums[mid] > nums[mid + 1]`

The slope is decreasing. A peak exists at `mid` or somewhere to its left.

We keep `mid` because it may itself be a peak:

```python
right = mid
```

The problem guarantees adjacent elements are different, so these two cases cover every comparison.

### When does the search stop?

Continue while:

```python
left < right
```

When `left == right`, only one index remains. That index is guaranteed to be a peak, so return it.

---

## 5. Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(nums) - 1`.
3. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] < nums[mid + 1]`, set `left = mid + 1`.
   - Otherwise, set `right = mid`.
4. Return `left`.

---

## 6. Python Solution

```python
class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
```

### Code Explanation

| Code | Purpose |
|---|---|
| `left = 0` | Start of the search range |
| `right = len(nums) - 1` | End of the search range |
| `while left < right` | Continue while more than one candidate remains |
| `mid = (left + right) // 2` | Find the middle index |
| `nums[mid] < nums[mid + 1]` | The slope is increasing, so search right |
| `left = mid + 1` | Discard the left part through `mid` |
| `right = mid` | Keep `mid` and search the left part |
| `return left` | Return the index of the peak |

**Important:** `mid + 1` is always a valid index inside the loop. Since `left < right`, the middle index is strictly smaller than `right`, so `mid + 1 <= right`.

---

## 7. Dry Run

Consider Example 1:

```python
nums = [1, 2, 3, 1]
```

Initial values:

```text
left = 0
right = 3
```

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[mid + 1]` | Decision |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0 | 3 | 1 | 2 | 3 | `2 < 3`, so `left = 2` |
| 2 | 2 | 3 | 2 | 3 | 1 | `3 > 1`, so `right = 2` |

Now:

```text
left = 2
right = 2
```

The loop stops because `left < right` is false.

Return:

```python
left  # 2
```

**Output:**

```text
2
```

### Dry Run: Multiple Peaks

Consider Example 2:

```python
nums = [1, 2, 1, 3, 5, 6, 4]
```

The array has peaks at indices `1` and `5`. Binary search may return either one, depending on how the search range is reduced. Both are valid answers.

---

## 8. Why This Works

At every step, we keep a range that is guaranteed to contain at least one peak.

- If `nums[mid] < nums[mid + 1]`, the array is increasing at that point. A peak must exist to the right, so we can discard the range through `mid`.
- If `nums[mid] > nums[mid + 1]`, the array is decreasing at that point. A peak must exist at `mid` or to its left, so we keep `mid` and discard the range to its right.

Each iteration reduces the search interval to at most about half its previous size.

Eventually, `left` and `right` meet at an index that is guaranteed to be a peak.

---

## 9. Complexity Analysis

### Time Complexity: `O(log n)`

Each iteration reduces the search range by approximately half.

Therefore, the number of iterations grows logarithmically with the array size:

```text
O(log n)
```

### Space Complexity: `O(1)`

The algorithm uses only three variables: `left`, `right`, and `mid`. No additional array or recursion is used.

```text
Time:  O(log n)
Space: O(1)
```

---

## 10. Important Edge Cases

### Single element

```python
nums = [1]
```

The loop does not execute. Return index `0`.

### Peak at the beginning

```python
nums = [5, 4, 3, 2, 1]
```

The first element is greater than its only neighbor, so index `0` is a peak.

### Peak at the end

```python
nums = [1, 2, 3, 4, 5]
```

The last element is greater than its only neighbor, so index `4` is a peak.

### Multiple peaks

```python
nums = [1, 2, 1, 3, 5, 6, 4]
```

Indices `1` and `5` are both peaks. Either can be returned.

---

## 11. Pattern Recognition

**Pattern:** Binary Search on the Slope.

Recognize this pattern when:
- The array is not necessarily sorted.
- You need to find a local maximum or peak.
- Adjacent values are different.
- The problem asks for `O(log n)` time.

### Related LeetCode Problems

| Problem | Number | Main idea |
|---|---:|---|
| Binary Search | 704 | Classic binary search |
| Search Insert Position | 35 | Binary search for an insertion position |
| Find Minimum in Rotated Sorted Array | 153 | Modified binary search |
| Find Peak Element | 162 | Binary search using the slope |

---

## 12. Quick Revision

Remember this comparison:

```python
if nums[mid] < nums[mid + 1]:
    left = mid + 1
else:
    right = mid
```

- Increasing slope → move right.
- Decreasing slope → move left, keeping `mid`.
- Stop when `left == right`.
- Return the index `left`, not `nums[left]`.

**Final Complexity:**
- Time: `O(log n)`
- Space: `O(1)`
