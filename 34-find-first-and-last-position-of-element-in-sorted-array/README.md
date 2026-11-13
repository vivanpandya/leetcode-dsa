# 34. Find First and Last Position of Element in Sorted Array

[LeetCode Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

**Difficulty:** Medium  
**Topics:** Array, Binary Search

---

## Question

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with **O(log n)** runtime complexity.

### Example 1

```text
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2

```text
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3

```text
Input: nums = [], target = 0
Output: [-1,-1]
```

### Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

---

## 1. Approach – Two Binary Searches

A normal Binary Search finds an occurrence of the target, but this problem asks for both the **first** and **last** occurrence.

We solve it by performing Binary Search twice:

1. **First search:** Find the first index where `nums[index] == target`.
2. **Second search:** Find the last index where `nums[index] == target`.

When the middle element equals the target:

- During the first search, save `mid` and continue searching to the **left**. There may be an earlier occurrence.
- During the second search, save `mid` and continue searching to the **right**. There may be a later occurrence.

If the target does not exist, the corresponding index remains `-1`.

This works with non-decreasing arrays, including arrays containing duplicate values.

---

## 2. Algorithm

### First Binary Search – Find the First Occurrence

1. Initialize `first = -1`.
2. Set `left = 0` and `right = len(nums) - 1`.
3. While `left <= right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] == target`:
     - Store `mid` in `first`.
     - Continue searching left using `right = mid - 1`.
   - If `nums[mid] < target`, search right using `left = mid + 1`.
   - Otherwise, search left using `right = mid - 1`.

### Second Binary Search – Find the Last Occurrence

1. Initialize `last = -1`.
2. Reset `left = 0` and `right = len(nums) - 1`.
3. While `left <= right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] == target`:
     - Store `mid` in `last`.
     - Continue searching right using `left = mid + 1`.
   - If `nums[mid] < target`, search right using `left = mid + 1`.
   - Otherwise, search left using `right = mid - 1`.

4. Return `[first, last]`.

---

## 3. Python Code

```python
class Solution:
    def searchRange(self, nums, target):

        first = -1
        left = 0
        right = len(nums) - 1

        # Find the first occurrence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        last = -1
        left = 0
        right = len(nums) - 1

        # Find the last occurrence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return [first, last]
```

---

## 4. Example / Dry Run

**Input:**

```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
```

### Search 1 – Find the First Occurrence

| Iteration | `left` | `right` | `mid` | `nums[mid]` | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 5 | 2 | 7 | `7 < 8`, move right |
| 2 | 3 | 5 | 4 | 8 | Found; save `first = 4`, search left |
| 3 | 3 | 3 | 3 | 8 | Found; save `first = 3`, search left |

Now `left = 3` and `right = 2`, so the loop stops.

**First occurrence = 3**

### Search 2 – Find the Last Occurrence

| Iteration | `left` | `right` | `mid` | `nums[mid]` | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 5 | 2 | 7 | `7 < 8`, move right |
| 2 | 3 | 5 | 4 | 8 | Found; save `last = 4`, search right |
| 3 | 5 | 5 | 5 | 10 | `10 > 8`, search left |

Now `left = 5` and `right = 4`, so the loop stops.

**Last occurrence = 4**

### Final Output

```python
[3, 4]
```

The target `8` appears at indices `3` and `4`.

### Example When the Target Is Missing

```python
nums = [5, 7, 7, 8, 8, 10]
target = 6
```

Neither search finds the target, so `first` and `last` both remain `-1`.

```python
[-1, -1]
```

The same code also handles an empty array because `right` starts at `-1`, so both loops are skipped.

---

## 5. Why This Works

The array is sorted in non-decreasing order. This allows Binary Search to eliminate half of the remaining search range after every comparison.

For the first occurrence:

- When `nums[mid] == target`, `mid` is a possible answer.
- We save it and continue searching left to check whether an earlier occurrence exists.

For the last occurrence:

- When `nums[mid] == target`, `mid` is a possible answer.
- We save it and continue searching right to check whether a later occurrence exists.

Because we keep the best candidate every time we find the target, the final saved indices are the first and last positions.

If the target never appears, the initial values `-1` are returned.

---

## 6. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity: O(log n)** – We perform two Binary Searches. Each takes O(log n), so the total is O(2 log n), which simplifies to O(log n).
- **Space Complexity: O(1)** – We use only a fixed number of variables and do not create an additional data structure.

---

## 7. Pattern

**Pattern: Binary Search – First and Last Occurrence / Boundary Search**

| LeetCode Problem | Main Binary Search idea |
|---|---|
| 704. Binary Search | Find an exact target |
| 35. Search Insert Position | Find the first position with value `>= target` |
| 278. First Bad Version | Find the first version satisfying a condition |
| **34. Find First and Last Position** | Find both boundaries of a target's range |

### Important Pointer Updates

```python
# First occurrence: keep searching LEFT
if nums[mid] == target:
    first = mid
    right = mid - 1

# Last occurrence: keep searching RIGHT
if nums[mid] == target:
    last = mid
    left = mid + 1
```

**Remember:**

- First occurrence → save the index, then move `right` left.
- Last occurrence → save the index, then move `left` right.
- Use `while left <= right` because the current index must still be checked.
- Initialize both answers to `-1` so missing targets are handled correctly.

The key idea is to use Binary Search not just to find a target, but to find the **boundaries** of its repeated occurrences.
