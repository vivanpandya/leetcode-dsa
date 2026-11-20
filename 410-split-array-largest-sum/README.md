# 410. Split Array Largest Sum

[LeetCode Problem](https://leetcode.com/problems/split-array-largest-sum/)

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Topics
- Array
- Binary Search
- Greedy

---

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty contiguous subarrays such that the largest sum among these subarrays is minimized.

Return the minimized largest subarray sum.

A subarray is a contiguous part of an array.

### Example 1

**Input:**
```python
nums = [7, 2, 5, 10, 8]
k = 2
```

**Output:**
```python
18
```

**Explanation:**

The best split is `[7, 2, 5]` and `[10, 8]`.

Their sums are `14` and `18`, so the largest sum is `18`.

### Example 2

**Input:**
```python
nums = [1, 2, 3, 4, 5]
k = 2
```

**Output:**
```python
9
```

**Explanation:**

The best split is `[1, 2, 3]` and `[4, 5]`.

Their sums are `6` and `9`, so the largest sum is `9`.

### Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= min(50, nums.length)`

---

## 2. Approach: Binary Search on Answer + Greedy

Instead of trying every possible way to split the array, binary search the answer.

The answer represents the maximum sum allowed for any one subarray.

### Search space

The minimum possible answer is:

```python
left = max(nums)
```

Every element must belong to a subarray, so the largest subarray sum cannot be smaller than the largest individual element.

The maximum possible answer is:

```python
right = sum(nums)
```

The entire array could be placed into one subarray, whose sum is the total sum.

Therefore, the answer lies between `max(nums)` and `sum(nums)`.

### Greedy feasibility check

For a candidate maximum sum `mid`, count how many subarrays are needed if no subarray can have a sum greater than `mid`.

Traverse the array in its original order:

- Start with one subarray and `current_sum = 0`.
- If adding the next number keeps the sum at most `mid`, add it to the current subarray.
- Otherwise, start a new subarray with that number.

After traversing the array:

- If the number of subarrays is `<= k`, `mid` is feasible. Try a smaller capacity.
- If the number of subarrays is `> k`, the capacity is too small. Increase it.

Because all elements are non-negative and `k <= len(nums)`, a split into at most `k` subarrays can be divided further into exactly `k` non-empty subarrays without increasing any subarray sum.

---

## 3. Algorithm

1. Set `left = max(nums)` and `right = sum(nums)`.
2. While `left < right`:
   1. Calculate `mid = (left + right) // 2`.
   2. Initialize `subarrays = 1` and `current_sum = 0`.
   3. Traverse every number in `nums`:
      - If `current_sum + num <= mid`, add `num` to `current_sum`.
      - Otherwise, increment `subarrays` and set `current_sum = num`.
   4. If `subarrays <= k`, the candidate is feasible, so set `right = mid`.
   5. Otherwise, set `left = mid + 1`.
3. Return `left`.

---

## 4. Python Code

```python
class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= mid:
                    current_sum += num
                else:
                    subarrays += 1
                    current_sum = num

            if subarrays <= k:
                right = mid
            else:
                left = mid + 1

        return left
```

---

## 5. Dry Run

**Input:**

```python
nums = [7, 2, 5, 10, 8]
k = 2
```

Initial boundaries:

```text
left = max(nums) = 10
right = sum(nums) = 32
```

### Binary search iterations

| `left` | `right` | `mid` | Subarrays needed | Decision |
|---:|---:|---:|---:|---|
| 10 | 32 | 21 | 2 | Feasible: `right = 21` |
| 10 | 21 | 15 | 3 | Not feasible: `left = 16` |
| 16 | 21 | 18 | 2 | Feasible: `right = 18` |
| 16 | 18 | 17 | 3 | Not feasible: `left = 18` |

Now `left = right = 18`, so the loop stops.

### Check the final answer

For `mid = 18`, the greedy traversal creates:

```text
Subarray 1: [7, 2, 5]  -> sum = 14
Subarray 2: [10, 8]    -> sum = 18
```

The number of subarrays is `2`, equal to `k`.

**Output:**
```python
18
```

---

## 6. Why This Works

The greedy check calculates the minimum number of contiguous subarrays needed for a chosen maximum sum.

- If the check needs more than `k` subarrays, the candidate maximum sum is too small.
- If it needs at most `k` subarrays, the candidate is feasible. We can split some subarrays further to obtain exactly `k` non-empty subarrays without increasing any sum.

Feasibility is monotonic:

- If a maximum sum is feasible, any larger maximum sum is also feasible.
- If a maximum sum is not feasible, any smaller maximum sum is also not feasible.

This monotonic property allows binary search on the answer.

---

## 7. Complexity Analysis

Let `n` be the length of `nums`, and let `S = sum(nums)`.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(n * log(S - max(nums) + 1))` | Binary search checks the possible sums. Each feasibility check traverses the array once. |
| Auxiliary Space | `O(1)` | Only a fixed number of variables are used. |

A commonly used simplified time complexity is:

- **Time:** `O(n * log(sum(nums)))`
- **Auxiliary Space:** `O(1)`

---

## 8. Pattern and Related Problems

**Pattern:** Binary Search on Answer + Greedy Feasibility Check.

Look for this pattern when:
- The problem asks to minimize the maximum value or maximize the minimum value.
- You can test whether a proposed answer is feasible.
- Feasibility changes monotonically as the candidate answer increases or decreases.

Related LeetCode problems:

| Problem | LeetCode Number | Pattern |
|---|---:|---|
| Koko Eating Bananas | 875 | Binary Search on Answer |
| Capacity To Ship Packages Within D Days | 1011 | Binary Search on Answer + Greedy |
| Split Array Largest Sum | 410 | Binary Search on Answer + Greedy |

### Important boundary rule

For problems that minimize the largest subarray or group sum:

```python
left = max(nums)
right = sum(nums)
```

- `max(nums)` is the smallest possible capacity.
- `sum(nums)` is the largest possible capacity.
