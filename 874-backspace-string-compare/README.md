# 844. Backspace String Compare

[LeetCode Problem](https://leetcode.com/problems/backspace-string-compare/) | **Difficulty:** Easy

## Problem Statement

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

After backspacing an empty text, the text remains empty.

### Example 1

**Input:** `s = "ab#c", t = "ad#c"`  
**Output:** `true`  
**Explanation:** Both strings become `"ac"`.

### Example 2

**Input:** `s = "ab##", t = "c#d#"`  
**Output:** `true`  
**Explanation:** Both strings become `""`.

### Example 3

**Input:** `s = "a#c", t = "b"`  
**Output:** `false`  
**Explanation:** `s` becomes `"c"`, while `t` becomes `"b"`.

### Constraints

- `1 <= s.length, t.length <= 200`
- `s` and `t` contain only lowercase English letters and `'#'`.

**Follow-up:** Can you solve it in `O(n)` time and `O(1)` extra space?

---

## 1. Question

Check whether two strings are equal after applying all backspaces. Every `'#'` removes the closest character to its left, if one exists.

## 2. Example

```text
s = "ab#c"
t = "ad#c"

After backspaces:
s = "ac"
t = "ac"

Output: True
```

## 3. Approach

Use **two pointers from the end** of both strings. Moving backwards lets us skip characters that are erased by backspaces without building new strings.

For each string:
- If the current character is `'#'`, increase a skip counter and move left.
- If the skip counter is positive, the current character is erased: decrease the counter and move left.
- Otherwise, the current character is a visible character.

Compare the visible characters. If they differ, return `False`. If one string still has a visible character while the other does not, return `False`. If both pointers finish, return `True`.

## 4. Algorithm

1. Set `i` to the last index of `s` and `j` to the last index of `t`.
2. While either pointer is still inside its string:
   - Set `skip_s = 0` and `skip_t = 0`.
   - Move `i` left until it points to a visible character or goes below zero.
   - Move `j` left until it points to a visible character or goes below zero.
   - If both pointers point to characters and those characters differ, return `False`.
   - If only one pointer points to a character, return `False`.
   - Move both pointers one position left.
3. Return `True`.

## 5. Code

```python
class Solution:
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            skip_s = 0
            skip_t = 0

            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True
```

## 6. Dry Run

For `s = "ab#c"` and `t = "ad#c"`:

| Step | Visible character in `s` | Visible character in `t` | Result |
|---|---|---|---|
| 1 | `c` | `c` | Match |
| 2 | `b` is skipped by `#` | `d` is skipped by `#` | Continue |
| 3 | `a` | `a` | Match |
| 4 | No characters left | No characters left | Return `True` |

Both processed strings are `"ac"`, so the answer is `True`.

## 7. Complexity

- **Time Complexity:** `O(n + m)`, where `n` and `m` are the lengths of `s` and `t`. Each pointer only moves left through its string.
- **Auxiliary Space Complexity:** `O(1)`, because only pointers and skip counters are used; no extra strings or stacks are created.

## 8. Pattern

**Two Pointers — Traverse from the End / Skip Counter**

Use this pattern when backspaces or deletions affect characters to the left. Processing from the end makes it possible to find each surviving character using constant extra space.
