# LeetCode 167 — Two Sum II: Input Array Is Sorted

**Difficulty:** Medium  
**Topics:** Array, Two Pointers  
**LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## 1. Question

You are given a **1-indexed** integer array `numbers` sorted in non-decreasing order. Find two numbers that add up to `target` and return their indices as `[index1, index2]`.

- `index1 < index2`
- You cannot use the same element twice.
- Exactly one solution exists.
- Use only constant extra space.

## 2. Examples

**Example 1**
```python
numbers = [2, 7, 11, 15]
target = 9
# Output: [1, 2]
```
Explanation: `2 + 7 = 9`.

**Example 2**
```python
numbers = [2, 3, 4]
target = 6
# Output: [1, 3]
```
Explanation: `2 + 4 = 6`.

**Example 3**
```python
numbers = [-1, 0]
target = -1
# Output: [1, 2]
```
Explanation: `-1 + 0 = -1`.

## 3. Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- Exactly one solution exists.

## 4. Approach

Use **Two Pointers**:
- `left` starts at the beginning.
- `right` starts at the end.
- If the sum is too small, move `left` forward.
- If the sum is too large, move `right` backward.
- If the sum equals `target`, return the two 1-based indices.

## 5. Algorithm

1. Set `left = 0` and `right = len(numbers) - 1`.
2. While `left < right`, calculate `total = numbers[left] + numbers[right]`.
3. If `total == target`, return `[left + 1, right + 1]`.
4. If `total < target`, increment `left`; otherwise, decrement `right`.
5. The problem guarantees a solution.

## 6. Python Code

```python
class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
```

## 7. Dry Run

Input: `numbers = [2, 7, 11, 15]`, `target = 9`

| Left index | Right index | Values | Sum | Action |
|---:|---:|---|---:|---|
| 0 | 3 | 2 + 15 | 17 | Too large; move `right` left |
| 0 | 2 | 2 + 11 | 13 | Too large; move `right` left |
| 0 | 1 | 2 + 7 | 9 | Target found |

The zero-based indices are `0` and `1`, so the required 1-based output is `[1, 2]`.

## 8. Why This Works

Because the array is sorted, moving `left` forward increases or preserves the sum, while moving `right` backward decreases or preserves it. When the current sum is too small or too large, the corresponding pointer move safely eliminates impossible pairs. The pointers eventually reach the unique solution.

## 9. Complexity Analysis

- **Time Complexity:** `O(n)` — each pointer moves inward at most `n` times.
- **Auxiliary Space Complexity:** `O(1)` — only a constant number of variables are used.

## 10. Pattern

**Two Pointers on a Sorted Array**

Use this pattern when searching for a pair in a sorted array that satisfies a target sum.

**Important:** The problem requires **1-based indices**, so return `[left + 1, right + 1]`.
