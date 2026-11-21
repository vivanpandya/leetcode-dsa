# 436. Find Right Interval

[LeetCode Problem](https://leetcode.com/problems/find-right-interval/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Binary Search
- Sorting

---

## 1. Problem Statement

You are given an array `intervals`, where `intervals[i] = [start_i, end_i]`. Every interval has a unique starting point.

The **right interval** for interval `i` is the interval `j` whose starting point is:
1. Greater than or equal to `end_i`.
2. The smallest possible starting point satisfying the first condition.

The interval itself may also be its own right interval.

Return an array containing the original index of the right interval for every interval. If no right interval exists, return `-1`.

### Example 1

**Input:**
```python
intervals = [[1, 2]]
```

**Output:**
```python
[-1]
```

There is no interval whose starting point is greater than or equal to `2`.

### Example 2

**Input:**
```python
intervals = [[3, 4], [2, 3], [1, 2]]
```

**Output:**
```python
[-1, 0, 1]
```

- For `[3, 4]`, no starting point is at least `4`.
- For `[2, 3]`, the smallest starting point at least `3` belongs to interval `0`, `[3, 4]`.
- For `[1, 2]`, the smallest starting point at least `2` belongs to interval `1`, `[2, 3]`.

### Example 3

**Input:**
```python
intervals = [[1, 4], [2, 3], [3, 4]]
```

**Output:**
```python
[-1, 2, -1]
```

### Constraints
- `1 <= intervals.length <= 2 * 10^4`
- `intervals[i].length == 2`
- `-10^6 <= start_i <= end_i <= 10^6`
- The start point of each interval is unique.

---

## 2. Approach: Sorting + Binary Search (Lower Bound)

For every interval, we need the smallest starting point that is greater than or equal to its ending point.

Checking every interval against every other interval would take `O(n^2)` time. Instead, sort the starting points and use binary search.

### Step 1: Store each start point with its original index

We must return the original interval index, not its position in the sorted list.

```python
starts = sorted(
    (interval[0], i)
    for i, interval in enumerate(intervals)
)
```

For example:

```python
intervals = [[3, 4], [2, 3], [1, 2]]

starts = [(1, 2), (2, 1), (3, 0)]
```

Each pair contains `(starting_point, original_index)`.

### Step 2: Search for each interval's end point

For an interval `[start, end]`, find the first entry in `starts` whose starting point is greater than or equal to `end`.

This is called **lower bound** binary search.

Initialize:

```python
left = 0
right = len(starts)
```

The right boundary is exclusive, so it can represent the position after the last element.

During binary search:

- If `starts[mid][0] >= end`, this starting point is valid. Keep searching to the left:

  ```python
  right = mid
  ```

- Otherwise, the starting point is too small. Search to the right:

  ```python
  left = mid + 1
  ```

### Step 3: Store the original index

When the loop ends:

- If `left < len(starts)`, `starts[left]` is the first valid starting point. Append its original index:

  ```python
  result.append(starts[left][1])
  ```

- Otherwise, no right interval exists. Append `-1`.

Repeat this for every original interval.

---

## 3. Algorithm

1. Create a list of `(start, original_index)` pairs.
2. Sort this list by starting point.
3. Create an empty `result` list.
4. For every interval `[start, end]`:
   1. Set `left = 0` and `right = len(starts)`.
   2. While `left < right`:
      - Calculate `mid = (left + right) // 2`.
      - If `starts[mid][0] >= end`, set `right = mid`.
      - Otherwise, set `left = mid + 1`.
   3. If `left < len(starts)`, append `starts[left][1]`.
   4. Otherwise, append `-1`.
5. Return `result`.

---

## 4. Python Code

```python
class Solution:
    def findRightInterval(self, intervals):
        starts = sorted(
            (interval[0], i)
            for i, interval in enumerate(intervals)
        )

        result = []

        for start, end in intervals:
            left = 0
            right = len(starts)

            while left < right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1

            if left < len(starts):
                result.append(starts[left][1])
            else:
                result.append(-1)

        return result
```

---

## 5. Dry Run

**Input:**

```python
intervals = [[3, 4], [2, 3], [1, 2]]
```

### Step 1: Sort the starting points

```python
starts = [(1, 2), (2, 1), (3, 0)]
```

The first value is the starting point; the second value is the original index.

### Step 2: Process each interval

**Interval 1: `[3, 4]`**

Find the first starting point greater than or equal to `4`.

| `left` | `right` | `mid` | `starts[mid][0]` | Decision |
|---:|---:|---:|---:|---|
| 0 | 3 | 1 | 2 | Too small; `left = 2` |
| 2 | 3 | 2 | 3 | Too small; `left = 3` |

Now `left = 3`, which equals `len(starts)`. No valid interval exists.

```python
result = [-1]
```

**Interval 2: `[2, 3]`**

Find the first starting point greater than or equal to `3`.

| `left` | `right` | `mid` | `starts[mid][0]` | Decision |
|---:|---:|---:|---:|---|
| 0 | 3 | 1 | 2 | Too small; `left = 2` |
| 2 | 3 | 2 | 3 | Valid; `right = 2` |

Now:

```python
starts[2] = (3, 0)
```

The original index is `0`.

```python
result = [-1, 0]
```

**Interval 3: `[1, 2]`**

Find the first starting point greater than or equal to `2`.

| `left` | `right` | `mid` | `starts[mid][0]` | Decision |
|---:|---:|---:|---:|---|
| 0 | 3 | 1 | 2 | Valid; `right = 1` |
| 0 | 1 | 0 | 1 | Too small; `left = 1` |

Now:

```python
starts[1] = (2, 1)
```

The original index is `1`.

```python
result = [-1, 0, 1]
```

### Final Output

```python
[-1, 0, 1]
```

---

## 6. Why This Works

Sorting puts all starting points in ascending order.

For a given interval ending at `end`, every starting point before the lower-bound position is smaller than `end`. The lower-bound position is therefore the first starting point greater than or equal to `end`.

Because all starting points are unique, this position identifies exactly one interval. We store its original index so the answer refers to the input array rather than the sorted list.

If the lower-bound position equals the length of the sorted list, no valid right interval exists, so we return `-1`.

---

## 7. Complexity Analysis

Let `n` be the number of intervals.

| Operation | Time Complexity |
|---|---|
| Build and sort `(start, index)` pairs | `O(n log n)` |
| Binary search for one interval | `O(log n)` |
| Binary searches for all intervals | `O(n log n)` |
| Build the result | `O(n)` |

**Total Time Complexity:**

```text
O(n log n)
```

**Space Complexity:**

- `O(n)` for the sorted `(start, index)` list.
- `O(n)` for the returned result list.
- Python's sorting implementation may also use temporary memory.

Overall space is `O(n)`.

---

## 8. Pattern and Related Problems

**Pattern: Sorting + Lower Bound Binary Search**

Recognize this pattern when:
- You need the smallest element greater than or equal to a target.
- You need to preserve original indices after sorting.
- You need to answer multiple threshold-search queries efficiently.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Search Insert Position | 35 | Lower Bound Binary Search |
| Find First and Last Position of Element in Sorted Array | 34 | Boundary Binary Search |
| Successful Pairs of Spells and Potions | 2300 | Sorting + Lower Bound |
| Find Right Interval | 436 | Sorting + Lower Bound |
| First Bad Version | 278 | First True Binary Search |

### Important Lines to Remember

**Keep the original index while sorting:**

```python
starts = sorted(
    (interval[0], i)
    for i, interval in enumerate(intervals)
)
```

**Find the first starting point greater than or equal to `end`:**

```python
if starts[mid][0] >= end:
    right = mid
else:
    left = mid + 1
```

**Return the original index or `-1`:**

```python
if left < len(starts):
    result.append(starts[left][1])
else:
    result.append(-1)
```
