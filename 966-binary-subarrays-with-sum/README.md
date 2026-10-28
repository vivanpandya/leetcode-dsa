# 930. Binary Subarrays With Sum

**LeetCode:** https://leetcode.com/problems/binary-subarrays-with-sum/  
**Difficulty:** Medium  
**Pattern:** Sliding Window — At Most Trick

---

## Question

Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to `goal`.

A subarray is a contiguous part of an array.

## Examples

### Example 1

**Input**
```python
nums = [1, 0, 1, 0, 1]
goal = 2
```

**Output**
```text
4
```

**Explanation:** The four subarrays are `[1, 0, 1]` (indices 0–2), `[1, 0, 1, 0]` (indices 0–3), `[0, 1, 0, 1]` (indices 1–4), and `[1, 0, 1]` (indices 2–4).

### Example 2

**Input**
```python
nums = [0, 0, 0, 0, 0]
goal = 0
```

**Output**
```text
15
```

**Explanation:** Every non-empty subarray has sum `0`. The number of subarrays is `n * (n + 1) // 2 = 5 * 6 // 2 = 15`.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `nums[i]` is either `0` or `1`.
- `0 <= goal <= nums.length`

---

## Approach

Use the **Sliding Window + At Most Trick**.

Count subarrays whose sum is at most a value `k`, then subtract:

`number of subarrays with sum exactly goal = atMost(goal) - atMost(goal - 1)`

- `atMost(goal)` counts subarrays with sum `goal` or less.
- `atMost(goal - 1)` counts subarrays with sum strictly less than `goal`.
- Subtracting leaves only subarrays whose sum is exactly `goal`.

Because the array contains only `0`s and `1`s, the sliding window can shrink whenever its sum becomes greater than `k`.

## Algorithm

1. Define a helper function `atMost(k)`.
2. If `k < 0`, return `0`.
3. Initialize `left = 0`, `current_sum = 0`, and `count = 0`.
4. Move `right` through `nums`:
   - Add `nums[right]` to `current_sum`.
   - While `current_sum > k`, subtract `nums[left]` and move `left` forward.
   - Add `right - left + 1` to `count`, because every subarray ending at `right` and starting from `left` through `right` has sum at most `k`.
5. Return `atMost(goal) - atMost(goal - 1)`.

## Code

```python
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            current_sum = 0
            count = 0

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)
```

## Dry Run

For `nums = [1, 0, 1, 0, 1]` and `goal = 2`, first calculate `atMost(2)`.

| `right` | `nums[right]` | Window after shrinking | Window sum | New subarrays (`right - left + 1`) | Running count |
|---:|---:|---|---:|---:|---:|
| 0 | 1 | `[1]` | 1 | 1 | 1 |
| 1 | 0 | `[1, 0]` | 1 | 2 | 3 |
| 2 | 1 | `[1, 0, 1]` | 2 | 3 | 6 |
| 3 | 0 | `[1, 0, 1, 0]` | 2 | 4 | 10 |
| 4 | 1 | `[0, 1, 0, 1]` | 2 | 4 | 14 |

So `atMost(2) = 14`.

Now `atMost(1) = 10`.

Therefore:

`atMost(2) - atMost(1) = 14 - 10 = 4`

**Output:** `4`

### Example 2 dry run

For `[0, 0, 0, 0, 0]`, `goal = 0`:

- `atMost(0) = 15`, because every subarray has sum zero.
- `atMost(-1) = 0`.
- Answer = `15 - 0 = 15`.

## Why This Works

For a fixed `right`, after shrinking the window until its sum is at most `k`, every starting index from `left` through `right` creates a valid subarray. There are `right - left + 1` such subarrays, so adding that value counts all subarrays with sum at most `k` exactly once.

Subtracting the counts for `goal` and `goal - 1` leaves only subarrays with sum exactly `goal`.

## Complexity

- **Time Complexity:** `O(n)`. Each pointer moves forward at most `n` times. The helper is called twice, so total time remains linear.
- **Space Complexity:** `O(1)`. Only a fixed number of variables are used.

## Pattern

**Sliding Window + At Most Trick**

Remember:

- `exactly(goal) = atMost(goal) - atMost(goal - 1)`
- `count += right - left + 1` counts valid subarrays ending at `right`.
- If `goal == 0`, `atMost(-1)` returns `0`.
