# 1456. Maximum Number of Vowels in a Substring of Given Length

[LeetCode Problem](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)  
**Difficulty:** Medium  
**Pattern:** Fixed Size Sliding Window

---

## 1. Question

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length exactly `k`.

Vowels are `a`, `e`, `i`, `o`, and `u`.

## 2. Examples

**Example 1**

Input: `s = "abciiidef"`, `k = 3`  
Output: `3`  
Explanation: The substring `"iii"` contains 3 vowels.

**Example 2**

Input: `s = "aeiou"`, `k = 2`  
Output: `2`  
Explanation: Any substring of length 2 contains 2 vowels.

**Example 3**

Input: `s = "leetcode"`, `k = 3`  
Output: `2`  
Explanation: `"lee"`, `"eet"` and `"ode"` contain 2 vowels.

## 3. Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

## 4. Approach

Use **Fixed Size Sliding Window**.

Count the vowels in the first window of length `k`. Then slide the window one character at a time:
- Add the incoming character if it is a vowel.
- Remove the outgoing character if it is a vowel.
- Update the maximum vowel count.

This avoids recounting all `k` characters for every substring.

## 5. Algorithm

1. Store the vowels in `vowels = "aeiou"`.
2. Initialize `count = 0`.
3. Count vowels in the first `k` characters.
4. Set `max_vowels = count`.
5. Loop through the remaining characters, starting at index `k`.
6. Add the incoming character's vowel contribution.
7. Subtract the outgoing character's vowel contribution at index `right - k`.
8. Update `max_vowels`.
9. Return `max_vowels`.

## 6. Code

```python
class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_vowels = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1

            if s[right - k] in vowels:
                count -= 1

            max_vowels = max(max_vowels, count)

        return max_vowels
```

## 7. Dry Run

Input: `s = "abciiidef"`, `k = 3`

The first window is `"abc"`. It contains one vowel (`a`), so `count = 1` and `max_vowels = 1`.

| Window | Added | Removed | Vowel Count | Maximum |
|---|---|---|---:|---:|
| `abc` | — | — | 1 | 1 |
| `bci` | `i` | `a` | 1 | 1 |
| `cii` | `i` | `b` | 2 | 2 |
| `iii` | `i` | `c` | 3 | 3 |
| `iid` | `d` | `i` | 2 | 3 |
| `ide` | `e` | `i` | 2 | 3 |
| `def` | `f` | `d` | 1 | 3 |

Final answer: `3`.

## 8. Why This Works

Every substring of length `k` is considered as the window moves across the string. Between two consecutive windows, exactly one character enters and one character leaves. Updating the previous count using those two characters gives the correct vowel count for the new window. Tracking the maximum therefore gives the required answer.

## 9. Complexity

- **Time Complexity:** `O(n)` — the first window takes `O(k)` and the remaining characters are processed once.
- **Space Complexity:** `O(1)` — only a fixed number of variables are used.

## 10. Pattern

**Fixed Size Sliding Window**

Remember:
1. Calculate the first window.
2. Add the incoming element.
3. Remove the outgoing element.
4. Update the answer.
5. Continue until the end.

Use this pattern when a problem asks for a maximum, minimum, count, or sum in a subarray or substring of a fixed length `k`.
