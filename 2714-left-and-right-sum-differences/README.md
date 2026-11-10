# 2574. Left and Right Sum Differences

[LeetCode Problem](https://leetcode.com/problems/left-and-right-sum-differences/)  
**Difficulty:** Easy  
**Topics:** Array, Prefix Sum

---

## 1. Problem Statement

You are given a 0-indexed integer array `nums` of size `n`.

Define two arrays:

- `leftSum[i]`: The sum of all elements to the left of index `i`. If there are no elements to the left, its value is `0`.
- `rightSum[i]`: The sum of all elements to the right of index `i`. If there are no elements to the right, its value is `0`.

Return an integer array `answer` where:

```python
answer[i] = abs(leftSum[i] - rightSum[i])
```

## 2. Examples

### Example 1

```text
Input:  nums = [10,4,8,3]
Output: [15,1,11,22]
```

**Explanation:**

```text
leftSum  = [0, 10, 14, 22]
rightSum = [15, 11,  3,  0]

answer = [|0 - 15|, |10 - 11|, |14 - 3|, |22 - 0|]
       = [15, 1, 11, 22]
```

### Example 2

```text
Input:  nums = [1]
Output: [0]
```

**Explanation:** There are no elements to the left or right, so both sums are `0`.

## 3. Approach — Total Sum + Running Left Sum

We do not need to create separate `leftSum` and `rightSum` arrays.

First, calculate the sum of the entire array:

```python
total_sum = sum(nums)
```

Then traverse the array while maintaining `left_sum`.

For the current index `i`:

- `left_sum` contains the sum of elements before index `i`.
- `right_sum` is the total sum minus the left sum and the current element.

Therefore:

```python
right_sum = total_sum - left_sum - nums[i]
```

Calculate the absolute difference and then add the current element to `left_sum` for the next iteration.

**Important:** We must subtract `nums[i]` as well. The right sum contains only elements strictly to the right of the current index.

## 4. Algorithm

1. Calculate `total_sum = sum(nums)`.
2. Initialize `left_sum = 0`.
3. Create an empty array `answer`.
4. Traverse every index `i`:
   - Calculate `right_sum = total_sum - left_sum - nums[i]`.
   - Calculate `difference = abs(left_sum - right_sum)`.
   - Append `difference` to `answer`.
   - Update `left_sum += nums[i]`.
5. Return `answer`.

## 5. Python Solution

```python
class Solution:
    def leftRightDifference(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            difference = abs(left_sum - right_sum)
            answer.append(difference)

            left_sum += nums[i]

        return answer
```

## 6. Dry Run

Consider:

```python
nums = [10, 4, 8, 3]
```

First calculate:

```text
total_sum = 10 + 4 + 8 + 3 = 25
left_sum = 0
answer = []
```

| Index `i` | `nums[i]` | `left_sum` | `right_sum = total_sum - left_sum - nums[i]` | Difference |
|---:|---:|---:|---:|---:|
| 0 | 10 | 0 | 25 - 0 - 10 = 15 | \|0 - 15\| = 15 |
| 1 | 4 | 10 | 25 - 10 - 4 = 11 | \|10 - 11\| = 1 |
| 2 | 8 | 14 | 25 - 14 - 8 = 3 | \|14 - 3\| = 11 |
| 3 | 3 | 22 | 25 - 22 - 3 = 0 | \|22 - 0\| = 22 |

After each iteration, update `left_sum` by adding the current element.

Final arrays:

```text
leftSum  = [0, 10, 14, 22]
rightSum = [15, 11, 3, 0]
answer   = [15, 1, 11, 22]
```

**Final output:**

```text
[15, 1, 11, 22]
```

## 7. Why This Works

The total sum contains every element in the array.

At index `i`, the array is divided into three parts:

1. Elements before `i` — their sum is `left_sum`.
2. The current element — its value is `nums[i]`.
3. Elements after `i` — their sum is `right_sum`.

So:

```python
right_sum = total_sum - left_sum - nums[i]
```

This gives exactly the sum of elements to the right of the current index. Taking the absolute difference between the left and right sums produces the required answer.

## 8. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity: O(n)** — `sum(nums)` takes O(n), and the loop visits each element once. Total time is O(n).
- **Auxiliary Space Complexity: O(1)** — Only `total_sum`, `left_sum`, `right_sum`, and `difference` are used, excluding the output.
- **Output Space Complexity: O(n)** — The `answer` array stores `n` values.

## 9. Pattern

**Prefix Sum + Running Sum**

Remember:

- Calculate the total sum once.
- Maintain the sum of elements on the left.
- Derive the right sum using the total sum.
- Exclude the current element from the right sum.

**Key formula:**

```python
right_sum = total_sum - left_sum - nums[i]
```

This avoids building separate left and right sum arrays.
