# 2845. Count of Interesting Subarrays

[LeetCode Problem](https://leetcode.com/problems/count-of-interesting-subarrays/)  
**Difficulty:** Medium  
**Pattern:** Prefix Sum + HashMap + Modulo

---

## 1. Question

You are given a 0-indexed integer array `nums`, an integer `modulo`, and an integer `k`.

A non-empty contiguous subarray `nums[l..r]` is **interesting** if:

1. Count the indices `i` in the subarray for which `nums[i] % modulo == k`.
2. Let this count be `cnt`. The subarray is interesting when `cnt % modulo == k`.

Return the total number of interesting subarrays.

## 2. Examples

### Example 1

```python
Input:
nums = [3, 2, 4]
modulo = 2
k = 1

Output: 3
```

The interesting subarrays are:

```text
[3]       -> qualifying count = 1 -> 1 % 2 = 1
[3, 2]    -> qualifying count = 1 -> 1 % 2 = 1
[3, 2, 4] -> qualifying count = 1 -> 1 % 2 = 1
```

### Example 2

```python
Input:
nums = [3, 1, 9, 6]
modulo = 3
k = 0

Output: 2
```

The interesting subarrays are:

```text
[3, 1, 9, 6] -> qualifying count = 3 -> 3 % 3 = 0
[1]          -> qualifying count = 0 -> 0 % 3 = 0
```

## 3. Approach – Prefix Sum + HashMap + Modulo

We do not need to store the actual values in each subarray. Convert each number into an indicator:

- If `num % modulo == k`, it contributes `1`.
- Otherwise, it contributes `0`.

Now the problem becomes:

**Count subarrays whose sum of indicators has remainder `k` when divided by `modulo`.**

Use a prefix sum to count how many qualifying elements have appeared so far.

Let:
- `prefix_sum` be the number of qualifying elements seen so far.
- `remainder = prefix_sum % modulo`.

For a subarray to be interesting, the difference between the current prefix sum and an earlier prefix sum must have remainder `k`.

```text
(current_prefix - previous_prefix) % modulo = k
```

Rearranging:

```text
previous_prefix % modulo
    = (current_prefix % modulo - k) % modulo
```

Therefore, for each current prefix remainder, look up how many earlier prefix sums have the required remainder.

Store the frequency of each prefix remainder in a HashMap.

**Important:** Start with `prefix_count = {0: 1}`. This represents the empty prefix, allowing subarrays that begin at index `0` to be counted.

## 4. Algorithm

1. Initialize `prefix_count = {0: 1}`.
2. Initialize `prefix_sum = 0` and `result = 0`.
3. Traverse each number in `nums`.
4. If `num % modulo == k`, increment `prefix_sum` by `1`.
5. Calculate the current remainder: `remainder = prefix_sum % modulo`.
6. Calculate the needed previous remainder: `target = (remainder - k) % modulo`.
7. Add `prefix_count.get(target, 0)` to `result`.
8. Increase the frequency of the current `remainder` in the HashMap.
9. Return `result`.

## 5. Code

```python
class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix_sum += 1

            remainder = prefix_sum % modulo
            target = (remainder - k) % modulo

            result += prefix_count.get(target, 0)

            prefix_count[remainder] = prefix_count.get(remainder, 0) + 1

        return result
```

## 6. Dry Run

Input:

```python
nums = [3, 2, 4]
modulo = 2
k = 1
```

### Step 1: Convert numbers into indicators

| Number | Check (`num % 2 == 1`) | Indicator |
|---:|---|---:|
| 3 | True | 1 |
| 2 | False | 0 |
| 4 | False | 0 |

The indicator sequence is:

```text
[1, 0, 0]
```

### Step 2: Initialize

```text
prefix_sum = 0
result = 0
prefix_count = {0: 1}
```

### Step 3: Process each element

| num | Indicator added | Prefix sum | Remainder | Target `(remainder - 1) % 2` | Added to result |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 1 |
| 4 | 0 | 1 | 1 | 0 | 1 |

The remainder `0` initially has frequency `1`, representing the empty prefix. Each of the three current positions finds that matching earlier prefix and contributes one interesting subarray.

Final result:

```python
return 3
```

## 7. Complexity

Let `n` be the length of `nums`.

- **Time Complexity: `O(n)`** – We traverse the array once. HashMap lookups and updates take `O(1)` average time.
- **Space Complexity: `O(min(n, modulo))`** – The HashMap stores frequencies for at most `min(n + 1, modulo)` distinct remainders, which is `O(min(n, modulo))`.

## 8. Pattern

**Prefix Sum + HashMap + Modulo**

Related problems:
- #560 – Subarray Sum Equals K
- #523 – Continuous Subarray Sum
- #974 – Subarray Sums Divisible by K
- #2845 – Count of Interesting Subarrays

**Key takeaway:** Turn the condition into a prefix sum of qualifying elements. Then use modulo remainders and a frequency HashMap to count valid subarrays in one pass.

Remember the two key lines:

```python
target = (remainder - k) % modulo
result += prefix_count.get(target, 0)
```

The target remainder tells us how many earlier prefix sums can form an interesting subarray ending at the current index.
