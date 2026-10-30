# 1524. Number of Sub-arrays With Odd Sum

[LeetCode Problem](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)  
**Difficulty:** Medium  
**Pattern:** Prefix Sum + Parity Counting

---

## 1. Question

Given an array of integers `arr`, return the number of subarrays with an **odd** sum.

Since the answer can be very large, return it modulo `10^9 + 7`.

A subarray is a contiguous part of an array.

## 2. Examples

### Example 1

**Input:** `arr = [1, 3, 5]`

**Output:** `4`

**Explanation:** All subarrays are `[1]`, `[1,3]`, `[1,3,5]`, `[3]`, `[3,5]`, and `[5]`. Their sums are `1, 4, 9, 3, 8, 5`. The odd sums are `1, 9, 3, 5`, so the answer is `4`.

### Example 2

**Input:** `arr = [2, 4, 6]`

**Output:** `0`

**Explanation:** Every subarray has an even sum.

### Example 3

**Input:** `arr = [1, 2, 3, 4, 5, 6, 7]`

**Output:** `16`

## 3. Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 100`

## 4. Approach

Use **Prefix Sum + Parity Counting**.

We only need to know whether a prefix sum is even or odd.

- Even + Even = Even
- Odd + Odd = Even
- Even + Odd = Odd

For the current prefix sum:
- If it is **odd**, subtracting a previous **even** prefix sum gives an odd subarray sum.
- If it is **even**, subtracting a previous **odd** prefix sum gives an odd subarray sum.

We maintain:
- `even = 1`: the empty prefix has sum `0`, which is even.
- `odd = 0`: no odd prefix has been seen yet.
- `prefix_sum = 0`: running prefix sum.
- `count = 0`: number of odd-sum subarrays.

## 5. Algorithm

1. Initialize `even = 1`, `odd = 0`, `prefix_sum = 0`, and `count = 0`.
2. Traverse each number in `arr`.
3. Add the number to `prefix_sum`.
4. If `prefix_sum` is odd:
   - Add `even` to `count`.
   - Increase `odd` by `1`.
5. Otherwise:
   - Add `odd` to `count`.
   - Increase `even` by `1`.
6. Return `count % (10**9 + 7)`.

## 6. Code

```python
class Solution:
    def numOfSubarrays(self, arr):
        even = 1
        odd = 0
        prefix_sum = 0
        count = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                count += even
                odd += 1
            else:
                count += odd
                even += 1

        return count % (10**9 + 7)
```

## 7. Dry Run

Input: `arr = [1, 3, 5]`

Initial values:
- `even = 1`
- `odd = 0`
- `prefix_sum = 0`
- `count = 0`

| Number | Prefix Sum | Parity | Odd subarrays added | Total count |
|---:|---:|---|---:|---:|
| 1 | 1 | Odd | `even = 1` | 1 |
| 3 | 4 | Even | `odd = 1` | 2 |
| 5 | 9 | Odd | `even = 2` | 4 |

Final answer: `4`.

## 8. Why This Works

A subarray sum from index `i` to `j` is:

`prefix_sum[j] - prefix_sum[i - 1]`

This difference is odd only when the two prefix sums have different parity:
- Odd prefix minus even prefix = odd.
- Even prefix minus odd prefix = odd.

Therefore, at each position, adding the number of previously seen prefix sums with the opposite parity counts every odd-sum subarray ending at that position exactly once.

## 9. Complexity

- **Time Complexity:** `O(n)` — the array is traversed once.
- **Space Complexity:** `O(1)` — only a fixed number of variables are used.

## 10. Pattern

**Prefix Sum + Parity Counting**

Remember:
- Start with `even = 1` because the empty prefix sum is zero (even).
- An odd current prefix pairs with all previous even prefixes.
- An even current prefix pairs with all previous odd prefixes.
- Apply modulo `10^9 + 7` when returning the answer.
