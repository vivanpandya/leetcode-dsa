# 1608. Special Array With X Elements Greater Than or Equal X

[LeetCode Problem](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Topics
- Array
- Sorting
- Binary Search

---

## 1. Problem Statement

You are given an array of non-negative integers `nums`.

The array is called **special** if there exists an integer `x` such that exactly `x` elements in `nums` are greater than or equal to `x`.

The value `x` does not need to be an element of `nums`.

Return `x` if the array is special. Otherwise, return `-1`.

It is guaranteed that if a valid `x` exists, it is unique.

### Example 1

**Input:**
```python
nums = [3, 5]
```

**Output:**
```python
2
```

**Explanation:** Exactly two numbers (`3` and `5`) are greater than or equal to `2`.

### Example 2

**Input:**
```python
nums = [0, 0]
```

**Output:**
```python
-1
```

**Explanation:** No value of `x` satisfies the condition.

### Example 3

**Input:**
```python
nums = [0, 4, 3, 0, 4]
```

**Output:**
```python
3
```

**Explanation:** Exactly three numbers are greater than or equal to `3`.

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

---

## 2. Approach: Sorting + Linear Scan

We need to find a number `x` such that exactly `x` elements in the array are greater than or equal to `x`.

First, sort `nums` in ascending order.

After sorting, smaller values appear at the beginning and larger values appear at the end.

For every index `i`, calculate:

```python
x = n - i
```

Here:
- `n` is the total number of elements.
- `i` is the current index.
- `n - i` is the number of elements from index `i` to the end.

Because the array is sorted, every element from index `i` onward is greater than or equal to `nums[i]`.

We need to check two conditions:

```python
nums[i] >= x
```

The current element must be at least `x`, so all `x` elements from index `i` onward are also at least `x`.

```python
i == 0 or nums[i - 1] < x
```

The previous element must be smaller than `x`. This ensures that exactly `x` elements meet the condition, not more.

If both conditions are true, return `x`.

If no index satisfies both conditions, return `-1`.

---

## 3. Algorithm

1. Sort `nums` in ascending order.
2. Calculate `n = len(nums)`.
3. Traverse the array using index `i` from `0` to `n - 1`.
4. For each index, calculate:
   ```python
   x = n - i
   ```
5. Check whether:
   - `nums[i] >= x`
   - `i == 0 or nums[i - 1] < x`
6. If both conditions are true, return `x`.
7. If the loop finishes without finding a valid value, return `-1`.

---

## 4. Python Code

This is the exact code used for submission:

```python
class Solution:
    def specialArray(self, nums):
        nums.sort()

        n = len(nums)

        for i in range(n):
            x = n - i

            if nums[i] >= x and (i == 0 or nums[i - 1] < x):
                return x

        return -1
```

---

## 5. Dry Run

**Input:**
```python
nums = [0, 4, 3, 0, 4]
```

### Step 1: Sort the array

```python
nums = [0, 0, 3, 4, 4]
```

The length is:

```text
n = 5
```

### Step 2: Traverse the array

For each index, calculate `x = n - i` and check the two conditions.

| `i` | `nums[i]` | `x = n - i` | `nums[i] >= x` | Previous element `< x` | Result |
|---:|---:|---:|---|---|---|
| 0 | 0 | 5 | False | Not needed | Continue |
| 1 | 0 | 4 | False | `0 < 4` is True | Continue |
| 2 | 3 | 3 | True | `0 < 3` is True | Return `3` |

At index `2`:

```text
x = 5 - 2
x = 3
```

Check the conditions:

```text
nums[2] >= x
3 >= 3  -> True

nums[1] < x
0 < 3   -> True
```

Both conditions are true, so return `3`.

**Output:**
```python
3
```

### Why do we check the previous element?

Suppose the sorted array is:

```python
nums = [1, 3, 3, 4]
```

At index `1`, `x = 3`.

There are three elements from index `1` onward, and all three are at least `3`.

The previous element is `1`, which is smaller than `3`. Therefore, exactly three elements satisfy the condition.

The previous-element check confirms that the count is exactly `x`.

---

## 6. Why This Works

After sorting, all elements greater than or equal to a particular value are grouped together at the end of the array.

At index `i`, there are exactly `n - i` elements from that index to the end.

We choose this count as the candidate `x`.

- `nums[i] >= x` guarantees that all elements from index `i` onward are at least `x`.
- `i == 0 or nums[i - 1] < x` guarantees that no element before index `i` is also at least `x`.

Together, these conditions prove that exactly `x` elements are greater than or equal to `x`.

Therefore, returning `x` is correct. If no index satisfies both conditions, no valid `x` exists, so we return `-1`.

---

## 7. Complexity Analysis

Let `n` be the length of `nums`.

| Operation | Time Complexity |
|---|---|
| Sorting `nums` | `O(n log n)` |
| Traversing the array | `O(n)` |
| Checking each candidate | `O(1)` |

**Total Time Complexity:**

```text
O(n log n)
```

Sorting is the dominant operation.

**Auxiliary Space Complexity:**

```text
O(1)
```

The algorithm uses only a constant number of extra variables, excluding any temporary memory used internally by Python's sorting implementation.

---

## 8. Pattern and Related Problems

**Pattern: Sorting + Counting Elements**

Recognize this pattern when:
- You need to find a value based on how many array elements satisfy a condition.
- Sorting makes qualifying elements appear together.
- The number of qualifying elements can be calculated using an index.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| H-Index II | 275 | Binary Search on Sorted Array |
| Find Smallest Letter Greater Than Target | 744 | Binary Search |
| Special Array With X Elements Greater Than or Equal X | 1608 | Sorting + Counting |
| H-Index | 274 | Sorting + Counting |

### Important Lines to Remember

Calculate how many elements are in the suffix:

```python
x = n - i
```

Check that the current and all following elements are at least `x`, while the previous element is smaller:

```python
if nums[i] >= x and (i == 0 or nums[i - 1] < x):
    return x
```
