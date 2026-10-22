# 567. Permutation in String

**LeetCode:** https://leetcode.com/problems/permutation-in-string/  
**Difficulty:** Medium  
**Pattern:** Sliding Window + Character Frequency

---

## 1. Question

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

A permutation contains the same characters with the same frequencies, but the characters may be in a different order.

## 2. Examples

### Example 1

**Input:** `s1 = "ab", s2 = "eidbaooo"`  
**Output:** `True`

**Explanation:** The substring `"ba"` is a permutation of `"ab"`.

### Example 2

**Input:** `s1 = "ab", s2 = "eidboaoo"`  
**Output:** `False`

**Explanation:** No substring of length `len(s1)` has the same character frequencies as `s1`.

## 3. Approach

Use a **fixed-size sliding window** of length `len(s1)` across `s2`.

- `count1` stores the frequency of every character in `s1`.
- `count2` stores the frequency of characters in the current window of `s2`.
- First, compare the first window.
- Then move the window one character at a time: add the new character and remove the character that leaves the window.
- If the two frequency dictionaries match, a permutation exists.

## 4. Algorithm

1. Set `k = len(s1)`.
2. If `k > len(s2)`, return `False`.
3. Create empty dictionaries `count1` and `count2`.
4. Count the frequency of every character in `s1` and store it in `count1`.
5. Count the first `k` characters of `s2` and store them in `count2`.
6. If `count1 == count2`, return `True`.
7. For each index `i` from `k` to the end of `s2`:
   - Add `s2[i]` to `count2`.
   - Decrease the count of the outgoing character `s2[i-k]`.
   - If its count becomes zero, remove it from `count2`.
   - If `count1 == count2`, return `True`.
8. If no matching window is found, return `False`.

## 5. Code

```python
class Solution:
    def checkInclusion(self, s1, s2):
        k = len(s1)

        if k > len(s2):
            return False

        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        for ch in s2[:k]:
            count2[ch] = count2.get(ch, 0) + 1

        if count1 == count2:
            return True

        for i in range(k, len(s2)):
            new_char = s2[i]
            old_char = s2[i - k]

            count2[new_char] = count2.get(new_char, 0) + 1

            count2[old_char] -= 1
            if count2[old_char] == 0:
                del count2[old_char]

            if count1 == count2:
                return True

        return False
```

## 6. Dry Run

For `s1 = "ab"` and `s2 = "eidbaooo"`:

- `k = 2`; `count1 = {'a': 1, 'b': 1}`.
- First window `"ei"`: `count2 = {'e': 1, 'i': 1}`. No match.
- Slide to `"id"`: add `'d'`, remove `'e'`. No match.
- Slide to `"db"`: add `'b'`, remove `'i'`. No match.
- Slide to `"ba"`: add `'a'`, remove `'d'`. Now `count2 = {'b': 1, 'a': 1}`.
- `count1 == count2`, so return `True`.

**Output:** `True`

## 7. Complexity

Let `n = len(s2)` and `k = len(s1)`.

- **Time Complexity:** `O(n * A)` average, where `A` is the number of distinct keys in the frequency dictionaries. Since the strings contain only lowercase English letters, `A <= 26`, so this is effectively `O(n)`.
- **Space Complexity:** `O(A)`, effectively `O(1)` for the fixed lowercase English alphabet.

## 8. Pattern

**Fixed-Size Sliding Window + Frequency Counting**

Use this pattern when checking whether any substring of a fixed length has the same character frequencies as a target string.

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.
