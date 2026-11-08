# 974. Subarray Sums Divisible by K

[LeetCode Problem](https://leetcode.com/problems/subarray-sums-divisible-by-k/)  
**Difficulty:** Medium  
**Pattern:** Prefix Sum + HashMap + Modulo

---

## 1. Question

Given an integer array `nums` and an integer `k`, return the number of non-empty contiguous subarrays whose sum is divisible by `k`.

A sum is divisible by `k` when its remainder after division by `k` is zero.

## 2. Examples

### Example 1

```python
Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
```

The seven valid subarrays are:

```text
[4, 5, 0, -2, -3, 1]
[5]
[5, 0]
[5, 0, -2, -3]
[0]
[0, -2, -3]
[-2, -3]
```

### Example 2

```python
Input: nums = [5], k = 9
Output: 0
```

The only non-empty subarray has sum 5, which is not divisible by 9.

## 3. Approach – Prefix Sum + HashMap

We use **Prefix Sum and HashMap** to count valid subarrays in one traversal.

Let:
- `prefix_sum` be the sum of all elements from the beginning up to the current index.
- `remainder = prefix_sum % k`.

The key observation is:

**If two prefix sums have the same remainder when divided by `k`, the sum of the elements between those two prefix positions is divisible by `k`.**

Why?

If:

```text
prefix_sum_1 % k == prefix_sum_2 % k
```

then:

```text
(prefix_sum_2 - prefix_sum_1) % k == 0
```

That difference is the sum of the subarray between the two prefix positions.

We store how many times each remainder has appeared in a HashMap. Whenever the current remainder has appeared before, each previous occurrence forms one valid subarray ending at the current index.

**Important:** Initialize the HashMap as `{0: 1}`. This represents the empty prefix with sum zero and allows us to count valid subarrays that start at index 0.

Python's modulo operator returns a non-negative remainder for a positive divisor, so negative numbers are handled correctly.

## 4. Algorithm

1. Initialize `prefix_count = {0: 1}`.
2. Initialize `prefix_sum = 0` and `count = 0`.
3. Traverse every number in `nums`.
4. Add the current number to `prefix_sum`.
5. Calculate `remainder = prefix_sum % k`.
6. Add the frequency of this remainder in the HashMap to `count`.
7. Increase the frequency of this remainder in the HashMap.
8. Return `count`.

## 5. Code

```python
class Solution:
    def subarraysDivByK(self, nums, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            count += prefix_count.get(remainder, 0)

            prefix_count[remainder] = prefix_count.get(remainder, 0) + 1

        return count
```

## 6. Dry Run

Input:

```python
nums = [4, 5, 0, -2, -3, 1]
k = 5
```

Initial values:

```text
prefix_sum = 0
count = 0
prefix_count = {0: 1}
```

Now process each number:

| num | Prefix Sum | Remainder (`prefix_sum % 5`) | Previous frequency | Count |
|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 0 | 0 |
| 5 | 9 | 4 | 1 | 1 |
| 0 | 9 | 4 | 2 | 3 |
| -2 | 7 | 2 | 0 | 3 |
| -3 | 4 | 4 | 3 | 6 |
| 1 | 5 | 0 | 1 | 7 |

### Understanding one iteration

When `num = 5`:

```text
prefix_sum = 4 + 5 = 9
remainder = 9 % 5 = 4
```

Remainder `4` has appeared once before, so one new valid subarray is found:

```text
[5]
```

When `num = 0`:

```text
prefix_sum = 9
remainder = 9 % 5 = 4
```

Remainder `4` has appeared twice before, so two more valid subarrays are found:

```text
[5, 0]
[4, 5, 0, -2, -3, 1]  # This full-array subarray is counted later,
                       # when its final prefix remainder is processed.
```

The frequency lookup counts subarrays ending at the current index; the table above shows the running count after each iteration.

Final result:

```python
return 7
```

## 7. Complexity

Let `n` be the length of `nums`.

- **Time Complexity: `O(n)`** – We traverse the array once. HashMap lookups and updates take `O(1)` average time.
- **Space Complexity: `O(min(n, k))`** – There are at most `k` possible remainders (`0` through `k - 1`), and at most `n + 1` prefix positions.

## 8. Pattern

**Prefix Sum + HashMap + Modulo**

Related LeetCode problems:
- #560 – Subarray Sum Equals K
- #523 – Continuous Subarray Sum
- #974 – Subarray Sums Divisible by K
- #2845 – Count of Interesting Subarrays

**Key takeaway:** Equal prefix-sum remainders mean the subarray between those prefix positions has a sum divisible by `k`.

Remember these two lines:

```python
count += prefix_count.get(remainder, 0)
prefix_count[remainder] = prefix_count.get(remainder, 0) + 1
```

First count the earlier matching remainders, then record the current one.
