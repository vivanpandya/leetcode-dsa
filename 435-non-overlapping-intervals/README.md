# 435. Non-overlapping Intervals

[LeetCode Problem](https://leetcode.com/problems/non-overlapping-intervals/)

- **Difficulty:** Medium
- **Topics:** Array, Greedy, Sorting

---

## 1. Problem Statement

Given an array of intervals `intervals`, where `intervals[i] = [start_i, end_i]`, return the **minimum number of intervals you need to remove** to make the remaining intervals non-overlapping.

**Important:** Intervals that only touch at one point are considered non-overlapping. For example, `[1, 2]` and `[2, 3]` do not overlap.

## 2. Examples

### Example 1

```text
Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
```

Remove `[1,3]`. The remaining intervals `[1,2]`, `[2,3]`, and `[3,4]` do not overlap.

### Example 2

```text
Input:  intervals = [[1,2],[1,2],[1,2]]
Output: 2
```

Only one of the three identical intervals can remain, so two must be removed.

### Example 3

```text
Input:  intervals = [[1,2],[2,3]]
Output: 0
```

The intervals only touch at `2`, so they are already non-overlapping.

## 3. Approach: Greedy + Sorting

The key idea is to **keep as many non-overlapping intervals as possible**. The minimum number to remove is:

```text
number of intervals - maximum number of intervals we can keep
```

To keep the maximum number, sort intervals by their **ending time** in ascending order.

Why sort by ending time?

- An interval that ends earlier leaves more room for intervals that come after it.
- Choosing the interval with the earliest ending time is a greedy choice that helps us fit the maximum number of non-overlapping intervals.
- After selecting an interval, the next selected interval must start at or after the previous selected interval's end.

Because intervals that touch are allowed, the compatibility check is:

```python
start >= prev_end
```

If `start < prev_end`, the current interval overlaps with the last kept interval, so we remove it (do not count it as kept).

## 4. Algorithm

1. Sort `intervals` by their ending value (`interval[1]`).
2. Keep `prev_end` to store the ending time of the last selected interval.
3. Initialize `removed = 0`.
4. Traverse the sorted intervals:
   - If the current interval starts at or after `prev_end`, keep it and update `prev_end` to its ending time.
   - Otherwise, it overlaps with the last selected interval, so increment `removed`.
5. Return `removed`.

## 5. Python Code

```python
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        removed = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1

        return removed
```

**Note:** Sorting `intervals` in place is allowed. To preserve the original list, use `sorted(intervals, key=lambda x: x[1])` instead.

## 6. Dry Run

Consider:

```text
intervals = [[1,2], [2,3], [3,4], [1,3]]
```

### Step 1: Sort by ending time

The intervals are already in the required order:

```text
[[1,2], [2,3], [3,4], [1,3]]
```

### Step 2: Traverse the intervals

Initialize:

```text
removed = 0
prev_end = -infinity
```

| Current interval | Check | Decision | `prev_end` | `removed` |
|---|---|---|---:|---:|
| `[1,2]` | `1 >= -infinity` | Keep | 2 | 0 |
| `[2,3]` | `2 >= 2` | Keep | 3 | 0 |
| `[3,4]` | `3 >= 3` | Keep | 4 | 0 |
| `[1,3]` | `1 < 4` | Remove | 4 | 1 |

Final result:

```text
1
```

We remove only `[1,3]`.

## 7. Why This Works

After sorting by ending time, the greedy algorithm always selects the compatible interval that finishes earliest.

When two available intervals overlap, choosing the one that ends earlier cannot reduce the space available for future intervals compared with choosing the one that ends later. It leaves at least as much room for every later choice.

Repeating this choice produces the maximum possible number of non-overlapping intervals. Therefore, removing every interval not selected gives the minimum number of removals.

## 8. Complexity Analysis

Let `n` be the number of intervals.

- **Time Complexity:** `O(n log n)`
  - Sorting takes `O(n log n)`.
  - Traversing the intervals takes `O(n)`.
  - Sorting dominates the total time.
- **Auxiliary Space Complexity:** `O(1)` for the greedy traversal, excluding sorting's internal space. Python's in-place sort may use additional temporary memory.

## 9. Pattern Recognition

**Pattern:** Greedy Interval Scheduling

Use this pattern when a problem asks you to:
- Select the maximum number of non-overlapping intervals.
- Remove the minimum number of intervals to eliminate overlaps.
- Schedule the maximum number of compatible activities.

**Important distinction:**

- **Merge Intervals (#56):** Sort by start time and combine overlapping intervals.
- **Insert Interval (#57):** Insert one interval into an already sorted, non-overlapping list and merge if needed.
- **Non-overlapping Intervals (#435):** Sort by end time and greedily keep the maximum number of compatible intervals.

**Key rule:** For this problem, sort by **end time**, and allow the next interval when `start >= prev_end`.
