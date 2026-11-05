# 303. Range Sum Query - Immutable

**Difficulty:** Easy  
**LeetCode:** https://leetcode.com/problems/range-sum-query-immutable/

---

## Problem Statement

Given an integer array `nums`, implement the `NumArray` class to handle multiple range-sum queries.

- `NumArray(nums)` initializes the object with the given array.
- `sumRange(left, right)` returns the sum of elements from index `left` to index `right`, inclusive.

## Example

```text
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output:
[null, 1, -1, -3]
```

Explanation:

```text
nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) = -2 + 0 + 3 = 1
sumRange(2, 5) = 3 + (-5) + 2 + (-1) = -1
sumRange(0, 5) = -2 + 0 + 3 + (-5) + 2 + (-1) = -3
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

---

## Approach: Prefix Sum

Calculating the sum from `left` to `right` by looping through the array for every query can take O(n) time per query. Since many queries may be made, we can optimize this using a **prefix sum array**.

A prefix sum stores the cumulative sum of elements from the beginning of the array.

We create a prefix array with an extra `0` at the beginning:

```text
nums   = [-2, 0, 3, -5, 2, -1]
prefix = [ 0,-2,-2,  1,-4,-2,-3]
```

The extra zero makes range calculations easier.

### Formula

```text
sumRange(left, right) = prefix[right + 1] - prefix[left]
```

The prefix sum at `right + 1` includes all elements up to `right`. Subtracting the prefix sum at `left` removes all elements before `left`.

## Algorithm

### Initialization

1. Create `self.prefix = [0]`.
2. Traverse every number in `nums`.
3. Append the previous prefix sum plus the current number.

### Range Query

1. Receive `left` and `right`.
2. Calculate `self.prefix[right + 1] - self.prefix[left]`.
3. Return the result.

## Python Code

```python
class NumArray:

    def __init__(self, nums):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

## Dry Run

Input:

```python
nums = [-2, 0, 3, -5, 2, -1]
```

### Step 1: Build the prefix sum array

Start with:

```text
prefix = [0]
```

Process each number:

| Number | Calculation | Updated prefix |
|---:|---|---|
| -2 | 0 + (-2) | `[0, -2]` |
| 0 | -2 + 0 | `[0, -2, -2]` |
| 3 | -2 + 3 | `[0, -2, -2, 1]` |
| -5 | 1 + (-5) | `[0, -2, -2, 1, -4]` |
| 2 | -4 + 2 | `[0, -2, -2, 1, -4, -2]` |
| -1 | -2 + (-1) | `[0, -2, -2, 1, -4, -2, -3]` |

Final prefix array:

```text
[0, -2, -2, 1, -4, -2, -3]
```

### Step 2: Query `sumRange(0, 2)`

```text
prefix[2 + 1] - prefix[0]
= prefix[3] - prefix[0]
= 1 - 0
= 1
```

### Step 3: Query `sumRange(2, 5)`

```text
prefix[5 + 1] - prefix[2]
= prefix[6] - prefix[2]
= -3 - (-2)
= -1
```

### Step 4: Query `sumRange(0, 5)`

```text
prefix[5 + 1] - prefix[0]
= prefix[6] - prefix[0]
= -3 - 0
= -3
```

Final output:

```text
[null, 1, -1, -3]
```

## Why This Works

`prefix[i]` stores the sum of all elements before index `i`.

- `prefix[right + 1]` contains the sum from the beginning through `right`.
- `prefix[left]` contains the sum of all elements before `left`.

Subtracting the second value from the first leaves exactly the sum from `left` through `right`.

The prefix array is built once, so each query requires only one subtraction.

## Complexity Analysis

Let `n` be the length of `nums`.

| Operation | Time Complexity |
|---|---|
| Build prefix sum | O(n) |
| Each `sumRange()` query | O(1) |

- **Time Complexity:** O(n) for initialization and O(1) for each query.
- **Space Complexity:** O(n) for storing the prefix sum array.

## Pattern

**Prefix Sum — Range Sum Queries**

Use this pattern when:
- Many queries ask for the sum of a continuous range.
- The array does not change between queries.
- You want to avoid recalculating each range sum from scratch.

**Important formula:**

```python
prefix[right + 1] - prefix[left]
```

**Key takeaway:** Precompute cumulative sums once, then answer every range-sum query in O(1) time.
