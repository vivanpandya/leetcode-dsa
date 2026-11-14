# 154. Find Minimum in Rotated Sorted Array II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

- **LeetCode:** [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
- **Problem Number:** 154
- **Difficulty:** Hard
- **Topics:** Array, Binary Search

---

## 1. Problem Statement

Suppose an array of length `n`, sorted in ascending order, is rotated between `1` and `n` times.

For example, the sorted array:

```text
[0, 1, 4, 4, 5, 6, 7]
```

may become:

```text
[4, 5, 6, 7, 0, 1, 4]
```

or:

```text
[0, 1, 4, 4, 5, 6, 7]
```

Given the rotated sorted array `nums`, which may contain **duplicates**, return the minimum element.

The goal is to minimize the number of operations.

## 2. Examples

### Example 1

```text
Input:  nums = [1, 3, 5]
Output: 1
```

### Example 2

```text
Input:  nums = [2, 2, 2, 0, 1]
Output: 0
```

## 3. Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times.
- Duplicate values may be present.

---

## 4. Approach: Modified Binary Search

This problem is very similar to **LeetCode 153 – Find Minimum in Rotated Sorted Array**.

The important difference is that this problem allows duplicate values.

We use two pointers:

```python
left = 0
right = len(nums) - 1
```

Then repeatedly calculate the middle index:

```python
mid = (left + right) // 2
```

Compare `nums[mid]` with `nums[right]`.

There are three possible cases.

### Case 1: `nums[mid] > nums[right]`

The minimum must be in the right part of the current search range, after `mid`.

Update:

```python
left = mid + 1
```

Example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
                 ^
                mid
```

Here, `nums[mid] = 7` and `nums[right] = 2`.

Since `7 > 2`, the minimum is to the right of `mid`.

### Case 2: `nums[mid] < nums[right]`

The part from `mid` to `right` is sorted in ascending order. The minimum is either at `mid` or somewhere to its left.

Update:

```python
right = mid
```

We do not use `mid - 1` because `mid` itself could be the minimum.

### Case 3: `nums[mid] == nums[right]`

This is the extra case caused by duplicates.

Example:

```text
nums = [2, 2, 2, 0, 1]
```

When the middle value and rightmost value are equal, we cannot determine which side contains the minimum just from this comparison.

We safely remove one element from the right:

```python
right -= 1
```

Why is this safe?

Because `nums[mid]` and `nums[right]` are equal. Removing the rightmost element cannot discard the only minimum:

- If their shared value is greater than the minimum, the minimum is elsewhere.
- If their shared value is the minimum, an equal occurrence remains at `mid`.

This step may remove only one element instead of half the search range. That is why duplicates can make the worst-case runtime linear.

---

## 5. Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(nums) - 1`.
3. Run a loop while `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`, set `left = mid + 1`.
   - If `nums[mid] < nums[right]`, set `right = mid`.
   - Otherwise, set `right = right - 1`.
4. When the loop ends, return `nums[left]`.

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

            elif nums[mid] < nums[right]:
                right = mid

            else:
                right -= 1

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
| `left = mid + 1` | Move the left boundary past `mid` |
| `nums[mid] < nums[right]` | Minimum is at `mid` or to its left |
| `right = mid` | Keep `mid` in the search range |
| `nums[mid] == nums[right]` | Comparison is inconclusive because of duplicates |
| `right -= 1` | Safely remove one duplicate candidate from the right |
| `return nums[left]` | Return the remaining minimum |

---

## 7. Dry Run

Consider Example 2:

```python
nums = [2, 2, 2, 0, 1]
```

Initial values:

```text
left = 0
right = 4
```

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[right]` | Decision |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0 | 4 | 2 | 2 | 1 | `2 > 1`, so `left = 3` |
| 2 | 3 | 4 | 3 | 0 | 1 | `0 < 1`, so `right = 3` |

Now:

```text
left = 3
right = 3
```

The loop stops because `left < right` is false.

Return:

```python
nums[left]  # nums[3] = 0
```

**Output:**

```text
0
```

### Dry Run: When Duplicates Make Progress Slower

Consider:

```python
nums = [2, 2, 2, 2, 2]
```

At each iteration, `nums[mid] == nums[right]`, so we execute:

```python
right -= 1
```

The search range shrinks by only one element per iteration. This illustrates why the worst-case time complexity is `O(n)`.

---

## 8. Why This Works

At every iteration, the current search range contains at least one minimum element.

- When `nums[mid] > nums[right]`, the minimum must be after `mid`, so the range can safely move to the right half.
- When `nums[mid] < nums[right]`, the section from `mid` to `right` is sorted, so the minimum is at `mid` or to its left.
- When the values are equal, we cannot identify the correct half. Removing the rightmost element is safe because an equal value remains at `mid`.

The loop ends when `left == right`. The remaining element is the minimum.

---

## 9. Complexity Analysis

### Best / Typical Case: `O(log n)`

When comparisons allow us to discard approximately half of the search range, binary search takes logarithmic time.

### Worst Case: `O(n)`

When many values are equal, the comparison may repeatedly reach:

```python
nums[mid] == nums[right]
```

Then we remove only one element at a time using `right -= 1`.

For an array containing many duplicates, this can require up to `O(n)` operations.

### Space Complexity: `O(1)`

Only a fixed number of variables (`left`, `right`, and `mid`) are used. No extra array or recursion is needed.

```text
Best / typical time: O(log n)
Worst-case time:     O(n)
Space:               O(1)
```

---

## 10. Important Edge Cases

### No rotation / already sorted

```python
nums = [1, 3, 5]
```

Output:

```text
1
```

### Minimum near the middle

```python
nums = [2, 2, 2, 0, 1]
```

Output:

```text
0
```

### All elements are equal

```python
nums = [2, 2, 2, 2, 2]
```

Output:

```text
2
```

This case can take `O(n)` time.

### Single element

```python
nums = [5]
```

Output:

```text
5
```

The loop does not execute.

---

## 11. Follow-Up: Does Allowing Duplicates Affect Runtime?

**Yes.**

In LeetCode 153, all elements are unique. Comparing `nums[mid]` and `nums[right]` tells us which part can be discarded, so the time complexity is always `O(log n)`.

In LeetCode 154, duplicates are allowed. If:

```python
nums[mid] == nums[right]
```

we cannot tell which side contains the minimum. We can only reduce the search range by one element.

Therefore:

- **LeetCode 153:** `O(log n)` time.
- **LeetCode 154:** `O(log n)` in cases where the range can be halved, but `O(n)` in the worst case because of duplicates.

---

## 12. Pattern Recognition

**Pattern:** Modified Binary Search on a Rotated Sorted Array with Duplicates.

Recognize this pattern when:
- The array was originally sorted.
- The array has been rotated.
- Duplicate values may be present.
- You need to find the minimum element.

### Related LeetCode Problems

| Problem | Number | Main idea |
|---|---:|---|
| Search in Rotated Sorted Array | 33 | Search for a target, unique elements |
| Find Minimum in Rotated Sorted Array | 153 | Find minimum, unique elements |
| Search in Rotated Sorted Array II | 81 | Search for a target with duplicates |
| Find Minimum in Rotated Sorted Array II | 154 | Find minimum with duplicates |

### LC 153 vs. LC 154

| Feature | LC 153 | LC 154 |
|---|---|---|
| Duplicates | Not allowed | Allowed |
| Binary search | Yes | Yes, with an extra equality case |
| Equality case | Not needed | `right -= 1` |
| Worst-case time | `O(log n)` | `O(n)` |
| Space | `O(1)` | `O(1)` |

---

## 13. Quick Revision

Remember these three conditions:

```python
if nums[mid] > nums[right]:
    left = mid + 1

elif nums[mid] < nums[right]:
    right = mid

else:
    right -= 1
```

- `nums[mid] > nums[right]` → minimum is to the right.
- `nums[mid] < nums[right]` → minimum is at `mid` or to the left.
- `nums[mid] == nums[right]` → comparison is inconclusive; remove one element from the right.
- Stop when `left == right`.
- Return `nums[left]`.

**Final Complexity:**
- Best / typical time: `O(log n)`
- Worst-case time: `O(n)`
- Space: `O(1)`
