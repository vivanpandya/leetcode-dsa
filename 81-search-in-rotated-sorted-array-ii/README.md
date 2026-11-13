# 81. Search in Rotated Sorted Array II

[LeetCode Problem](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

**Difficulty:** Medium  
**Topics:** Array, Binary Search

---

## Question

Given an integer array `nums` sorted in non-decreasing order, the array may be rotated at an unknown pivot. Unlike the original rotated-array problem, `nums` may contain **duplicate values**.

Given `nums` after rotation and an integer `target`:

- Return `True` if `target` exists in `nums`.
- Return `False` otherwise.

You should reduce the number of operations as much as possible.

### Example 1

```text
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: True
```

### Example 2

```text
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: False
```

### Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`

---

## 1. Approach – Modified Binary Search with Duplicate Handling

This problem is similar to **LeetCode 33 – Search in Rotated Sorted Array**, but duplicates are allowed.

In a rotated sorted array, at least one half around the middle is sorted. We use that sorted half to decide which side may contain the target.

However, duplicates can make it impossible to identify the sorted half.

For example:

```python
nums = [1, 0, 1, 1, 1]
```

If:

```python
nums[left] == nums[mid] == nums[right]
```

we cannot tell which side contains the rotation point. In this situation, safely shrink the search range from both ends:

```python
left += 1
right -= 1
```

Otherwise, use the same sorted-half logic as LeetCode 33.

### Three Cases

**Case 1 – Target found**

If `nums[mid] == target`, return `True`.

**Case 2 – Duplicates make the sorted half unclear**

If `nums[left] == nums[mid] == nums[right]`, move both boundaries inward:

```python
left += 1
right -= 1
```

**Case 3 – One half can be identified as sorted**

If `nums[left] <= nums[mid]`, the left half is sorted:

- If `nums[left] <= target < nums[mid]`, search left.
- Otherwise, search right.

If the left half is not sorted, the right half is sorted:

- If `nums[mid] < target <= nums[right]`, search right.
- Otherwise, search left.

---

## 2. Algorithm

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. Continue while `left <= right`.
3. Calculate `mid = (left + right) // 2`.
4. If `nums[mid] == target`, return `True`.
5. If `nums[left] == nums[mid] == nums[right]`:
   - Increment `left`.
   - Decrement `right`.
6. Otherwise, check whether the left half is sorted:
   - If `nums[left] <= nums[mid]`:
     - If `nums[left] <= target < nums[mid]`, set `right = mid - 1`.
     - Otherwise, set `left = mid + 1`.
7. If the left half is not sorted, the right half is sorted:
   - If `nums[mid] < target <= nums[right]`, set `left = mid + 1`.
   - Otherwise, set `right = mid - 1`.
8. If the loop finishes without finding the target, return `False`.

---

## 3. Python Code

```python
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Duplicates make it unclear which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Check whether the left half is sorted
            elif nums[left] <= nums[mid]:
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

        return False
```

---

## 4. Example / Dry Run

**Input:**

```python
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

| Iteration | left | right | mid | nums[mid] | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 0 | Target found |

**Output:**

```python
True
```

### Dry Run – Duplicate Handling

Use an example where the duplicate condition is triggered:

```python
nums = [1, 0, 1, 1, 1]
target = 0
```

| Iteration | left | right | mid | nums[left], nums[mid], nums[right] | Decision |
|---|---:|---:|---:|---|---|
| 1 | 0 | 4 | 2 | 1, 1, 1 | All equal; shrink both boundaries |
| 2 | 1 | 3 | 2 | 0, 1, 1 | Left half sorted; target is in it |
| 3 | 1 | 1 | 1 | 0, 0, 0 | Target found |

**Output:**

```python
True
```

### Example When the Target Is Missing

```python
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
```

The algorithm keeps eliminating ranges that cannot contain `3`. Eventually, `left` becomes greater than `right`.

**Output:**

```python
False
```

---

## 5. Why This Works

When the values are distinct, we can always identify the sorted half by comparing the boundary and middle values.

With duplicates, that comparison can become ambiguous. If the left, middle, and right values are all equal, either half might contain the rotation point. Removing one value from each end is safe because both values are equal, and we already checked whether the middle value is the target.

When the values are not all equal, we can identify a sorted half and use its value range to determine which side may contain the target.

The algorithm never discards a range that could contain the target.

---

## 6. Complexity Analysis

Let `n` be the number of elements in `nums`.

- **Average Time Complexity: O(log n)** – When duplicates do not frequently make the sorted half ambiguous, Binary Search removes approximately half the search range each iteration.
- **Worst-Case Time Complexity: O(n)** – If many duplicate values occur at the boundaries, the algorithm may only shrink the range by one element from each side per iteration.
- **Space Complexity: O(1)** – Only a fixed number of variables are used.

### Follow-up – How Do Duplicates Affect Runtime?

Yes, duplicates can affect the runtime.

Consider:

```python
nums = [1, 1, 1, 1, 1, 1, 1]
target = 2
```

Here, the left, middle, and right values are repeatedly equal. We cannot determine which half is sorted, so we shrink the boundaries gradually instead of eliminating half the array.

That is why the worst-case time complexity becomes **O(n)** instead of O(log n).

---

## 7. Pattern

**Pattern:** Modified Binary Search – Rotated Sorted Array with Duplicates

| Problem | Main idea |
|---|---|
| 704. Binary Search | Search for an exact target in a sorted array. |
| 33. Search in Rotated Sorted Array | Identify the sorted half and search the possible side. |
| **81. Search in Rotated Sorted Array II** | Modified Binary Search with duplicate handling. |

### Important Conditions to Remember

```python
# If duplicates make the sorted half unclear
if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1

# Otherwise, check which half is sorted
elif nums[left] <= nums[mid]:
    # Left half is sorted
    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1
else:
    # Right half is sorted
    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

**Remember the difference between LeetCode 33 and 81:**

| Feature | LeetCode 33 | LeetCode 81 |
|---|---|---|
| Duplicates | Not allowed | Allowed |
| Return type | Index or `-1` | `True` or `False` |
| Time complexity | O(log n) | Average O(log n), worst O(n) |
| Extra duplicate check | Not needed | Required |

The key lesson: duplicates can hide the rotation boundary. When the boundary and middle values are equal, shrink both ends safely and continue searching.
