# 76. Minimum Window Substring

**LeetCode:** [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
**Difficulty:** Hard  
**Pattern:** Variable-Size Sliding Window + Frequency Hash Map

---

## 1. Question

Given two strings `s` and `t` of lengths `m` and `n`, return the **minimum window substring** of `s` such that every character in `t` (including duplicate characters) is included in the window. If no such substring exists, return `""`.

The test cases are generated so that the answer is unique.

## 2. Examples

### Example 1

**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`  
**Output:** `"BANC"`

**Explanation:** The minimum window substring `"BANC"` includes `'A'`, `'B'`, and `'C'` from `t`.

### Example 2

**Input:** `s = "a"`, `t = "a"`  
**Output:** `"a"`

**Explanation:** The entire string `s` is the minimum window.

### Example 3

**Input:** `s = "a"`, `t = "aa"`  
**Output:** `""`

**Explanation:** Both `'a'` characters from `t` must be included. Since `s` contains only one `'a'`, no valid window exists.

## 3. Approach

Use a **variable-size sliding window** with two frequency dictionaries.

- `need` stores the required frequency of every character in `t`.
- `window` stores the frequency of characters in the current window of `s`.
- `right` expands the window by adding characters.
- `left` shrinks a valid window to try to find a shorter answer.
- `formed` counts how many distinct required characters currently have their full required frequency in the window.
- `required` is the number of distinct characters in `t`.

The window is valid when `formed == required`. This frequency-based check correctly handles duplicate characters.

## 4. Algorithm

1. If either string is empty, return `""`.
2. Count the characters in `t` and store the frequencies in `need`.
3. Initialize `window = {}`, `left = 0`, `formed = 0`, and `required = len(need)`.
4. Initialize `min_length` to infinity and `start` to `0`.
5. Move `right` through every character in `s`:
   - Add the current character to `window`.
   - If it is required and its window frequency reaches the needed frequency, increment `formed`.
6. While `formed == required`:
   - Update the best window if the current window is shorter.
   - Remove the character at `left` from the window and move `left` one position forward.
   - If removing it makes a required character frequency too small, decrement `formed`.
7. After the loop, return `""` if no valid window was found. Otherwise, return the substring starting at `start` with length `min_length`.

## 5. Code

```python
class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0
        formed = 0
        required = len(need)

        min_length = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_length == float('inf'):
            return ""

        return s[start:start + min_length]
```

## 6. Dry Run

For `s = "ADOBECODEBANC"` and `t = "ABC"`:

| Current window | What happens |
|---|---|
| `ADOBEC` | Contains `A`, `B`, and `C`; save length `6`. |
| `DOBEC` | After removing `A`, the window is no longer valid. |
| `BANC` | Contains all required characters; save length `4`. |
| End | No shorter valid window is found, so return `"BANC"`. |

**Output:** `"BANC"`

## 7. Complexity

Let `m = len(s)` and `n = len(t)`.

- **Time Complexity:** `O(m + n)` average. Building `need` takes `O(n)`. Both sliding-window pointers move only forward through `s`, so the window operations take `O(m)` average time.
- **Space Complexity:** `O(k)`, where `k` is the number of distinct characters tracked in the dictionaries. With English letters, this is bounded by the character set size.

## 8. Pattern

**Variable-Size Sliding Window + Frequency Hash Map**

Use this pattern when searching for the shortest substring that satisfies character-frequency requirements.

**Remember:**
- Expand the right side until the window is valid.
- Shrink the left side while it remains valid.
- Count frequencies, not just whether a character exists.
- Keep the final `if min_length == float('inf')` and `return` statements **outside** the `for` loop.

## Constraints

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.
- Target time complexity: `O(m + n)`.
