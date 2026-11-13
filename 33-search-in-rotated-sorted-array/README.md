# 33. Search in Rotated Sorted Array

[LeetCode Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**Difficulty:** Medium  
**Topics:** Array, Binary Search

---

## Question

There is an integer array `nums` sorted in ascending order with distinct values.

Before being passed to the function, `nums` may be left-rotated at an unknown index. For example, `[0,1,2,4,5,6,7]` may become `[4,5,6,7,0,1,2]` after being rotated by 3 positions.

Given the rotated array and an integer `target`, return the index of `target` if it exists. Otherwise, return `-1`.

You must solve the problem in **O(log n)** time.

### Example 1

```text
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2

```text
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3

```text
Input: nums = [1], target = 0
Output: -1
```

### Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values in `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

---

## 1. Approach – Modified Binary Search

A rotated sorted array is made of two sorted parts. Even though the entire array is not sorted, **at least one half of the current search range is always sorted**.

At every iteration:

1. Calculate the middle index.
2. If `nums[mid]` is the target, return `mid`.
3. Check which half is sorted.
4. Decide whether the target can lie inside that sorted half.
5. Discard the half that cannot contain the target.

### How to identify the sorted half

- If `nums[left] <= nums[mid]`, the **left half** is sorted.
  - If `nums[left] <= target < nums[mid]`, search the left half.
  - Otherwise, search the right half.
- Otherwise, the **right half** is sorted.
  - If `nums[mid] < target <= nums[right]`, search the right half.
  - Otherwise, search the left half.

Because all values are distinct, these range checks identify the correct side.

---

## 2. Algorithm

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. If `nums[mid] == target`, return `mid`.
   3. If `nums[left] <= nums[mid]`, the left half is sorted:
      - If `nums[left] <= target < nums[mid]`, set `right = mid - 1`.
      - Otherwise, set `left = mid + 1`.
   4. Otherwise, the right half is sorted:
      - If `nums[mid] < target <= nums[right]`, set `left = mid + 1`.
      - Otherwise, set `right = mid - 1`.
3. If the loop finishes, return `-1`.

---

## 3. Code

```python
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check whether the left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, the right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

---

## 4. Example / Dry Run

**Input:**

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

| Iteration | left | right | mid | nums[mid] | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 7 | Left half `[4,5,6,7]` is sorted. `0` is not in its target range, so search right. |
| 2 | 4 | 6 | 5 | 1 | Left half `[0,1]` is sorted. `0` is in this range, so search left. |
| 3 | 4 | 4 | 4 | 0 | Target found. |

**Output:**

```python
4
```

The target `0` is found at index `4`.

### Another Example – Target Not Found

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
```

The algorithm keeps discarding the half that cannot contain `3`. Eventually, `left` becomes greater than `right`, meaning the search range is empty.

**Output:**

```python
-1
```

---

## 5. Why This Works

A rotation splits the original sorted array into two individually sorted sections.

For any current search range, at least one side of the middle element is sorted. We can use the sorted side's boundary values to determine whether the target belongs there.

- If the target is inside the sorted half's value range, the other half can be discarded.
- If it is outside that range, the sorted half can be discarded.

This guarantees that the target's possible location is never removed. Each iteration reduces the search interval, so the algorithm eventually finds the target or determines that it is absent.

---

## 6. Complexity Analysis

- **Time Complexity: O(log n)** – The search range is approximately halved in every iteration.
- **Space Complexity: O(1)** – Only a fixed number of variables are used.

---

## 7. Pattern

**Pattern:** Modified Binary Search – Search in a Rotated Sorted Array

| Problem | Main idea |
|---|---|
| 704. Binary Search | Search for an exact target in a sorted array. |
| 35. Search Insert Position | Find the first position where the value is greater than or equal to the target. |
| 278. First Bad Version | Find the first version satisfying a condition. |
| 34. Find First and Last Position | Use two binary searches to find the target's boundaries. |
| 33. Search in Rotated Sorted Array | Identify the sorted half and decide which side may contain the target. |

### Important Conditions to Remember

```python
# Is the left half sorted?
if nums[left] <= nums[mid]:

    # Is the target inside the sorted left half?
    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1

# Otherwise, the right half is sorted
else:

    # Is the target inside the sorted right half?
    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

**Remember:** Do not apply ordinary binary search directly to the whole rotated array. First identify which half is sorted, then decide where the target can be.
