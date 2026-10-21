# 3. Longest Substring Without Repeating Characters

[LeetCode Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Statement

Given a string `s`, find the length of the **longest substring** without duplicate characters.

A substring is a contiguous part of a string.

### Example 1

**Input:**
```text
s = "abcabcbb"
```

**Output:**
```text
3
```

**Explanation:** The answer is `"abc"`, with a length of `3`. `"bca"` and `"cab"` are also valid answers.

### Example 2

**Input:**
```text
s = "bbbbb"
```

**Output:**
```text
1
```

**Explanation:** The longest substring without repeating characters is `"b"`.

### Example 3

**Input:**
```text
s = "pwwkew"
```

**Output:**
```text
3
```

**Explanation:** The answer can be `"wke"`, with a length of `3`. Notice that `"pwke"` is a subsequence, not a substring.

### Constraints

- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols, and spaces.

---

## 1. Approach

Use a **sliding window** with two pointers and a set.

- `left` marks the beginning of the current substring.
- `right` moves through the string.
- `seen` stores the characters currently inside the window.
- If `s[right]` is already in `seen`, remove characters from the left until that duplicate is removed.
- Update the maximum window length after adding each character.

This works for all characters, including letters, digits, symbols, and spaces.

## 2. Algorithm

1. Initialize `left = 0`, `seen = set()`, and `max_length = 0`.
2. Loop through the string using `right`.
3. While `s[right]` is already in `seen`:
   - Remove `s[left]` from `seen`.
   - Move `left` one step to the right.
4. Add `s[right]` to `seen`.
5. Update `max_length` using `right - left + 1`.
6. Return `max_length`.

## 3. Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```

## 4. Dry Run

Input: `s = "abcabcbb"`

| `right` | Character | Current window after processing | `max_length` |
|---:|:---:|---|---:|
| 0 | `a` | `a` | 1 |
| 1 | `b` | `ab` | 2 |
| 2 | `c` | `abc` | 3 |
| 3 | `a` | `bca` | 3 |
| 4 | `b` | `cab` | 3 |
| 5 | `c` | `abc` | 3 |
| 6 | `b` | `cb` | 3 |
| 7 | `b` | `b` | 3 |

**Answer: `3`**

## 5. Why This Works

The window always contains unique characters. When a repeated character appears, the left pointer moves forward and removes characters until the window no longer contains that duplicate. Every time the window is valid, its length is checked against `max_length`. Therefore, the largest valid window length is returned.

## 6. Time Complexity

**O(n)** average time — each character is added to and removed from the set at most once.

## 7. Space Complexity

**O(min(n, charset))** — the set stores only the distinct characters in the current window. In the general case, this is O(n).

## 8. Pattern

**Sliding Window + Hash Set**

Use this pattern to find a longest or shortest contiguous substring where a condition must remain true, such as having no repeated characters.
