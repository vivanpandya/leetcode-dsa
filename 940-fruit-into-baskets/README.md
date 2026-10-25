# 904. Fruit Into Baskets

**LeetCode:** [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)  
**Difficulty:** Medium  
**Pattern:** Variable-Size Sliding Window + Hash Map

---

## 1. Question

You are given an integer array `fruits`, where `fruits[i]` represents the type of fruit produced by the `i`th tree.

You have two baskets, and each basket can hold only one type of fruit. Starting from any tree, move to the right and collect exactly one fruit from every tree until you reach a tree whose fruit cannot fit in your baskets.

Return the maximum number of fruits you can collect.

## 2. Examples

### Example 1

**Input:** `fruits = [1,2,1]`  
**Output:** `3`

All three trees contain at most two fruit types, so we can collect all three.

### Example 2

**Input:** `fruits = [0,1,2,2]`  
**Output:** `3`

The longest valid section is `[1,2,2]`, which contains only two fruit types.

### Example 3

**Input:** `fruits = [1,2,3,2,2]`  
**Output:** `4`

The longest valid section is `[2,3,2,2]`, which contains only two fruit types.

## 3. Approach

Use a **variable-size sliding window** and a dictionary to count fruit types.

- `left` is the start of the current window.
- `right` moves through the array and adds each fruit to the window.
- `count` stores how many times each fruit type appears in the current window.
- If the window contains more than two different fruit types, shrink it from the left until only two types remain.
- Update the maximum window length after each step.

## 4. Algorithm

1. Initialize `left = 0`, an empty dictionary `count`, and `max_fruits = 0`.
2. For each `right` index:
   - Add `fruits[right]` to the dictionary count.
   - While the dictionary contains more than two fruit types:
     - Decrease the count of `fruits[left]`.
     - If its count becomes zero, remove that type from the dictionary.
     - Move `left` one step to the right.
   - Update `max_fruits` with `right - left + 1`.
3. Return `max_fruits`.

## 5. Code

```python
class Solution:
    def totalFruit(self, fruits):
        count = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
```

## 6. Dry Run

For `fruits = [1,2,3,2,2]`:

| Right | Fruit added | Window after adjustment | Fruit types | Window length | Maximum |
|---:|---:|---|---:|---:|---:|
| 0 | 1 | `[1]` | 1 | 1 | 1 |
| 1 | 2 | `[1,2]` | 2 | 2 | 2 |
| 2 | 3 | `[2,3]` | 2 | 2 | 2 |
| 3 | 2 | `[2,3,2]` | 2 | 3 | 3 |
| 4 | 2 | `[2,3,2,2]` | 2 | 4 | 4 |

When fruit type `3` is added at index `2`, the window temporarily contains three types: `1`, `2`, and `3`. Move `left` forward and remove type `1` from the window. The valid window becomes `[2,3]`.

**Final output:** `4`

## 7. Complexity

Let `n = len(fruits)`.

- **Time Complexity:** `O(n)` — each index enters and leaves the window at most once.
- **Space Complexity:** `O(1)` — the dictionary holds at most three fruit types temporarily, and at most two after shrinking.

## 8. Pattern

**Sliding Window — Longest Subarray With At Most Two Distinct Values**

This is the same general pattern as problems that ask for the longest substring or subarray with at most `k` distinct values.

Remember:
- Expand the window by moving `right`.
- If there are too many distinct types, move `left` until the window is valid.
- Track the largest valid window using `right - left + 1`.

## Constraints

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`
