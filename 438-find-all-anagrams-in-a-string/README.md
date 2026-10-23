# 438. Find All Anagrams in a String

**LeetCode:** https://leetcode.com/problems/find-all-anagrams-in-a-string/  
**Difficulty:** Medium  
**Pattern:** Sliding Window + Character Frequency

---

## 1. Question

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

## 2. Examples

### Example 1

**Input:** `s = "cbaebabacd"`, `p = "abc"`  
**Output:** `[0, 6]`

**Explanation:**
- The substring starting at index `0` is `"cba"`, an anagram of `"abc"`.
- The substring starting at index `6` is `"bac"`, an anagram of `"abc"`.

### Example 2

**Input:** `s = "abab"`, `p = "ab"`  
**Output:** `[0, 1, 2]`

**Explanation:** The substrings `"ab"`, `"ba"`, and `"ab"` are all anagrams of `"ab"`.

## 3. Approach

Use a **fixed-size sliding window** of length `len(p)`.

1. Count the frequency of each character in `p`.
2. Count the frequency of the first window in `s`.
3. Compare the two frequency dictionaries. If they match, save the window's start index.
4. Slide the window one character at a time:
   - Add the new character entering the window.
   - Decrease the count of the character leaving the window.
   - Remove a character from the dictionary if its count becomes zero.
5. Whenever the dictionaries match, add the current window's start index to the answer.

## 4. Algorithm

1. If `len(p) > len(s)`, return an empty list.
2. Create dictionaries `count_p` and `window`.
3. Count the characters in `p` and the first `len(p)` characters of `s`.
4. If `count_p == window`, add index `0` to the result.
5. For each `right` index from `len(p)` to `len(s) - 1`:
   - Add `s[right]` to `window`.
   - Remove one occurrence of `s[right - len(p)]`.
   - Delete that character's key if its count becomes zero.
   - If `count_p == window`, append `right - len(p) + 1`.
6. Return the result.

## 5. Code

```python
class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        count_p = {}
        window = {}

        for ch in p:
            count_p[ch] = count_p.get(ch, 0) + 1

        for ch in s[:len(p)]:
            window[ch] = window.get(ch, 0) + 1

        result = []

        if count_p == window:
            result.append(0)

        for right in range(len(p), len(s)):
            new_char = s[right]
            old_char = s[right - len(p)]

            window[new_char] = window.get(new_char, 0) + 1

            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]

            if count_p == window:
                result.append(right - len(p) + 1)

        return result
```

## 6. Dry Run

For `s = "cbaebabacd"` and `p = "abc"`:

- Window `"cba"` at index `0`: its character frequencies match `"abc"` → add `0`.
- Slide the window through `"bae"`, `"aeb"`, `"eba"`, `"bab"`, `"aba"`.
- Window `"bac"` at index `6`: its character frequencies match `"abc"` → add `6`.
- No other windows match.

**Output:** `[0, 6]`

## 7. Complexity

Let `n = len(s)` and `m = len(p)`.

- **Time Complexity:** `O(n)` average, because each character enters and leaves the window at most once. Dictionary comparisons take constant time under the fixed lowercase-English alphabet constraint.
- **Space Complexity:** `O(1)` auxiliary space, because each dictionary can contain at most 26 lowercase English letters.

## 8. Pattern

**Fixed-Size Sliding Window + Hash Map**

Use this pattern when you need to find all substrings of a fixed length that match a character-frequency requirement, such as anagrams or permutations.

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.
