# 392. Is Subsequence

[LeetCode Problem](https://leetcode.com/problems/is-subsequence/)  
**Difficulty:** Easy  
**Pattern:** Two Pointers

---

## Original Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, `"ace"` is a subsequence of `"abcde"`, while `"aec"` is not.

### Examples

**Example 1**

- Input: `s = "abc"`, `t = "ahbgdc"`
- Output: `true`

**Example 2**

- Input: `s = "axc"`, `t = "ahbgdc"`
- Output: `false`

### Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

**Follow-up:** If there are many incoming strings `s` to check against the same `t`, how could the solution be improved?

---

## 1. Question

Check whether all characters of `s` appear in `t` in the same order. The characters do not need to be next to each other.

## 2. Example

Input:
```python
s = "abc"
t = "ahbgdc"
```

Output:
```python
True
```

Explanation: Find `a`, then `b` after it, then `c` after `b` in `t`.

## 3. Approach

Use two pointers:

- `i` points to the current character in `s`.
- `j` scans through `t`.
- When `s[i] == t[j]`, move `i` forward because that character has been matched.
- Always move `j` forward.
- If `i` reaches the end of `s`, every character was matched in order.

This also correctly returns `True` when `s` is empty.

## 4. Algorithm

1. Set `i = 0` and `j = 0`.
2. While `i < len(s)` and `j < len(t)`:
   - If `s[i] == t[j]`, increment `i`.
   - Increment `j`.
3. Return `i == len(s)`.

## 5. Code

```python
class Solution:
    def isSubsequence(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

## 6. Dry Run

For `s = "abc"` and `t = "ahbgdc"`:

| `j` | `t[j]` | `s[i]` before check | Action |
|---:|:---:|:---:|---|
| 0 | `a` | `a` | Match; `i = 1` |
| 1 | `h` | `b` | No match |
| 2 | `b` | `b` | Match; `i = 2` |
| 3 | `g` | `c` | No match |
| 4 | `d` | `c` | No match |
| 5 | `c` | `c` | Match; `i = 3` |

Now `i == len(s)`, so return `True`.

For `s = "axc"` and `t = "ahbgdc"`, `a` matches but `x` is never found after it. The loop ends with `i < len(s)`, so return `False`.

## 7. Complexity

- **Time:** `O(len(t))` — each character in `t` is scanned at most once.
- **Auxiliary space:** `O(1)` — only two pointers are used.

## 8. Pattern

**Two Pointers / Subsequence Check**

Use this pattern when checking whether one sequence appears inside another in the same relative order, without requiring adjacent characters.

### Follow-up: Many queries for the same `t`

If many different strings `s` must be checked against the same fixed `t`, preprocess `t` by storing the positions where each character occurs. For each character in a query `s`, use binary search to find the next occurrence strictly after the previous match. This makes each query faster when `t` is reused many times.

- **Preprocessing:** `O(len(t))` to store character positions.
- **Each query:** approximately `O(len(s) log len(t))` using binary search.
