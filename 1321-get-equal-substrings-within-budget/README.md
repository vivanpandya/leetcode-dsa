# 1208. Get Equal Substrings Within Budget

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/get-equal-substrings-within-budget/

---

## Problem Statement

You are given two strings `s` and `t` of the same length and an integer `maxCost`.

Changing the `i`th character of `s` to the `i`th character of `t` costs `abs(ord(s[i]) - ord(t[i]))`.

Return the maximum length of a substring of `s` that can be changed to the corresponding substring of `t` with a total cost less than or equal to `maxCost`. If no non-empty substring can be changed within the budget, return `0`.

## Examples

### Example 1

```text
Input:  s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" can be changed to "bcd" with cost 1 + 1 + 1 = 3.
```

### Example 2

```text
Input:  s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character costs 2 to change, so only one character fits the budget.
```

### Example 3

```text
Input:  s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: Only the first character is already equal, so its cost is 0.
```

## Constraints

- `1 <= s.length <= 10^5`
- `t.length == s.length`
- `0 <= maxCost <= 10^6`
- `s` and `t` consist of lowercase English letters.

---

## Approach: Sliding Window

We need the longest continuous section where the total cost of changing characters in `s` to the matching characters in `t` does not exceed `maxCost`.

1. Calculate each character's conversion cost using `abs(ord(s[i]) - ord(t[i]))`.
2. Expand the window by moving `right` and add the new cost to `total`.
3. If `total` becomes greater than `maxCost`, shrink the window from the left:
   - Subtract the cost at `left`.
   - Move `left` one position forward.
4. Once the window is valid, update the maximum window length.
5. Return the maximum length.

All costs are non-negative. Therefore, when the window exceeds the budget, removing characters from the left can only keep or reduce its total cost.

## Algorithm

1. Initialize `left = 0`, `total = 0`, and `max_length = 0`.
2. Loop `right` from `0` to `len(s) - 1`.
3. Calculate the current conversion cost:
   `cost = abs(ord(s[right]) - ord(t[right]))`.
4. Add the cost to `total`.
5. While `total > maxCost`:
   - Subtract the conversion cost at index `left`.
   - Increment `left`.
6. Calculate the current window length using `right - left + 1`.
7. Update `max_length`.
8. Return `max_length`.

## Python Code

```python
class Solution:
    def equalSubstring(self, s, t, maxCost):
        left = 0
        total = 0
        max_length = 0

        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            total += cost

            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

## Dry Run

Input:

```text
s = "abcd"
t = "bcdf"
maxCost = 3
```

Character conversion costs:

| Index | `s[i]` | `t[i]` | Cost |
|---:|:---:|:---:|---:|
| 0 | a | b | 1 |
| 1 | b | c | 1 |
| 2 | c | d | 1 |
| 3 | d | f | 2 |

Window movement:

| `right` | Added cost | `total` | Window before shrinking | Action |
|---:|---:|---:|:---:|---|
| 0 | 1 | 1 | `a` | Valid; maximum = 1 |
| 1 | 1 | 2 | `ab` | Valid; maximum = 2 |
| 2 | 1 | 3 | `abc` | Valid; maximum = 3 |
| 3 | 2 | 5 | `abcd` | Over budget; shrink from left |

At `right = 3`:
- Remove the cost at index 0: `total = 5 - 1 = 4`.
- The total is still greater than 3, so remove the cost at index 1: `total = 4 - 1 = 3`.
- Move `left` to index 2. The valid window is now `cd`, with length 2.

The maximum length found is **3**.

Output:

```text
3
```

## Why This Works

The window always represents a continuous substring. `total` stores the exact cost of changing that substring of `s` into the matching substring of `t`.

Whenever the cost exceeds `maxCost`, we move `left` forward until the window is valid again. Since all conversion costs are non-negative, shrinking the window cannot increase its total cost.

We update the answer only after the window is valid. Thus, the algorithm finds the maximum length of a valid substring.

## Complexity Analysis

Let `n` be the length of the strings.

- **Time Complexity: `O(n)`** — The `right` pointer visits each character once. The `left` pointer also moves forward at most `n` times.
- **Space Complexity: `O(1)`** — Only a few variables are used; no additional data structure grows with the input size.

## Pattern

**Variable-Size Sliding Window**

Use this pattern when:
- You need the longest or shortest contiguous substring/subarray.
- A running total or cost must stay within a given limit.
- You can expand the window and shrink it when the condition becomes invalid.

Key formula:

```python
window_length = right - left + 1
```
