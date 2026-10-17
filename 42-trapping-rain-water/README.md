# LeetCode 42: Trapping Rain Water

[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/trapping-rain-water/)
[![LeetCode](https://img.shields.io/badge/LeetCode-42-blue)](https://leetcode.com/problems/trapping-rain-water/)

**Problem link:** https://leetcode.com/problems/trapping-rain-water/

---

## 1. Question

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, calculate how much water can be trapped between the bars after it rains.

### Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## 2. Examples

### Example 1

```python
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
```

### Example 2

```python
height = [4, 2, 0, 3, 2, 5]
# Output: 9
```

## 3. Approach

Use **Two Pointers** with two running maximums: `left_max` and `right_max`.

- Start `left` at the first index and `right` at the last index.
- The shorter current boundary determines which side can be processed safely.
- If `height[left] <= height[right]`, update `left_max`. Water above the left bar is `left_max - height[left]`, then move `left` forward.
- Otherwise, update `right_max`. Water above the right bar is `right_max - height[right]`, then move `right` backward.
- Add each position's trapped water to `water`.

This avoids creating separate left-maximum and right-maximum arrays.

## 4. Algorithm

1. Initialize `left = 0` and `right = len(height) - 1`.
2. Initialize `left_max = 0`, `right_max = 0`, and `water = 0`.
3. While `left < right`:
   - If `height[left] <= height[right]`:
     - Update `left_max = max(left_max, height[left])`.
     - Add `left_max - height[left]` to `water`.
     - Increment `left`.
   - Otherwise:
     - Update `right_max = max(right_max, height[right])`.
     - Add `right_max - height[right]` to `water`.
     - Decrement `right`.
4. Return `water`.

## 5. Code

```python
class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water
```

## 6. Dry Run

Input: `height = [4, 2, 0, 3, 2, 5]`

| Left index | Right index | Side processed | Running maximum | Water added | Total water |
|---:|---:|---|---:|---:|---:|
| 0 | 5 | Left (height 4) | `left_max = 4` | 0 | 0 |
| 1 | 5 | Left (height 2) | `left_max = 4` | 2 | 2 |
| 2 | 5 | Left (height 0) | `left_max = 4` | 4 | 6 |
| 3 | 5 | Left (height 3) | `left_max = 4` | 1 | 7 |
| 4 | 5 | Left (height 2) | `left_max = 4` | 2 | 9 |

The total trapped water is `2 + 4 + 1 + 2 = 9`.

**Output:** `9`

## 7. Complexity

- **Time Complexity:** `O(n)` — each pointer moves inward, processing each position at most once.
- **Auxiliary Space Complexity:** `O(1)` — only a fixed number of variables are used.

## 8. Pattern

**Two Pointers + Running Maximums**

Use this pattern when calculating trapped water from boundaries while avoiding extra arrays.

## Image

The image below illustrates the elevation map and trapped rainwater from Example 1.

![Trapping Rain Water — Example 1](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
