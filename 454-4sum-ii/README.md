# 454. 4Sum II

**Difficulty:** Medium\
**LeetCode:** [4Sum II](https://leetcode.com/problems/4sum-ii/)

------------------------------------------------------------------------

## Problem Statement

Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of
length `n`, return the number of tuples `(i, j, k, l)` such that:

-   `0 <= i, j, k, l < n`
-   `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

### Example 1

**Input:**

``` python
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
```

**Output:**

``` text
2
```

**Explanation:**

The two tuples are:

1.  `(0, 0, 0, 1)` → `1 + (-2) + (-1) + 2 = 0`
2.  `(1, 1, 0, 0)` → `2 + (-1) + (-1) + 0 = 0`

### Example 2

**Input:**

``` python
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
```

**Output:**

``` text
1
```

### Constraints

-   `n == nums1.length`
-   `n == nums2.length`
-   `n == nums3.length`
-   `n == nums4.length`
-   `1 <= n <= 200`
-   `-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28`

------------------------------------------------------------------------

## Approach

Use **Hash Map + Meet in the Middle**.

Checking every combination of four arrays would take `O(n^4)` time.
Instead, split the equation into two parts:

`nums1[i] + nums2[j] = -(nums3[k] + nums4[l])`

1.  Calculate every possible sum of a value from `nums1` and a value
    from `nums2`.
2.  Store each sum's frequency in a hash map called `pair_sum`.
3.  For every pair `(c, d)` from `nums3` and `nums4`, calculate
    `target = -(c + d)`.
4.  Add `pair_sum.get(target, 0)` to the answer, because it counts how
    many pairs from the first two arrays complete the sum to zero.

## Algorithm

1.  Create an empty dictionary `pair_sum`.
2.  For each `a` in `nums1`:
    -   For each `b` in `nums2`, calculate `total = a + b`.
    -   Increase `pair_sum[total]` by one.
3.  Initialize `count = 0`.
4.  For each `c` in `nums3`:
    -   For each `d` in `nums4`, calculate `target = -(c + d)`.
    -   Add the frequency of `target` in `pair_sum` to `count`.
5.  Return `count`.

## Code

``` python
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        pair_sum = {}

        for a in nums1:
            for b in nums2:
                total = a + b
                pair_sum[total] = pair_sum.get(total, 0) + 1

        count = 0

        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += pair_sum.get(target, 0)

        return count
```

## Example Dry Run

For:

``` python
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
```

Pair sums from `nums1` and `nums2`:

-   `1 + (-2) = -1` → frequency of `-1` is `1`
-   `1 + (-1) = 0` → frequency of `0` is `1`
-   `2 + (-2) = 0` → frequency of `0` becomes `2`
-   `2 + (-1) = 1` → frequency of `1` is `1`

So `pair_sum = {-1: 1, 0: 2, 1: 1}`.

Now check pairs from `nums3` and `nums4`:

-   `-1 + 0 = -1`, so target is `1`; there is `1` matching pair.
-   `-1 + 2 = 1`, so target is `-1`; there is `1` matching pair.
-   `2 + 0 = 2`, so target is `-2`; there are no matching pairs.
-   `2 + 2 = 4`, so target is `-4`; there are no matching pairs.

The total count is `2`.

## Why This Works

Every valid tuple can be split into a pair from `nums1` and `nums2`, and
a pair from `nums3` and `nums4`. For each second pair, the hash map
tells us exactly how many first pairs have the opposite sum. Adding
these frequencies counts every valid tuple once, including different
index combinations that produce the same values.

## Time Complexity

**O(n\^2)** average time. There are `n^2` pairs processed for the first
two arrays and `n^2` pairs processed for the last two arrays.

## Space Complexity

**O(n\^2)** because the hash map can store up to `n^2` distinct pair
sums.

## Pattern

**Hash Map + Frequency Counting + Meet in the Middle**

Use this pattern when a problem combines four choices or values in an
equation. Split the equation into two groups, store the sums from one
group, and look up the complementary sums from the other group. This
reduces the time from `O(n^4)` to `O(n^2)`.
