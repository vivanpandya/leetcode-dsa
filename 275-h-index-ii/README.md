# 275. H-Index II

[LeetCode Problem](https://leetcode.com/problems/h-index-ii/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics

- Array
- Binary Search

---

## 1. Problem Statement

You are given an array `citations` where `citations[i]` is the number of citations received by the researcher's `i`th paper.

The array is sorted in **ascending order**.

Return the researcher's **h-index**.

The h-index is the maximum value `h` such that the researcher has at least `h` papers, and each of those papers has at least `h` citations.

You must solve the problem in `O(log n)` time.

### Example 1

**Input:**
```python
citations = [0, 1, 3, 5, 6]
```

**Output:**
```python
3
```

**Explanation:**

There are 3 papers with at least 3 citations each: the papers with 3, 5, and 6 citations.

### Example 2

**Input:**
```python
citations = [1, 2, 100]
```

**Output:**
```python
2
```

There are 2 papers with at least 2 citations each.

### Constraints

- `n == citations.length`
- `1 <= n <= 10^5`
- `0 <= citations[i] <= 1000`
- `citations` is sorted in ascending order.

---

## 2. Approach: Binary Search

The array is already sorted in ascending order, so we can use binary search instead of checking every possible h-index.

The key observation is:

At index `mid`, the number of papers from `mid` to the end is:

```python
n - mid
```

For an h-index of `n - mid` to be possible, the citation count at `mid` must be at least that number:

```python
citations[mid] >= n - mid
```

Why?

- `citations[mid]` is the citation count of the first paper in the suffix.
- Since the array is sorted, every paper after `mid` has at least as many citations.
- There are exactly `n - mid` papers from `mid` to the end.

Therefore, if `citations[mid] >= n - mid`, we have at least `n - mid` papers with at least `n - mid` citations each.

We need the **first index** where this condition becomes true.

### Binary Search Decisions

- If `citations[mid] >= n - mid`, the condition is satisfied. This index may give the answer, but an earlier index could produce a larger h-index. Search left:

  ```python
  right = mid - 1
  ```

- Otherwise, there are not enough citations at this position to satisfy the condition. Search right:

  ```python
  left = mid + 1
  ```

After binary search, `left` is the first valid index.

The h-index is:

```python
n - left
```

If no index satisfies the condition, `left` becomes `n`, and the answer is `0`.

---

## 3. Algorithm

1. Store the number of papers: `n = len(citations)`.
2. Initialize `left = 0` and `right = n - 1`.
3. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. Calculate the number of papers from `mid` onward: `n - mid`.
   3. If `citations[mid] >= n - mid`, the condition is satisfied. Save the possibility by moving left: `right = mid - 1`.
   4. Otherwise, move right: `left = mid + 1`.
4. Return `n - left`.

---

## 4. Python Code

```python
class Solution:
    def hIndex(self, citations):
        n = len(citations)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left
```

---

## 5. Dry Run

**Input:**

```python
citations = [0, 1, 3, 5, 6]
```

The number of papers is:

```python
n = 5
```

Initially:

```python
left = 0
right = 4
```

### Iteration 1

```python
mid = (0 + 4) // 2
mid = 2
```

Check:

```python
citations[2] = 3
n - mid = 5 - 2 = 3
```

Condition:

```python
3 >= 3  # True
```

We have 3 papers with at least 3 citations each. This is a valid answer, but we continue searching left in case a larger h-index is possible.

```python
right = mid - 1
right = 1
```

### Iteration 2

Now:

```python
left = 0
right = 1

mid = (0 + 1) // 2
mid = 0
```

Check:

```python
citations[0] = 0
n - mid = 5 - 0 = 5
```

Condition:

```python
0 >= 5  # False
```

There are not 5 papers with at least 5 citations each, so search right.

```python
left = mid + 1
left = 1
```

### Iteration 3

Now:

```python
left = 1
right = 1

mid = (1 + 1) // 2
mid = 1
```

Check:

```python
citations[1] = 1
n - mid = 5 - 1 = 4
```

Condition:

```python
1 >= 4  # False
```

Search right:

```python
left = mid + 1
left = 2
```

Now:

```python
left = 2
right = 1
```

The loop ends because `left > right`.

### Final Answer

```python
h_index = n - left
         = 5 - 2
         = 3
```

**Output:**

```python
3
```

---

## 6. Why This Works

Because `citations` is sorted in ascending order, the condition:

```python
citations[mid] >= n - mid
```

changes from false to true as we move toward the right through the array (once it becomes true, it stays true).

We therefore have a monotonic condition, which is suitable for binary search.

Binary search finds the first index where the condition is true. From that index to the end, there are `n - left` papers, and each has at least `citations[left] >= n - left` citations.

That gives an h-index of `n - left`. Since we found the first valid index, no larger h-index is possible.

If the condition is never true, the algorithm returns `0`, which is correct.

---

## 7. Complexity Analysis

Let `n` be the number of papers.

| Operation | Time Complexity |
|---|---|
| Initialize variables | `O(1)` |
| Binary search | `O(log n)` |
| Calculate the answer | `O(1)` |

**Total Time Complexity:**

```text
O(log n)
```

**Space Complexity:**

```text
O(1)
```

Only a constant number of variables are used. The input array is not modified.

---

## 8. Pattern and Related Problems

**Pattern: Binary Search on a Monotonic Condition (First True)**

Recognize this pattern when:

- The array is sorted.
- A condition changes monotonically from false to true.
- You need to find the first position where the condition becomes true.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| First Bad Version | 278 | First True Binary Search |
| Find First and Last Position of Element in Sorted Array | 34 | Boundary Binary Search |
| Search Insert Position | 35 | Lower Bound Binary Search |
| Find Right Interval | 436 | Sorting + Lower Bound |
| H-Index II | 275 | Binary Search on Monotonic Condition |

### Important Lines to Remember

**Number of papers from index `mid` to the end:**

```python
n - mid
```

**Check whether this position can produce a valid h-index:**

```python
if citations[mid] >= n - mid:
    right = mid - 1
else:
    left = mid + 1
```

**Calculate the final h-index:**

```python
return n - left
```
