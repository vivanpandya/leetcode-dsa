# 278. First Bad Version

[LeetCode Problem](https://leetcode.com/problems/first-bad-version/)  
**Difficulty:** Easy  
**Topics:** Binary Search

---

## Question

You are a product manager leading a team developing a new product. The latest version fails the quality check. Since each version is developed based on the previous version, all versions after a bad version are also bad.

There are `n` versions numbered from `1` to `n`. You are given an API:

```python
isBadVersion(version)
```

It returns `True` if the given version is bad and `False` otherwise.

Find the **first bad version** while minimizing the number of API calls.

### Example 1

```text
Input: n = 5, bad = 4
Output: 4

Explanation:
isBadVersion(3) -> False
isBadVersion(5) -> True
isBadVersion(4) -> True

Version 4 is the first bad version.
```

### Example 2

```text
Input: n = 1, bad = 1
Output: 1
```

### Constraints

- `1 <= bad <= n <= 2^31 - 1`

---

## 1. Approach – Binary Search

Versions have a **monotonic pattern**:

- All versions before the first bad version are good (`False`).
- The first bad version and every version after it are bad (`True`).

So the sequence looks like:

```text
Good  Good  Good  Bad  Bad  Bad
 F     F     F     T    T    T
```

We need to find the **first `True`**. Binary Search allows us to eliminate half of the remaining versions after each API call.

We maintain:

- `left = 1`: the first possible bad version.
- `right = n`: the last possible bad version.

For each iteration:

1. Calculate the middle version.
2. Call `isBadVersion(mid)`.
3. If it returns `True`, `mid` could be the first bad version, so keep it and search left: `right = mid`.
4. If it returns `False`, the first bad version must be after `mid`: `left = mid + 1`.

When `left == right`, that version is the first bad version.

## 2. Algorithm

1. Initialize `left = 1`.
2. Initialize `right = n`.
3. Continue while `left < right`.
4. Calculate `mid = (left + right) // 2`.
5. If `isBadVersion(mid)` is `True`, update `right = mid`.
6. Otherwise, update `left = mid + 1`.
7. Return `left`.

## 3. Code

LeetCode provides the `isBadVersion(version)` API. Do not implement or redefine it.

```python
# The isBadVersion API is provided by LeetCode.

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

## 4. Example / Dry Run

**Input:**

```python
n = 5
bad = 4
```

| Iteration | left | right | mid | isBadVersion(mid) | Decision |
|---|---:|---:|---:|---|---|
| 1 | 1 | 5 | 3 | False | `left = mid + 1 = 4` |
| 2 | 4 | 5 | 4 | True | `right = mid = 4` |

Now `left == right == 4`, so the loop stops.

**Output:**

```python
4
```

Version 4 is the first bad version.

### Example 2 – Only One Version

```python
n = 1
bad = 1
```

Initially, `left = 1` and `right = 1`. The loop condition `left < right` is false, so the loop does not run.

**Output:**

```python
1
```

## 5. Why This Works

The versions follow a monotonic order: once a version is bad, every later version is also bad.

- If `isBadVersion(mid)` is `True`, the first bad version is at `mid` or before it. We set `right = mid`, keeping `mid` as a possible answer.
- If `isBadVersion(mid)` is `False`, the first bad version must be after `mid`. We set `left = mid + 1`.

This never removes the actual first bad version from the search range. When the two boundaries meet, only the first bad version can remain.

## 6. Complexity Analysis

- **Time Complexity: O(log n)** — Each API call eliminates approximately half of the remaining versions.
- **Space Complexity: O(1)** — Only a fixed number of variables are used.
- **API Calls: O(log n)** — Binary Search minimizes the number of API calls.

## 7. Pattern

**Pattern:** Binary Search on a Monotonic Predicate – Find the First `True`

Compare these Binary Search problems:

| Problem | Main goal |
|---|---|
| 704. Binary Search | Find an exact target |
| 35. Search Insert Position | Find the first position where value is `>= target` |
| 278. First Bad Version | Find the first version for which the API returns `True` |

### Important Pointer Updates

```python
if isBadVersion(mid):
    right = mid       # Keep mid; first bad version may be earlier
else:
    left = mid + 1    # mid is good, so answer must be after it
```

**Remember:** Use `while left < right` and `right = mid` when searching for the first position satisfying a condition. Do not use `right = mid - 1`, because `mid` itself might be the first bad version.
