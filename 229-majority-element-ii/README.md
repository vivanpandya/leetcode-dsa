# 229. Majority Element II

**Difficulty:** Medium\
**LeetCode:** [Majority Element
II](https://leetcode.com/problems/majority-element-ii/)

------------------------------------------------------------------------

## Problem Statement

Given an integer array of size `n`, find all elements that appear more
than `floor(n / 3)` times.

### Example 1

**Input:**

``` python
nums = [3, 2, 3]
```

**Output:**

``` python
[3]
```

### Example 2

**Input:**

``` python
nums = [1]
```

**Output:**

``` python
[1]
```

### Example 3

**Input:**

``` python
nums = [1, 2]
```

**Output:**

``` python
[1, 2]
```

### Constraints

-   `1 <= nums.length <= 5 * 10^4`
-   `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Can you solve the problem in linear time and `O(1)`
auxiliary space?

------------------------------------------------------------------------

## Approach

Use the **Extended Boyer--Moore Voting Algorithm**.

At most **two distinct elements** can appear more than `n // 3` times.
If three different elements each appeared more than `n // 3` times,
their combined frequency would exceed `n`, which is impossible.

The algorithm has two passes:

1.  **Candidate selection:** Track two potential candidates and their
    vote counts. When the current number matches a candidate, increase
    its count. If a candidate's count is zero, assign the current number
    to that candidate. Otherwise, decrease both counts.
2.  **Verification:** Count the actual occurrences of both candidates
    and keep only those appearing more than `n // 3` times.

## Algorithm

1.  Initialize `candidate1`, `candidate2`, `count1`, and `count2`.
2.  Iterate through `nums`:
    -   If `num` matches `candidate1`, increment `count1`.
    -   Else if `num` matches `candidate2`, increment `count2`.
    -   Else if `count1 == 0`, set `candidate1 = num` and `count1 = 1`.
    -   Else if `count2 == 0`, set `candidate2 = num` and `count2 = 1`.
    -   Otherwise, decrement both counts.
3.  Reset `count1` and `count2` to zero.
4.  Traverse `nums` again to count each candidate's actual frequency.
5.  Set `threshold = len(nums) // 3`.
6.  Add each distinct candidate whose frequency is greater than
    `threshold` to `result`.
7.  Return `result`.

## Code

``` python
class Solution:
    def majorityElement(self, nums):
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1

        result = []
        threshold = len(nums) // 3

        if count1 > threshold:
            result.append(candidate1)

        if count2 > threshold and candidate2 != candidate1:
            result.append(candidate2)

        return result
```

## Example / Dry Run

Input:

``` python
nums = [1, 2]
```

**First pass --- candidate selection:**

    Number   Candidate 1   Count 1   Candidate 2   Count 2
  -------- ------------- --------- ------------- ---------
         1             1         1        `None`         0
         2             1         1             2         1

Potential candidates are `1` and `2`.

**Second pass --- verify frequencies:**

-   `1` appears once.
-   `2` appears once.
-   `threshold = 2 // 3 = 0`.

Both frequencies are greater than `0`, so the result is:

``` python
[1, 2]
```

## Why This Works

The extended Boyer--Moore algorithm cancels groups of three different
values. Such a cancellation cannot remove every occurrence of a value
that appears more than `n // 3` times, so every valid answer remains
among the two candidates. The second pass verifies which candidates
actually meet the required frequency threshold.

## Time Complexity

**O(n)** --- two passes through the array, each taking linear time.

## Space Complexity

**O(1) auxiliary space** --- the algorithm uses a fixed number of
variables, excluding the result list.

## Pattern

**Extended Boyer--Moore Voting + Candidate Verification**

Use this pattern when you need to find all elements occurring more than
`n / k` times with constant auxiliary space. The number of possible
candidates is at most `k - 1`. For the `n / 3` threshold, track two
candidates and verify them in a second pass.

### Key Takeaway

Do not assume the candidates are valid just because the voting pass
selected them. Always count their actual occurrences in the second pass.
