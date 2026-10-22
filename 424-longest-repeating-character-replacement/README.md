# 424. Longest Repeating Character Replacement

**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/  
**Difficulty:** Medium  
**Pattern:** Sliding Window + Hash Map

---

## 1. Question

You are given a string `s` and an integer `k`. You can change at most `k` characters in `s`. Return the length of the longest substring that can be made of the same character.

## 2. Examples

### Example 1

**Input:** `s = "ABAB", k = 2`  
**Output:** `4`

**Explanation:** Replace the two `'A'` characters with `'B'`, or the two `'B'` characters with `'A'`.

### Example 2

**Input:** `s = "AABABBA", k = 1`  
**Output:** `4`

**Explanation:** Replace one character in a suitable substring to make `"BBBB"`.

## 3. Approach

Use a **sliding window** to find the longest substring that can be made of one repeated character using at most `k` replacements.

- `left` marks the start of the current window.
- `right` expands the window one character at a time.
- `count` stores each character's frequency in the current window.
- `max_frequency` is the highest character frequency seen in the current window.
- Replacements needed = `window length - max_frequency`.
- If replacements needed exceed `k`, move `left` forward until the window is valid.
- Track the largest window length.

## 4. Algorithm

1. Create an empty dictionary `count`.
2. Initialize `left = 0`, `max_frequency = 0`, and `max_length = 0`.
3. Iterate `right` through every index of `s`.
4. Increase the frequency of `s[right]` in `count`.
5. Update `max_frequency`.
6. While `(right - left + 1) - max_frequency > k`:
   - Decrease the frequency of `s[left]`.
   - Move `left` one step forward.
7. Update `max_length` with `right - left + 1`.
8. Return `max_length`.

## 5. Code

```python
class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
```

## 6. Dry Run

For `s = "AABABBA"` and `k = 1`:

| Window | Highest frequency | Replacements needed | Action |
|---|---:|---:|---|
| `"A"` | 1 | 0 | Valid; max length = 1 |
| `"AA"` | 2 | 0 | Valid; max length = 2 |
| `"AAB"` | 2 | 1 | Valid; max length = 3 |
| `"AABA"` | 3 | 1 | Valid; max length = 4 |
| `"AABAB"` | 3 | 2 | Invalid; move `left` forward |
| Continue sliding | — | — | Longest length remains 4 |

**Output:** `4`

Note: `max_frequency` is intentionally not decreased when `left` moves. This standard optimization still returns the correct maximum length.

## 7. Complexity

- **Time Complexity:** `O(n)` — each index enters the window once, and `left` only moves forward.
- **Space Complexity:** `O(1)` — at most 26 uppercase English letters are stored.

## 8. Pattern

**Sliding Window + Frequency Counting**

Use this pattern when finding the longest substring/window that satisfies a condition involving character frequencies or a limited number of changes.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`
