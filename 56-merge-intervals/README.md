# 56. Merge Intervals

[LeetCode Problem](https://leetcode.com/problems/merge-intervals/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Sorting
- Greedy
- Intervals

---

## 1. Problem Statement

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of non-overlapping intervals that cover all the intervals in the input.

Two intervals overlap if they share at least one point. Therefore, `[1,4]` and `[4,5]` must also be merged.

## Examples

### Example 1

**Input:**
```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output:**
```python
[[1,6],[8,10],[15,18]]
```

**Explanation:** `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

### Example 2

**Input:**
```python
intervals = [[1,4],[4,5]]
```

**Output:**
```python
[[1,5]]
```

**Explanation:** The intervals share endpoint `4`, so they overlap.

### Example 3

**Input:**
```python
intervals = [[4,7],[1,4]]
```

**Output:**
```python
[[1,7]]
```

**Explanation:** After sorting, `[1,4]` and `[4,7]` share endpoint `4`, so they are merged.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

---

## 2. Approach: Sorting + Greedy

The key idea is to **sort intervals by their starting point**. Then process them from left to right, comparing each interval with the last interval in the result.

For every interval `[start, end]`, there are two possibilities.

### Case 1: No overlap

If the result is empty, or the current interval starts strictly after the end of the last merged interval, there is no overlap.

```python
if not merged or merged[-1][1] < start:
    merged.append([start, end])
```

Append the current interval as a new interval.

### Case 2: Overlap

Otherwise, the current interval overlaps with the last merged interval.

```python
else:
    merged[-1][1] = max(merged[-1][1], end)
```

Keep the earlier start and extend the ending point to the larger ending point.

**Important:** Use `< start`, not `<= start`. If the current interval starts exactly where the previous one ends, they share a point and must be merged.

---

## 3. Algorithm

1. Sort `intervals` in ascending order.
2. Create an empty list called `merged`.
3. Traverse every interval:
   - Extract `start` and `end`.
   - If `merged` is empty or `start` is greater than the end of the last merged interval, append `[start, end]`.
   - Otherwise, update the end of the last merged interval using `max()`.
4. Return `merged`.

---

## 4. Python Code

```python
class Solution:
    def merge(self, intervals):
        intervals.sort()

        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
```

---

## 5. Dry Run

**Input:**

```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

### Step 1: Sort the intervals

```python
[[1,3],[2,6],[8,10],[15,18]]
```

They are already sorted.

Initially:

```python
merged = []
```

### Step 2: Process `[1,3]`

The result is empty, so append the interval.

```python
merged = [[1,3]]
```

### Step 3: Process `[2,6]`

Compare the current start with the last merged end:

```text
start = 2
last merged end = 3

3 < 2  -> False
```

The intervals overlap. Update the ending point:

```python
merged[-1][1] = max(3, 6)
```

Now:

```python
merged = [[1,6]]
```

### Step 4: Process `[8,10]`

```text
start = 8
last merged end = 6

6 < 8  -> True
```

There is no overlap, so append it.

```python
merged = [[1,6],[8,10]]
```

### Step 5: Process `[15,18]`

```text
start = 15
last merged end = 10

10 < 15  -> True
```

There is no overlap, so append it.

```python
merged = [[1,6],[8,10],[15,18]]
```

### Dry Run Table

| Current interval | Last merged interval | Condition | Action |
|---|---|---|---|
| `[1,3]` | None | Result is empty | Append |
| `[2,6]` | `[1,3]` | `3 < 2` is false | Merge into `[1,6]` |
| `[8,10]` | `[1,6]` | `6 < 8` is true | Append |
| `[15,18]` | `[8,10]` | `10 < 15` is true | Append |

**Final Output:**

```python
[[1,6],[8,10],[15,18]]
```

### Special Case: Touching Endpoints

Input:

```python
intervals = [[1,4],[4,5]]
```

For `[4,5]`:

```text
last merged end = 4
current start = 4

4 < 4  -> False
```

Therefore, the intervals overlap and are merged:

```python
[[1,5]]
```

---

## 6. Why This Works

Sorting places intervals in non-decreasing order of their starting points.

When processing the current interval, the last interval in `merged` has the greatest starting point among the intervals already added.

- If `merged[-1][1] < start`, the current interval begins strictly after the previous merged interval ends. Since the input is sorted, it cannot overlap any earlier merged interval either. It is safe to append it.
- Otherwise, the current interval shares at least one point with the last merged interval. Updating the last ending point with the maximum of both ending points combines their coverage.

Repeating this process merges every group of overlapping intervals and leaves the result sorted and non-overlapping.

---

## 7. Complexity Analysis

Let `n` be the number of intervals.

| Operation | Time Complexity |
|---|---|
| Sorting intervals | `O(n log n)` |
| Traversing intervals | `O(n)` |
| Merging/appending each interval | `O(1)` per interval |

**Total Time Complexity:**

```text
O(n log n)
```

Sorting dominates the overall time complexity.

**Space Complexity:**

- `O(n)` for the `merged` result in the worst case, when no intervals overlap.
- Python's in-place sorting may also use temporary memory.

The result itself requires `O(n)` space in the worst case.

---

## 8. Pattern and Related Problems

**Main Pattern: Sorting + Greedy + Intervals**

Recognize this pattern when:
- You are given a collection of intervals.
- You need to combine overlapping ranges.
- You need non-overlapping ranges covering the same points.
- Sorting by start time makes the intervals easier to process from left to right.

### Important Code to Remember

**Sort intervals:**

```python
intervals.sort()
```

**Check whether there is no overlap:**

```python
if not merged or merged[-1][1] < start:
    merged.append([start, end])
```

**Merge overlapping intervals:**

```python
else:
    merged[-1][1] = max(merged[-1][1], end)
```

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Insert Interval | 57 | Intervals + Greedy |
| Non-overlapping Intervals | 435 | Greedy + Sorting |
| Meeting Rooms | 252 | Intervals |
| Meeting Rooms II | 253 | Intervals + Heap |
| Minimum Number of Arrows to Burst Balloons | 452 | Greedy + Intervals |

---

**Key Takeaway:** Sort intervals by their starting points, then compare each interval with the last merged interval. Use `last_end < current_start` to detect no overlap. Equality means the intervals touch, so they must be merged.
