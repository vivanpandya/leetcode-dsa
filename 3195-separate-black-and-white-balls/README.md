# 2938. Separate Black and White Balls

[LeetCode Problem](https://leetcode.com/problems/separate-black-and-white-balls/) | **Difficulty:** Medium

## Problem Statement

There are `n` balls on a table, each ball has a color black or white.

You are given a **0-indexed** binary string `s` of length `n`, where `1` and `0` represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the **minimum** number of steps to group all the black balls to the right and all the white balls to the left.

## Examples

### Example 1

**Input:**
```python
s = "101"
```

**Output:**
```python
1
```

**Explanation:** Swap the first two characters: `"101" -> "011"`. Now all white balls are on the left and all black balls are on the right.

### Example 2

**Input:**
```python
s = "100"
```

**Output:**
```python
2
```

**Explanation:** Swap adjacent balls twice: `"100" -> "010" -> "001"`.

### Example 3

**Input:**
```python
s = "0111"
```

**Output:**
```python
0
```

**Explanation:** All black balls are already grouped to the right.

## Constraints

- `1 <= n == s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

---

## 1. Question

Given a binary string where `0` represents a white ball and `1` represents a black ball, find the minimum number of adjacent swaps needed to place all `0`s before all `1`s.

## 2. Example

**Input:** `s = "100"`

We need to move the two white balls to the left of the black ball.

**Output:** `2`

The swaps are:

```text
100 -> 010 -> 001
```

## 3. Approach

Use a greedy counting approach.

Whenever we see a black ball (`'1'`), count how many white balls (`'0'`) appear after it. Each such white ball must cross that black ball in order to reach the left side, requiring one adjacent swap.

A simpler equivalent way is to scan from left to right and count black balls. Whenever a white ball appears, it must move left across all black balls already seen. Add the number of black balls seen to the answer.

## 4. Algorithm

1. Initialize `black = 0` and `steps = 0`.
2. Traverse each character in `s`.
3. If the character is `'1'`, increase `black` by `1`.
4. If the character is `'0'`, add `black` to `steps`, because this white ball must cross every black ball that appeared before it.
5. Return `steps`.

## 5. Code

```python
class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        steps = 0

        for ball in s:
            if ball == '1':
                black += 1
            else:
                steps += black

        return steps
```

## 6. Dry Run

Input: `s = "101"`

| Character | Black balls seen (`black`) | Steps added | Total steps |
|---|---:|---:|---:|
| `'1'` | 1 | 0 | 0 |
| `'0'` | 1 | 1 | 1 |
| `'1'` | 2 | 0 | 1 |

The white ball in the middle must cross the one black ball before it. Therefore, the minimum number of swaps is `1`.

Output: `1`

## 7. Complexity

- **Time Complexity:** `O(n)` — the string is traversed once.
- **Space Complexity:** `O(1)` — only two integer variables are used.

## 8. Pattern

**Greedy + Counting / Inversion Counting**

Count how many black balls appear before each white ball. Each such black-white pair is out of the desired order and requires one adjacent swap. This gives the minimum number of swaps in one pass without modifying the string.
