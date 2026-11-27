# 57. Insert Interval

[LeetCode Problem](https://leetcode.com/problems/insert-interval/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Sorting
- Greedy
- Intervals

---

## 1. Problem Statement

You are given an array of non-overlapping intervals, `intervals`, sorted in ascending order by their starting points. You are also given a new interval, `newInterval = [start, end]`.

Insert `newInterval` into `intervals` so that the result remains sorted and contains no overlapping intervals. If the new interval overlaps with existing intervals, merge them.

Two intervals overlap if they share at least one point. For example, `[3,5]` and `[5,8]` overlap because they share the point `5`.

You do not need to modify `intervals` in place. You can create and return a new list.

## Examples

### Example 1

**Input:**
```python
intervals = [[1,3],[6,9]]
newInterval = [2,5]
```

**Output:**
```python
[[1,5],[6,9]]
```

### Example 2

**Input:**
```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

**Output:**
```python
[[1,2],[3,10],[12,16]]
```

**Explanation:** `[4,8]` overlaps with `[3,5]`, `[6,7]`, and `[8,10]`. These intervals merge into `[3,10]`.

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by starting point in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

---

## 2. Approach: Three Phases (Greedy)

The intervals are already sorted and non-overlapping, so we do **not** need to sort them again. We can process the list from left to right in three phases.

### Phase 1: Add intervals before the new interval

If an existing interval ends strictly before `newInterval` starts, it cannot overlap with the new interval.

Condition:

```python
intervals[i][1] < newInterval[0]
```

Append that interval to `result` and move to the next interval.

### Phase 2: Merge overlapping intervals

An existing interval overlaps the current `newInterval` if its start is less than or equal to the new interval's end.

Condition:

```python
intervals[i][0] <= newInterval[1]
```

For every overlapping interval, expand `newInterval`:

```python
newInterval[0] = min(newInterval[0], intervals[i][0])
newInterval[1] = max(newInterval[1], intervals[i][1])
```

This is important because merging one interval may expand the new interval enough to overlap with the next interval too.

### Phase 3: Add the merged interval and all remaining intervals

When no more overlapping intervals remain:
1. Append the updated `newInterval`.
2. Append every interval that has not been processed.

These remaining intervals are already sorted and cannot overlap with the merged interval.

---

## 3. Algorithm

1. Create an empty list `result`.
2. Set `i = 0` and `n = len(intervals)`.
3. While there are intervals whose end is less than `newInterval[0]`:
   - Append the current interval to `result`.
   - Increment `i`.
4. While there are intervals whose start is less than or equal to `newInterval[1]`:
   - Update the new interval's start with the minimum of both starts.
   - Update the new interval's end with the maximum of both ends.
   - Increment `i`.
5. Append the merged `newInterval` to `result`.
6. Append all remaining intervals.
7. Return `result`.

---

## 4. Python Code

```python
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Phase 1: Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Phase 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
```

**Important indexing reminder:**
- `intervals[i][0]` is the existing interval's start.
- `intervals[i][1]` is the existing interval's end.
- `newInterval[0]` is the new interval's start.
- `newInterval[1]` is the new interval's end.

When merging, compare start with start and end with end.

---

## 5. Dry Run

Use Example 2:

```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

Initially:

```python
result = []
i = 0
newInterval = [4,8]
```

### Phase 1: Add intervals before the new interval

Current interval: `[1,2]`

Check:

```text
intervals[i][1] < newInterval[0]
2 < 4  -> True
```

Append `[1,2]`:

```python
result = [[1,2]]
i = 1
```

Next interval: `[3,5]`

```text
5 < 4  -> False
```

Stop Phase 1. This interval may overlap with the new interval.

### Phase 2: Merge overlapping intervals

Current interval: `[3,5]`

Check:

```text
intervals[i][0] <= newInterval[1]
3 <= 8  -> True
```

Merge:

```text
new start = min(4,3) = 3
new end   = max(8,5) = 8
```

Now:

```python
newInterval = [3,8]
```

Next interval: `[6,7]`

```text
6 <= 8  -> True
```

Merge:

```text
new start = min(3,6) = 3
new end   = max(8,7) = 8
```

The new interval remains:

```python
newInterval = [3,8]
```

Next interval: `[8,10]`

```text
8 <= 8  -> True
```

They overlap because they share endpoint `8`.

Merge:

```text
new start = min(3,8) = 3
new end   = max(8,10) = 10
```

Now:

```python
newInterval = [3,10]
```

Next interval: `[12,16]`

```text
12 <= 10  -> False
```

Stop Phase 2.

### Phase 3: Add the merged interval and remaining intervals

Append the merged interval:

```python
result = [[1,2],[3,10]]
```

Append all remaining intervals:

```python
result = [[1,2],[3,10],[12,16]]
```

**Final Output:**

```python
[[1,2],[3,10],[12,16]]
```

### Dry Run Table

| Current interval | Check | Action |
|---|---|---|
| `[1,2]` | `2 < 4` | Add before |
| `[3,5]` | `3 <= 8` | Merge; new interval becomes `[3,8]` |
| `[6,7]` | `6 <= 8` | Merge; remains `[3,8]` |
| `[8,10]` | `8 <= 8` | Merge; becomes `[3,10]` |
| `[12,16]` | `12 <= 10` is false | Stop merging; add as remaining |

### Special Case: Intervals Touch at an Endpoint

Input:

```python
intervals = [[1,3],[6,9]]
newInterval = [3,5]
```

The first interval ends at `3`, and the new interval starts at `3`. They share a point, so they overlap.

The merge produces:

```python
[[1,5],[6,9]]
```

This is why Phase 1 uses `<` and Phase 2 uses `<=`.

---

## 6. Why This Works

The existing intervals are already sorted and non-overlapping.

- **Before phase:** Every interval ending before `newInterval` starts is safely added to the result. None can overlap with the new interval.
- **Merge phase:** Every interval starting at or before the current new interval's end overlaps it. Updating the start with `min()` and end with `max()` produces an interval covering both. The updated end is used to check the next interval, so chains of overlapping intervals are merged too.
- **After phase:** All unprocessed intervals start after the merged interval ends. They can be appended directly and remain sorted and non-overlapping.

Each existing interval is visited once, so the algorithm correctly inserts and merges the new interval in linear time.

---

## 7. Complexity Analysis

Let `n` be the number of existing intervals.

**Time Complexity: `O(n)`**

- Phase 1 visits intervals before the new interval.
- Phase 2 visits intervals that overlap with it.
- Phase 3 visits the remaining intervals.
- Every existing interval is processed at most once.

Therefore, the total time complexity is `O(n)`.

**Space Complexity: `O(n)`**

The `result` list can contain up to `n + 1` intervals. Excluding the returned result, the algorithm uses `O(1)` auxiliary space.

---

## 8. Pattern and Related Problems

**Main Pattern: Greedy + Intervals + Two Pointers**

Recognize this pattern when:
- The intervals are already sorted.
- The intervals do not overlap initially.
- You need to insert a new interval.
- You need to merge every interval that overlaps with the inserted interval.

### Important Conditions to Remember

**1. Existing interval is completely before the new interval:**

```python
intervals[i][1] < newInterval[0]
```

**2. Existing interval overlaps the new interval:**

```python
intervals[i][0] <= newInterval[1]
```

**3. Update the new interval correctly:**

```python
newInterval[0] = min(newInterval[0], intervals[i][0])
newInterval[1] = max(newInterval[1], intervals[i][1])
```

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Merge Intervals | 56 | Sorting + Greedy |
| Insert Interval | 57 | Greedy + Intervals |
| Non-overlapping Intervals | 435 | Greedy + Sorting |
| Meeting Rooms | 252 | Intervals |
| Meeting Rooms II | 253 | Intervals + Heap |
| Minimum Number of Arrows to Burst Balloons | 452 | Greedy + Intervals |

---

**Key Takeaway:** Because the intervals are already sorted and non-overlapping, do not sort them again. Process them in three phases: add intervals before, merge overlapping intervals, and add intervals after.
