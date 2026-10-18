# 344. Reverse String

- **LeetCode:** [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- **Difficulty:** Easy
- **Topics:** Two Pointers, String, In-Place

## 1. Question

Write a function that reverses a string. The input is an array of characters `s`.

Reverse the array **in-place** using `O(1)` extra memory.

### Constraints
- `1 <= len(s) <= 10^5`
- `s[i]` is a printable ASCII character.

## 2. Example

### Example 1

**Input**
```python
s = ["h", "e", "l", "l", "o"]
```

**Output**
```python
["o", "l", "l", "e", "h"]
```

### Example 2

**Input**
```python
s = ["H", "a", "n", "n", "a", "h"]
```

**Output**
```python
["h", "a", "n", "n", "a", "H"]
```

## 3. Approach

Use **two pointers**:

- `left` starts at the first character.
- `right` starts at the last character.
- Swap the characters at `left` and `right`.
- Move `left` one step forward and `right` one step backward.
- Continue until the pointers meet or cross.

This reverses the array in-place, without creating another array.

## 4. Algorithm

1. Set `left = 0`.
2. Set `right = len(s) - 1`.
3. While `left < right`:
   - Swap `s[left]` and `s[right]`.
   - Increment `left`.
   - Decrement `right`.
4. The input array `s` is now reversed. LeetCode expects the array to be modified in-place, so no return value is needed.

## 5. Code

```python
class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## 6. Dry Run

Input: `s = ["h", "e", "l", "l", "o"]`

| Step | `left` | `right` | Operation | Array |
|---:|---:|---:|---|---|
| 1 | 0 | 4 | Swap `h` and `o` | `["o", "e", "l", "l", "h"]` |
| 2 | 1 | 3 | Swap `e` and `l` | `["o", "l", "l", "e", "h"]` |
| 3 | 2 | 2 | Stop because `left < right` is false | `["o", "l", "l", "e", "h"]` |

**Final array:** `["o", "l", "l", "e", "h"]`

## 7. Complexity

Let `n` be the number of characters in `s`.

- **Time Complexity: `O(n)`** — each pair of characters is swapped once, so roughly half the array is visited.
- **Auxiliary Space Complexity: `O(1)`** — the reversal uses only two pointers and modifies the original array.

## 8. Pattern

**Pattern: Two Pointers from Both Ends**

Use this pattern when:
- Reversing an array in-place.
- Swapping matching positions from opposite ends.
- Avoiding extra arrays to keep space usage constant.

**Related problems:**
- [Valid Palindrome — #125](https://leetcode.com/problems/valid-palindrome/)
- [Reverse Words in a String — #151](https://leetcode.com/problems/reverse-words-in-a-string/)
- [Two Sum II — #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
