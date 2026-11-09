# 3229. Minimum Operations to Make Array Equal to Target

[LeetCode Problem](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/)  
**Difficulty:** Hard  
**Topics:** Array, Greedy, Difference Array

---

## 1. Question

You are given two positive integer arrays, `nums` and `target`, of the same length.

In one operation, you can select any contiguous subarray of `nums` and either:

- Increment every element in that subarray by `1`, or
- Decrement every element in that subarray by `1`.

Return the **minimum number of operations** required to make `nums` equal to `target`.

## 2. Examples

### Example 1

```text
Input:  nums = [3,5,1,2], target = [4,6,2,4]
Output: 2
```

**Explanation:**

1. Increment the entire array by `1`:
   `[3,5,1,2] -> [4,6,2,3]`
2. Increment the last element by `1`:
   `[4,6,2,3] -> [4,6,2,4]`

Total operations: `2`.

### Example 2

```text
Input:  nums = [1,3,2], target = [2,1,4]
Output: 5
```

**Explanation:**

The required changes are `[+1, -2, +2]`.

- Increment index `0` once.
- Decrement index `1` twice.
- Increment index `2` twice.

Total operations: `1 + 2 + 2 = 5`.

## 3. Approach — Difference Array + Greedy

Instead of modifying `nums`, calculate how much each position needs to change.

Define:

```python
diff[i] = target[i] - nums[i]
```

For Example 1:

```text
nums   = [3, 5, 1, 2]
target = [4, 6, 2, 4]
diff   = [1, 1, 1, 2]
```

This means:

- Index `0` needs `+1`.
- Index `1` needs `+1`.
- Index `2` needs `+1`.
- Index `3` needs `+2`.

### Key observation

One operation can apply the same `+1` or `-1` change to a whole contiguous subarray.

Therefore, if neighboring positions need the same positive change, we can handle them together. When the required positive change increases, we need to start additional increment operations. The same reasoning applies independently to negative changes.

Separate each difference into its positive and negative parts:

```python
current_positive = max(0, diff)
current_negative = max(0, -diff)
```

Track the previous positive and negative requirements:

- If the current positive requirement is larger than the previous one, the increase requires new increment operations.
- If the current negative requirement is larger than the previous one, the increase requires new decrement operations.
- If the requirement stays the same or decreases, no new operations need to start at this position.

The number of operations added at each index is therefore:

```python
max(0, current_positive - positive)
+
max(0, current_negative - negative)
```

Here, `positive` and `negative` are the previous position's positive and negative requirements.

## 4. Algorithm

1. Initialize `operations = 0`.
2. Initialize the previous positive and negative requirements:
   - `positive = 0`
   - `negative = 0`
3. Traverse every index `i`:
   1. Calculate `diff = target[i] - nums[i]`.
   2. Calculate `current_positive = max(0, diff)`.
   3. Calculate `current_negative = max(0, -diff)`.
   4. If `current_positive > positive`, add the difference to `operations`.
   5. If `current_negative > negative`, add the difference to `operations`.
   6. Update `positive` and `negative`.
4. Return `operations`.

## 5. Python Code

```python
class Solution:
    def minimumOperations(self, nums, target):
        operations = 0
        positive = 0
        negative = 0

        for i in range(len(nums)):
            diff = target[i] - nums[i]

            current_positive = max(0, diff)
            current_negative = max(0, -diff)

            if current_positive > positive:
                operations += current_positive - positive

            if current_negative > negative:
                operations += current_negative - negative

            positive = current_positive
            negative = current_negative

        return operations
```

## 6. Dry Run

Consider Example 1:

```python
nums = [3, 5, 1, 2]
target = [4, 6, 2, 4]
```

The difference at each index is:

```text
diff = target - nums
     = [1, 1, 1, 2]
```

Initially:

```python
operations = 0
positive = 0
negative = 0
```

| Index | `diff` | Current positive | Current negative | New operations | Total operations |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 0 | 0 | 1 |
| 3 | 2 | 2 | 0 | 1 | 2 |

### Step-by-step

**Index 0**

```text
diff = 1
current_positive = 1
current_negative = 0

positive was 0, so add 1 operation.
operations = 1
```

**Index 1**

```text
diff = 1
current_positive = 1

The positive requirement did not increase.
No new operation is needed.
operations = 1
```

**Index 2**

```text
diff = 1
current_positive = 1

The positive requirement did not increase.
No new operation is needed.
operations = 1
```

**Index 3**

```text
diff = 2
current_positive = 2

The positive requirement increased from 1 to 2.
Add 2 - 1 = 1 operation.

operations = 2
```

Final answer:

```text
2
```

These two operations are exactly:

1. Increment the entire array once.
2. Increment the last element once.

## 7. Complexity Analysis

Let `n` be the length of the arrays.

- **Time Complexity: `O(n)`** — We traverse the arrays once and perform constant-time calculations at each index.
- **Space Complexity: `O(1)`** — We use only a fixed number of variables. We do not create a separate difference array.

## 8. Pattern

**Greedy + Difference Array**

### Key concepts

- Convert the target transformation into a difference: `target[i] - nums[i]`.
- Consecutive positions with the same required change can share an operation.
- Count only the increase in the positive or negative requirement at each position.
- Keep positive and negative changes separate.

### Related LeetCode Problems

| Problem | Pattern |
|---|---|
| #1526 — Minimum Number of Increments on Subarrays to Form a Target Array | Greedy + Difference |
| #370 — Range Addition | Difference Array |
| #1094 — Car Pooling | Difference Array + Prefix Sum |
| #1109 — Corporate Flight Bookings | Difference Array + Prefix Sum |
| #3229 — Minimum Operations to Make Array Equal to Target | Greedy + Difference Array |

---

**Key takeaway:** For range increment/decrement operations, transform the problem into the difference between the target and original arrays. The minimum operations are the increases in positive and negative requirements as we move from left to right.
