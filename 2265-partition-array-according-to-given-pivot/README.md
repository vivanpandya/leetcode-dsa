# 2161. Partition Array According to Given Pivot

[LeetCode Problem](https://leetcode.com/problems/partition-array-according-to-given-pivot/) | **Difficulty:** Medium

## Problem Statement

You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that:

- Every element less than `pivot` appears before every element greater than `pivot`.
- Every element equal to `pivot` appears between the elements less than and greater than `pivot`.
- The relative order of elements smaller than `pivot` is preserved, and the relative order of elements greater than `pivot` is preserved.

Return `nums` after rearranging it.

## Examples

### Example 1

**Input:**
```python
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
```

**Output:**
```python
[9, 5, 3, 10, 10, 12, 14]
```

**Explanation:** The elements smaller than `10` are `[9, 5, 3]`, the elements equal to `10` are `[10, 10]`, and the elements greater than `10` are `[12, 14]`. Their relative order is preserved within the smaller and greater groups.

### Example 2

**Input:**
```python
nums = [-3, 4, 3, 2]
pivot = 2
```

**Output:**
```python
[-3, 2, 4, 3]
```

**Explanation:** `[-3]` comes first, `[2]` comes next, and `[4, 3]` comes last. The order of `4` and `3` is preserved.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- `pivot` is an element of `nums`.

---

## 1. Question

Rearrange the array so all numbers smaller than `pivot` come first, all numbers equal to `pivot` come next, and all numbers greater than `pivot` come last. Preserve the original relative order within the smaller and greater groups.

## 2. Example

**Input:**
```python
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
```

**Output:**
```python
[9, 5, 3, 10, 10, 12, 14]
```

## 3. Approach

Use three lists:

- `less` stores numbers smaller than `pivot`.
- `equal` stores numbers equal to `pivot`.
- `greater` stores numbers greater than `pivot`.

Traverse `nums` once and append each number to its matching list. Since elements are appended in their original order, the relative order is preserved. Finally, combine the three lists.

## 4. Algorithm

1. Create empty lists named `less`, `equal`, and `greater`.
2. Visit each number in `nums`.
3. If `num < pivot`, append it to `less`.
4. Otherwise, if `num == pivot`, append it to `equal`.
5. Otherwise, append it to `greater`.
6. Return `less + equal + greater`.

## 5. Code

```python
class Solution:
    def pivotArray(self, nums, pivot):
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return less + equal + greater
```

## 6. Dry Run

Input: `nums = [9, 12, 5, 10, 14, 3, 10]`, `pivot = 10`

| Number | Condition | List after processing |
|---:|---|---|
| `9` | Less than `10` | `less = [9]` |
| `12` | Greater than `10` | `greater = [12]` |
| `5` | Less than `10` | `less = [9, 5]` |
| `10` | Equal to `10` | `equal = [10]` |
| `14` | Greater than `10` | `greater = [12, 14]` |
| `3` | Less than `10` | `less = [9, 5, 3]` |
| `10` | Equal to `10` | `equal = [10, 10]` |

Combine the lists:

```python
less + equal + greater
# [9, 5, 3, 10, 10, 12, 14]
```

## 7. Complexity

- **Time Complexity:** `O(n)` — each element is processed once, and the list concatenation takes linear time.
- **Space Complexity:** `O(n)` — the lists store the elements and the returned array contains all `n` elements.

## 8. Pattern

**Array Traversal + Stable Partitioning**

Use this pattern when you need to separate array elements by a condition while preserving their relative order. The three-list approach is simple and clear, but it uses `O(n)` extra space.

Related problems:
- [Sort Colors — LeetCode 75](https://leetcode.com/problems/sort-colors/)
- [Move Zeroes — LeetCode 283](https://leetcode.com/problems/move-zeroes/)
