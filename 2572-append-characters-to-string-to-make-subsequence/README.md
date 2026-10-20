# 2486. Append Characters to String to Make Subsequence

[LeetCode Problem](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/) | **Difficulty:** Medium

## Problem Statement

You are given two strings `s` and `t` consisting of only lowercase English letters.

Return the **minimum number of characters that need to be appended to the end of `s`** so that `t` becomes a subsequence of `s`.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

## Examples

### Example 1

**Input:**
```python
s = "coaching"
t = "coding"
```

**Output:**
```python
4
```

**Explanation:** Append `"ding"` to the end of `s`. The resulting string is `"coachingding"`, and `"coding"` is now a subsequence.

### Example 2

**Input:**
```python
s = "abcde"
t = "a"
```

**Output:**
```python
0
```

**Explanation:** `"a"` is already a subsequence of `s`, so no characters need to be appended.

### Example 3

**Input:**
```python
s = "z"
t = "abcde"
```

**Output:**
```python
5
```

**Explanation:** None of the characters in `t` can be matched in order from `s`, so all five characters of `t` must be appended.

## Constraints

- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.

---

## 1. Question

Find the minimum number of characters that must be appended to the end of `s` so that `t` becomes a subsequence of the resulting string.

## 2. Example

**Input:**
```python
s = "coaching"
t = "coding"
```

**Output:** `4`

We can match `c` and `o` in `s`, but the remaining characters of `t` are `"ding"`. Append those four characters to the end of `s`.

## 3. Approach

Use two pointers:

- `i` points to the current character in `s`.
- `j` points to the current character in `t`.

Move through `s` from left to right. Whenever `s[i] == t[j]`, we have matched one character of `t`, so move `j` forward. Move `i` forward on every iteration.

When the scan ends, `j` tells us how many characters of `t` have been matched in order. The remaining `len(t) - j` characters must be appended.

## 4. Algorithm

1. Initialize `i = 0` and `j = 0`.
2. While `i < len(s)` and `j < len(t)`:
   - If `s[i] == t[j]`, increment `j`.
   - Increment `i`.
3. Return `len(t) - j`.

## 5. Code

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j
```

## 6. Dry Run

Input: `s = "coaching"`, `t = "coding"`

| `s[i]` | `t[j]` | Match? | `j` after step |
|---|---|---|---:|
| `c` | `c` | Yes | 1 |
| `o` | `o` | Yes | 2 |
| `a` | `d` | No | 2 |
| `c` | `d` | No | 2 |
| `h` | `d` | No | 2 |
| `i` | `d` | No | 2 |
| `n` | `d` | No | 2 |
| `g` | `d` | No | 2 |

We matched the first two characters of `t`, `"co"`. The remaining part is `"ding"`, which has `6 - 2 = 4` characters.

Output: `4`

## 7. Complexity

- **Time Complexity:** `O(n + m)` in the general bound, where `n = len(s)` and `m = len(t)`. Each pointer moves forward at most once. More precisely, the loop takes `O(min(n, position needed))` and is bounded by `O(n + m)`.
- **Space Complexity:** `O(1)` — only two pointers are used.

## 8. Pattern

**Two Pointers + Subsequence Matching**

Use this pattern when checking whether one string can be matched in order inside another string. The pointer on the target string moves only when a matching character is found.
