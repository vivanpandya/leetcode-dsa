# 125. Valid Palindrome

- **LeetCode:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **Difficulty:** Easy
- **Topics:** Two Pointers, String

## 1. Question

A phrase is a palindrome if, after converting uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `True` if it is a palindrome; otherwise, return `False`.

**Alphanumeric characters** include letters and numbers.

### Constraints
- `1 <= len(s) <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## 2. Example

### Example 1

**Input**
```python
s = "A man, a plan, a canal: Panama"
```

**Output**
```python
True
```

**Explanation:** After removing spaces and punctuation and converting to lowercase, the string becomes `amanaplanacanalpanama`, which reads the same forward and backward.

### Example 2

**Input**
```python
s = "race a car"
```

**Output**
```python
False
```

**Explanation:** After cleaning, the string becomes `raceacar`, which is not a palindrome.

### Example 3

**Input**
```python
s = " "
```

**Output**
```python
True
```

**Explanation:** Removing non-alphanumeric characters leaves an empty string. An empty string is a palindrome.

## 3. Approach

Use **two pointers** so we do not need to build a separate cleaned string.

- `left` starts at the beginning.
- `right` starts at the end.
- Move `left` forward while it points to a non-alphanumeric character.
- Move `right` backward while it points to a non-alphanumeric character.
- Compare the two characters in lowercase.
- If they differ, return `False`. Otherwise, move both pointers inward.
- If the pointers meet or cross, all pairs matched, so return `True`.

Python's `isalnum()` checks whether a character is a letter or a number.

## 4. Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(s) - 1`.
3. While `left < right`:
   - If `s[left]` is not alphanumeric, increment `left` and continue.
   - If `s[right]` is not alphanumeric, decrement `right` and continue.
   - If `s[left].lower() != s[right].lower()`, return `False`.
   - Increment `left` and decrement `right`.
4. Return `True`.

## 5. Code

```python
class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

## 6. Dry Run

Input: `s = "A man, a plan, a canal: Panama"`

The two pointers skip spaces and punctuation, then compare letters without considering case.

| Comparison | Left character | Right character | Result |
|---:|---|---|---|
| 1 | `A` | `a` | Match |
| 2 | `m` | `m` | Match |
| 3 | `a` | `a` | Match |
| 4 | `n` | `n` | Match |
| 5 | `a` | `a` | Match |
| 6 | `p` | `P` | Match |
| 7 | `l` | `l` | Match |
| 8 | `a` | `a` | Match |
| 9 | `n` | `n` | Match |

The pointers continue inward, skipping spaces and punctuation. No mismatch is found.

**Final output:** `True`

## 7. Complexity

Let `n` be the length of `s`.

- **Time Complexity: `O(n)`** — each pointer moves across the string at most once.
- **Auxiliary Space Complexity: `O(1)`** — only two pointers are used; no cleaned copy of the string is created.

## 8. Pattern

**Pattern: Two Pointers from Both Ends**

Use this pattern when:
- Comparing a sequence from the beginning and end.
- Checking whether a string reads the same in reverse.
- Ignoring characters that do not meet a condition.
- Solving the problem in-place or with constant extra space.

**Related problems:**
- [Valid Palindrome II — #680](https://leetcode.com/problems/valid-palindrome-ii/)
- [Reverse String — #344](https://leetcode.com/problems/reverse-string/)
- [Two Sum II — #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
