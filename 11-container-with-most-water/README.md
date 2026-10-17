# LeetCode 11: Container With Most Water

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/container-with-most-water/)
[![LeetCode](https://img.shields.io/badge/LeetCode-11-blue)](https://leetcode.com/problems/container-with-most-water/)

**Problem link:** https://leetcode.com/problems/container-with-most-water/

---

## 1. Question

You are given an integer array `height` of length `n`. Each element represents the height of a vertical line, and the distance between adjacent lines is `1`.

Choose two lines that, together with the x-axis, form a container that can hold the maximum amount of water.

Return the maximum amount of water the container can store. The container cannot be tilted.

### Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## 2. Examples

### Example 1

```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
```

The lines at indices `1` and `8` have heights `8` and `7`.

- Width = `8 - 1 = 7`
- Water height = `min(8, 7) = 7`
- Area = `7 * 7 = 49`

### Example 2

```python
height = [1, 1]
# Output: 1
```

Width = `1`, water height = `1`, so area = `1`.

## 3. Approach

Use the **Two Pointers** technique.

- Set `left` to the first index and `right` to the last index.
- Calculate the area formed by these two lines.
- Update the maximum area whenever a larger area is found.
- Move the pointer at the **shorter line** inward, because the shorter line limits the water height.
- Continue until the pointers meet.

The area is:

`area = min(height[left], height[right]) * (right - left)`

Why move the shorter line? Moving the taller line cannot increase the limiting height while the width decreases. Moving the shorter line is the only move that may find a taller boundary and improve the area.

## 4. Algorithm

1. Initialize `left = 0`, `right = len(height) - 1`, and `max_area = 0`.
2. While `left < right`:
   - Calculate `width = right - left`.
   - Calculate `current_area = min(height[left], height[right]) * width`.
   - Update `max_area = max(max_area, current_area)`.
   - If `height[left] < height[right]`, increment `left`.
   - Otherwise, decrement `right`.
3. Return `max_area`.

## 5. Code

```python
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

## 6. Dry Run

Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

| Left index | Right index | Left height | Right height | Width | Area | Maximum area |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1 | 7 | 8 | 8 | 8 |
| 1 | 8 | 8 | 7 | 7 | 49 | 49 |
| 1 | 7 | 8 | 3 | 6 | 18 | 49 |
| 1 | 6 | 8 | 8 | 5 | 40 | 49 |
| 2 | 6 | 6 | 8 | 4 | 24 | 49 |
| 3 | 6 | 2 | 8 | 3 | 6 | 49 |
| 4 | 6 | 5 | 8 | 2 | 10 | 49 |
| 5 | 6 | 4 | 8 | 1 | 4 | 49 |

The maximum area found is `49`.

**Output:** `49`

## 7. Complexity

- **Time Complexity:** `O(n)` — each pointer moves inward, so each position is visited at most once.
- **Auxiliary Space Complexity:** `O(1)` — only a few variables are used.

## 8. Pattern

**Two Pointers — Greedy**

This pattern is useful when two boundaries define an area and moving the shorter boundary is the key to finding a better answer without checking every pair.

## Image

The illustration below shows the container for Example 1. The maximum water is formed by the lines at indices `1` and `8`.

![Container With Most Water — Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
