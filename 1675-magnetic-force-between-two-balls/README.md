# 1552. Magnetic Force Between Two Balls

[LeetCode Problem](https://leetcode.com/problems/magnetic-force-between-two-balls/)  
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Sorting
- Binary Search
- Greedy

---

## 1. Problem Statement

You are given an integer array `position`, where `position[i]` represents the position of the `i`th basket. You are also given an integer `m`, representing the number of balls.

Place all `m` balls into different baskets such that the **minimum distance between any two balls is as large as possible**.

The magnetic force between two balls placed at positions `x` and `y` is:

```text
|x - y|
```

Return the maximum possible value of the minimum magnetic force.

### Example 1

![Magnetic Force Example 1](https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg)

**Input:**
```python
position = [1, 2, 3, 4, 7]
m = 3
```

**Output:**
```python
3
```

**Explanation:**

Place the three balls at positions `1`, `4`, and `7`.

The distances between the pairs of balls are:

```text
4 - 1 = 3
7 - 4 = 3
7 - 1 = 6
```

The minimum distance is `3`, and it is the maximum possible minimum distance.

### Example 2

**Input:**
```python
position = [5, 4, 3, 2, 1, 1000000000]
m = 2
```

**Output:**
```python
999999999
```

**Explanation:**

Place the two balls in baskets at positions `1` and `1000000000`.

```text
1000000000 - 1 = 999999999
```

### Constraints

- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are distinct.
- `2 <= m <= position.length`

---

## 2. Approach: Binary Search on Answer + Greedy

We need to **maximize the minimum distance** between any two placed balls.

Instead of trying every possible placement, we binary search on the answer: the minimum distance we want to maintain between balls.

### Step 1: Sort the basket positions

```python
position.sort()
```

Sorting lets us place balls from left to right and greedily choose the earliest available basket that satisfies the required distance.

### Step 2: Set the binary search range

The smallest possible distance is `1`, because all basket positions are distinct integers.

The largest possible distance is the distance between the first and last baskets:

```python
left = 1
right = position[-1] - position[0]
```

### Step 3: Check whether a distance is possible

For a candidate minimum distance `mid`:

1. Place the first ball in the first basket.
2. Move through the remaining baskets from left to right.
3. Place a ball whenever its distance from the last placed ball is at least `mid`.
4. Count the balls placed.

The greedy check is:

```python
if position[i] - last_position >= mid:
    count += 1
    last_position = position[i]
```

If we can place at least `m` balls, the candidate distance is possible.

- If it is possible, try a larger distance.
- If it is not possible, try a smaller distance.

### Why greedy works

For a fixed minimum distance, placing each next ball in the earliest basket that is far enough leaves as much room as possible for the remaining balls. Therefore, if this greedy process cannot place `m` balls, no other placement can do so for that same distance.

---

## 3. Algorithm

1. Sort `position` in ascending order.
2. Set `left = 1`.
3. Set `right = position[-1] - position[0]`.
4. Initialize `ans = 0`.
5. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. Place the first ball at `position[0]`.
   3. Initialize `count = 1` and `last_position = position[0]`.
   4. Traverse the remaining basket positions:
      - If `position[i] - last_position >= mid`, place a ball there.
      - Increment `count` and update `last_position`.
   5. If `count >= m`:
      - The distance is possible.
      - Save `mid` in `ans`.
      - Search for a larger distance using `left = mid + 1`.
   6. Otherwise:
      - The distance is too large.
      - Search smaller distances using `right = mid - 1`.
6. Return `ans`.

---

## 4. Python Code

```python
class Solution:
    def maxDistance(self, position, m):
        position.sort()

        left = 1
        right = position[-1] - position[0]

        ans = 0

        while left <= right:
            mid = (left + right) // 2

            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]

            if count >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
```

---

## 5. Dry Run

**Input:**
```python
position = [1, 2, 3, 4, 7]
m = 3
```

Sort the positions:

```python
position = [1, 2, 3, 4, 7]
```

Initial values:

```text
left = 1
right = 7 - 1 = 6
ans = 0
```

### Iteration 1

```text
mid = (1 + 6) // 2 = 3
```

Try to place balls with a minimum distance of `3`.

| Basket position | Distance from last ball | Action |
|---:|---:|---|
| 1 | — | Place first ball |
| 2 | 1 | Skip |
| 3 | 2 | Skip |
| 4 | 3 | Place second ball |
| 7 | 3 | Place third ball |

We placed `3` balls.

```text
count = 3
count >= m
```

Distance `3` is possible.

```text
ans = 3
left = mid + 1 = 4
```

### Iteration 2

```text
mid = (4 + 6) // 2 = 5
```

Try to place balls with a minimum distance of `5`.

| Basket position | Distance from last ball | Action |
|---:|---:|---|
| 1 | — | Place first ball |
| 2 | 1 | Skip |
| 3 | 2 | Skip |
| 4 | 3 | Skip |
| 7 | 6 | Place second ball |

We placed only `2` balls.

```text
count = 2
count < m
```

Distance `5` is not possible.

```text
right = mid - 1 = 4
```

### Iteration 3

```text
mid = (4 + 4) // 2 = 4
```

Try to place balls with a minimum distance of `4`.

| Basket position | Distance from last ball | Action |
|---:|---:|---|
| 1 | — | Place first ball |
| 2 | 1 | Skip |
| 3 | 2 | Skip |
| 4 | 3 | Skip |
| 7 | 6 | Place second ball |

We placed only `2` balls.

```text
count = 2
count < m
```

Distance `4` is not possible.

```text
right = mid - 1 = 3
```

Now:

```text
left = 4
right = 3
```

The loop ends.

**Final output:**
```python
3
```

### Dry Run Summary

| Iteration | `left` | `right` | `mid` | Balls placed | Decision |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 6 | 3 | 3 | Possible; search higher |
| 2 | 4 | 6 | 5 | 2 | Not possible; search lower |
| 3 | 4 | 4 | 4 | 2 | Not possible; search lower |

The largest feasible minimum distance is `3`.

---

## 6. Why This Works

For a chosen distance `d`, the greedy algorithm places the first ball in the leftmost basket and every next ball in the earliest basket at least `d` units away from the previous ball.

This is an optimal way to test whether `d` is feasible: choosing an earlier valid basket never leaves less room for the remaining balls than choosing a later one.

The feasibility condition is monotonic:

- If a distance `d` is possible, every smaller distance is also possible.
- If a distance `d` is impossible, every larger distance is also impossible.

This monotonic property allows binary search on the answer. We keep the largest feasible distance and eventually return it.

---

## 7. Complexity Analysis

Let:
- `n` = number of baskets.
- `D` = `position[-1] - position[0]`, the maximum possible distance.

| Operation | Time Complexity |
|---|---|
| Sorting positions | `O(n log n)` |
| One greedy feasibility check | `O(n)` |
| Binary search over distances | `O(log D)` iterations |
| All feasibility checks | `O(n log D)` |

**Total Time Complexity:**

```text
O(n log n + n log D)
```

**Auxiliary Space Complexity:**

```text
O(1)
```

The algorithm uses a constant number of extra variables, excluding temporary memory used internally by Python's sorting implementation. Sorting is performed in place.

---

## 8. Pattern and Related Problems

**Pattern: Binary Search on Answer + Greedy Feasibility Check**

Recognize this pattern when:
- The problem asks to maximize the minimum distance.
- Items must be placed at selected positions.
- You can check whether a proposed distance is possible.
- Feasibility is monotonic: if a distance works, smaller distances also work.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Koko Eating Bananas | 875 | Binary Search on Answer |
| Capacity To Ship Packages Within D Days | 1011 | Binary Search on Answer + Greedy |
| Split Array Largest Sum | 410 | Binary Search on Answer + Greedy |
| Magnetic Force Between Two Balls | 1552 | Binary Search on Answer + Greedy |

### Important Lines to Remember

Check whether we can place the next ball:

```python
if position[i] - last_position >= mid:
    count += 1
    last_position = position[i]
```

If the candidate distance is possible, try a larger one:

```python
if count >= m:
    ans = mid
    left = mid + 1
```

Otherwise, reduce the candidate distance:

```python
else:
    right = mid - 1
```

---

## Image Source

The example illustration is embedded from the official LeetCode problem asset:

[Open the original illustration](https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg)
