# 713. Subarray Product Less Than K

**LeetCode:** [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)  
**Difficulty:** Medium  
**Pattern:** Variable-Size Sliding Window

---

## 1. Question

Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays where the product of all elements is **strictly less than** `k`.

## 2. Examples

### Example 1

**Input:** `nums = [10,5,2,6]`, `k = 100`  
**Output:** `8`

Valid subarrays: `[10]`, `[5]`, `[2]`, `[6]`, `[10,5]`, `[5,2]`, `[2,6]`, `[5,2,6]`.

The subarray `[10,5,2]` is excluded because its product is `100`, which is not strictly less than `k`.

### Example 2

**Input:** `nums = [1,2,3]`, `k = 0`  
**Output:** `0`

Every element is positive, so no subarray product can be less than `0`.

## 3. Approach

Use a **variable-size sliding window**.

- `left` marks the start of the current window.
- `right` expands the window.
- `product` stores the product of the current window.
- If `product >= k`, shrink the window from the left until the product is less than `k`.
- Add `right - left + 1` to the answer, because that many valid subarrays end at `right`.

All array elements are positive, so the sliding-window method works.

## 4. Algorithm

1. If `k <= 1`, return `0`.
2. Initialize `left = 0`, `product = 1`, and `count = 0`.
3. For each `right` index:
   - Multiply `product` by `nums[right]`.
   - While `product >= k`, divide by `nums[left]` and increment `left`.
   - Add `right - left + 1` to `count`.
4. Return `count`.

## 5. Code

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count
```

## 6. Dry Run

For `nums = [10,5,2,6]`, `k = 100`:

| Right | Added number | Product after shrinking | New valid subarrays | Total |
|---:|---:|---:|---:|---:|
| 0 | 10 | 10 | 1 | 1 |
| 1 | 5 | 50 | 2 | 3 |
| 2 | 2 | 10 | 2 | 5 |
| 3 | 6 | 60 | 3 | 8 |

At `right = 2`, the product becomes `100`. Because it must be **strictly less** than `100`, remove `10` from the left. The remaining window `[5,2]` has product `10`.

**Final output:** `8`

## 7. Complexity

Let `n = len(nums)`.

- **Time Complexity:** `O(n)` — each pointer moves forward at most `n` times.
- **Space Complexity:** `O(1)` — only a few variables are used.

## 8. Pattern

**Sliding Window — Count Valid Subarrays**

Remember this line:

```python
count += right - left + 1
```

When the current window is valid, every subarray ending at `right` and starting between `left` and `right` is also valid. So there are `right - left + 1` new valid subarrays.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`
