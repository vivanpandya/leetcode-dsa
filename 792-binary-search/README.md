# 704. Binary Search

[LeetCode Problem](https://leetcode.com/problems/binary-search/)  
**Difficulty:** Easy  
**Topics:** Array, Binary Search

---

## Question

Given an array of integers `nums` sorted in ascending order and an integer `target`, return the index of `target` if it exists. Otherwise, return `-1`.

You must solve the problem in **O(log n)** time.

### Example 1

```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists at index 4.
```

### Example 2

```text
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums.
```

### Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

## 1. Approach – Binary Search

Since the array is sorted, we can use **Binary Search** rather than checking every element.

Binary Search repeatedly divides the search range into two halves. We maintain two pointers:

- `left`: the first index in the current search range.
- `right`: the last index in the current search range.

At each step, calculate the middle index and compare `nums[mid]` with `target`:

- If they are equal, return `mid`.
- If `nums[mid]` is smaller, the target can only be in the right half.
- If `nums[mid]` is greater, the target can only be in the left half.

If the range becomes empty, return `-1`.

## 2. Algorithm

1. Set `left = 0` and `right = len(nums) - 1`.
2. Continue while `left <= right`.
3. Calculate `mid = (left + right) // 2`.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`, set `left = mid + 1`.
6. Otherwise, set `right = mid - 1`.
7. If the loop ends, return `-1`.

## 3. Code

```python
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

## 4. Example / Dry Run

**Input:**

```python
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```

| Iteration | left | right | mid | nums[mid] | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 5 | 2 | 3 | `3 < 9`, search right half |
| 2 | 3 | 5 | 4 | 9 | Target found |

At the second iteration, `nums[4] == 9`.

**Output:**

```python
4
```

### Dry Run When the Target Is Missing

**Input:**

```python
nums = [-1, 0, 3, 5, 9, 12]
target = 2
```

| Iteration | left | right | mid | nums[mid] | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 5 | 2 | 3 | `3 > 2`, search left half |
| 2 | 0 | 1 | 0 | -1 | `-1 < 2`, search right half |
| 3 | 1 | 1 | 1 | 0 | `0 < 2`, search right half |

Now `left = 2` and `right = 1`. Since `left > right`, the loop stops.

**Output:**

```python
-1
```

## 5. Why This Works

The array is sorted:

- If `nums[mid] < target`, every element at or before `mid` is too small, so we can discard that half.
- If `nums[mid] > target`, every element at or after `mid` is too large, so we can discard that half.
- If `nums[mid] == target`, we have found the required index.

Each comparison removes about half of the remaining search range, so the target can be found efficiently.

## 6. Complexity Analysis

- **Time Complexity: O(log n)** — The search range is halved in every iteration.
- **Space Complexity: O(1)** — Only a fixed number of variables are used.

## 7. Pattern

**Pattern:** Binary Search on a Sorted Array

Remember the two pointer updates:

```python
# Target is in the right half
left = mid + 1

# Target is in the left half
right = mid - 1
```

**Important:** A linear search takes `O(n)` time and does not satisfy this problem's required `O(log n)` runtime.

### Binary Search Template

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```
