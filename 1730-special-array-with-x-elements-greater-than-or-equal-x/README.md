# 1608. Special Array With X Elements Greater Than or Equal X

[LeetCode Problem](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Topics
- Array
- Binary Search
- Sorting

---

## 1. Problem Statement

You are given an array of non-negative integers `nums`.

The array is called **special** if there exists an integer `x` such that **exactly `x` elements** in `nums` are greater than or equal to `x`.

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

## 2. Approach: Sorting + Binary Search

We need to find an integer `x` such that exactly `x` elements are greater than or equal to `x`.

First, sort `nums` in ascending order.

After sorting, if we choose an index `i`, then the number of elements from index `i` to the end is:

```python
count = len(nums) - i
```

Those elements are all greater than or equal to `nums[i]`.

For a candidate `x`, we need to check whether the first position containing a value greater than or equal to `x` leaves exactly `x` elements to its right.

We can use binary search over possible values of `x`, from `0` to `n`, where `n = len(nums)`.

### Why binary search works

Define `count(x)` as the number of elements in `nums` that are greater than or equal to `x`.

As `x` increases, `count(x)` can only stay the same or decrease.

We need:
```text
count(x) == x
```

If `count(x) > x`, the candidate is too small, so search for a larger `x`.

If `count(x) < x`, the candidate is too large, so search for a smaller `x`.

If they are equal, we found the answer.

To calculate `count(x)` efficiently, use a lower-bound binary search on the sorted array to find the first element greater than or equal to `x`.

---

## 3. Algorithm

1. Sort `nums` in ascending order.
2. Set `n = len(nums)`.
3. Initialize the binary search range:
   - `left = 0`
   - `right = n`
4. While `left <= right`:
   1. Calculate `x = (left + right) // 2`.
   2. Use binary search to find the first index `i` where `nums[i] >= x`.
   3. Calculate `count = n - i`.
   4. If `count == x`, return `x`.
   5. If `count > x`, search larger values by setting `left = x + 1`.
   6. Otherwise, search smaller values by setting `right = x - 1`.
5. If no valid value is found, return `-1`.

---

## 4. Python Code

```python
class Solution:
    def specialArray(self, nums):
        nums.sort()

        n = len(nums)
        left = 0
        right = n

        while left <= right:
            x = (left + right) // 2

            low = 0
            high = n

            # Find the first index where nums[index] >= x
            while low < high:
                mid = (low + high) // 2

                if nums[mid] >= x:
                    high = mid
                else:
                    low = mid + 1

            count = n - low

            if count == x:
                return x
            elif count > x:
                left = x + 1
            else:
                right = x - 1

        return -1
```

---

## 5. Dry Run

**Input:**
```python
nums = [0, 4, 3, 0, 4]
```

Sort the array:

```python
nums = [0, 0, 3, 4, 4]
```

The array length is:

```text
n = 5
```

We binary search for `x` in the range `0` to `5`.

### Iteration 1

```text
left = 0
right = 5
x = (0 + 5) // 2 = 2
```

Find the first element greater than or equal to `2`.

In `[0, 0, 3, 4, 4]`, the first such element is `3` at index `2`.

```text
count = n - index
count = 5 - 2 = 3
```

Compare:

```text
count = 3
x = 2
```

Since `count > x`, we need to try a larger value:

```text
left = x + 1 = 3
```

### Iteration 2

```text
left = 3
right = 5
x = (3 + 5) // 2 = 4
```

Find the first element greater than or equal to `4`.

The first such element is at index `3`.

```text
count = 5 - 3 = 2
```

Compare:

```text
count = 2
x = 4
```

Since `count < x`, we need to try a smaller value:

```text
right = x - 1 = 3
```

### Iteration 3

```text
left = 3
right = 3
x = (3 + 3) // 2 = 3
```

Find the first element greater than or equal to `3`.

The first such element is at index `2`.

```text
count = 5 - 2 = 3
```

Now:

```text
count == x
3 == 3
```

We found the special value.

**Output:**
```python
3
```

### Dry Run Summary

| Iteration | `left` | `right` | Candidate `x` | First valid index | Count `>= x` | Decision |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0 | 5 | 2 | 2 | 3 | Count is larger; search higher |
| 2 | 3 | 5 | 4 | 3 | 2 | Count is smaller; search lower |
| 3 | 3 | 3 | 3 | 2 | 3 | Found answer |

---

## 6. Why This Works

After sorting, all elements greater than or equal to a candidate `x` appear together at the end of the array.

The inner binary search finds the first index where `nums[index] >= x`. Therefore, `n - index` is exactly the number of elements that satisfy the condition.

The outer binary search uses the fact that this count never increases when `x` increases:

- If the count is greater than `x`, we need a larger candidate.
- If the count is less than `x`, we need a smaller candidate.
- If the count equals `x`, the definition of a special array is satisfied.

Thus, the algorithm returns the unique valid `x`, or `-1` if none exists.

---

## 7. Complexity Analysis

Let `n` be the length of `nums`.

| Operation | Time Complexity |
|---|---|
| Sorting `nums` | `O(n log n)` |
| Outer binary search | `O(log n)` iterations |
| Inner binary search per iteration | `O(log n)` |
| Total binary-search work | `O(log² n)` |

**Total Time Complexity:**

```text
O(n log n + log² n)
```

**Auxiliary Space Complexity:**

- `O(1)` auxiliary space for the binary search variables, excluding the sorting implementation.
- Python's in-place sort may use additional temporary memory internally.

---

## 8. Pattern and Related Problems

**Pattern: Sorting + Binary Search on Answer**

Recognize this pattern when:
- You need to find a value that satisfies a numerical condition.
- The count of elements meeting a threshold changes monotonically as the threshold changes.
- You can use binary search to find the threshold where the required condition becomes true.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Binary Search | 704 | Basic Binary Search |
| Find Smallest Letter Greater Than Target | 744 | Upper Bound |
| H-Index II | 275 | Binary Search on Sorted Array |
| Special Array With X Elements Greater Than or Equal X | 1608 | Binary Search on Answer |
| Koko Eating Bananas | 875 | Binary Search on Answer |
