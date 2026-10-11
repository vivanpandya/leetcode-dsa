# 128. Longest Consecutive Sequence

**Difficulty:** Medium\
**LeetCode:** [Longest Consecutive
Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

------------------------------------------------------------------------

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the
longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

### Example 1

**Input:**

``` python
nums = [100, 4, 200, 1, 3, 2]
```

**Output:**

``` text
4
```

**Explanation:** The longest consecutive sequence is `[1, 2, 3, 4]`, so
its length is `4`.

### Example 2

**Input:**

``` python
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

**Output:**

``` text
9
```

### Example 3

**Input:**

``` python
nums = [1, 0, 1, 2]
```

**Output:**

``` text
3
```

### Constraints

-   `0 <= nums.length <= 10^5`
-   `-10^9 <= nums[i] <= 10^9`

------------------------------------------------------------------------

## Approach

Use a **Hash Set** to check whether numbers exist in the array in
average O(1) time.

1.  Convert `nums` into a set to remove duplicates and enable fast
    membership checks.
2.  Visit each number in the set.
3.  A number can start a consecutive sequence only when its previous
    number (`num - 1`) is not in the set.
4.  For each starting number, keep checking `num + 1`, `num + 2`, and so
    on, until the sequence ends.
5.  Track the longest sequence length and return it.

Checking only sequence beginnings prevents repeatedly counting the same
sequence.

## Algorithm

1.  Create `num_set = set(nums)`.
2.  Initialize `longest = 0`.
3.  For every `num` in `num_set`:
    -   If `num - 1` is not in `num_set`, set `current = num` and
        `length = 1`.
    -   While `current + 1` exists in `num_set`, increment `current` and
        `length`.
    -   Update `longest = max(longest, length)`.
4.  Return `longest`.

## Code

``` python
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
```

## Example Dry Run

For `nums = [100, 4, 200, 1, 3, 2]`:

-   `num_set = {100, 4, 200, 1, 3, 2}`
-   `1` starts a sequence because `0` is not in the set.
-   Check `2`, `3`, and `4`: all exist.
-   `5` does not exist, so this sequence has length `4`.
-   `100` and `200` each form sequences of length `1`.
-   The longest length is `4`, so return `4`.

## Why This Works

Every consecutive sequence has exactly one starting number: the number
whose predecessor is absent. The algorithm expands only from these
starting numbers, counts every number in each sequence, and records the
maximum length. Converting the array to a set also removes duplicates,
so duplicate values do not affect the result.

## Time Complexity

**O(n)** average time, where `n` is the number of elements in `nums`.
Building the set takes O(n), and each value is checked a constant number
of times across the sequence expansions.

## Space Complexity

**O(n)** because the hash set can store up to `n` distinct numbers.

## Pattern

**Hash Set + Sequence Start Detection**

Recognize this pattern when you need to find consecutive values in an
unsorted array efficiently. Instead of sorting, use a set for fast
lookups and begin expanding only when the previous value is missing.
