# 744. Find Smallest Letter Greater Than Target

[LeetCode Problem](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)  
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Topics
- Array
- Binary Search

---

## 1. Problem Statement

You are given an array of characters `letters` sorted in **non-decreasing order**, and a character `target`.

Return the smallest character in `letters` that is **strictly greater than** `target`. If no such character exists, return the first character in `letters`.

### Example 1
**Input:**
```python
letters = ["c", "f", "j"]
target = "a"
```
**Output:**
```python
"c"
```
The smallest character greater than `"a"` is `"c"`.

### Example 2
**Input:**
```python
letters = ["c", "f", "j"]
target = "c"
```
**Output:**
```python
"f"
```
The answer must be strictly greater than `"c"`, so `"f"` is returned.

### Example 3
**Input:**
```python
letters = ["x", "x", "y", "y"]
target = "z"
```
**Output:**
```python
"x"
```
No character is greater than `"z"`, so return `letters[0]`.

### Constraints
- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter.
- `letters` is sorted in non-decreasing order.
- `letters` contains at least two different characters.
- `target` is a lowercase English letter.

---

## 2. Approach: Binary Search (Upper Bound)

Because the array is sorted, we can use binary search to find the **first character strictly greater than `target`**. This is called an **upper bound** search.

Initialize:
```python
left = 0
right = len(letters) - 1
```

For each middle character:
- If `letters[mid] <= target`, it cannot be the answer. Search the right half using `left = mid + 1`.
- If `letters[mid] > target`, it may be the answer. Search the left half using `right = mid - 1`.

When the loop ends, `left` points to the first character greater than `target`.

- If `left < len(letters)`, return `letters[left]`.
- If `left == len(letters)`, no greater character exists, so return `letters[0]`.

**Important:** Use `<= target` because the answer must be strictly greater than the target.

---

## 3. Algorithm

1. Set `left = 0` and `right = len(letters) - 1`.
2. While `left <= right`:
   1. Calculate `mid = (left + right) // 2`.
   2. If `letters[mid] <= target`, set `left = mid + 1`.
   3. Otherwise, set `right = mid - 1`.
3. After the loop:
   - If `left == len(letters)`, return `letters[0]`.
   - Otherwise, return `letters[left]`.

---

## 4. Python Code

```python
class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left == len(letters):
            return letters[0]

        return letters[left]
```

---

## 5. Dry Run

**Input:**
```python
letters = ["c", "f", "j"]
target = "c"
```

Initial values:
```text
left = 0
right = 2
```

### Iteration 1
```text
mid = (0 + 2) // 2 = 1
letters[mid] = "f"
```
`"f" <= "c"` is false, so search left:
```text
right = mid - 1 = 0
```

### Iteration 2
```text
mid = (0 + 0) // 2 = 0
letters[mid] = "c"
```
`"c" <= "c"` is true. A character equal to the target is not valid, so move right:
```text
left = mid + 1 = 1
```

Now `left = 1` and `right = 0`, so the loop ends.

Return:
```python
letters[left]  # letters[1] = "f"
```

**Output:**
```python
"f"
```

### Dry Run Summary

| `left` | `right` | `mid` | `letters[mid]` | Decision |
|---:|---:|---:|---|---|
| 0 | 2 | 1 | `"f"` | Greater than target; move `right` to 0 |
| 0 | 0 | 0 | `"c"` | Equal to target; move `left` to 1 |

---

## 6. Why This Works

Since the array is sorted:
- When `letters[mid] <= target`, the middle character and every character before it cannot be the answer. Move right.
- When `letters[mid] > target`, the middle character could be the answer, but an earlier valid character may exist. Move left.

When binary search finishes, `left` identifies the first character strictly greater than `target`. If `left` is outside the array, the required wraparound answer is `letters[0]`.

---

## 7. Complexity Analysis

Let `n` be the number of characters in `letters`.

| Complexity | Value | Reason |
|---|---|---|
| Time | `O(log n)` | Binary search halves the search range in each iteration. |
| Auxiliary Space | `O(1)` | Only a fixed number of variables are used. |

---

## 8. Pattern and Related Problems

**Pattern: Binary Search – Upper Bound**

Use this pattern when you need to find the **first element strictly greater than a target** in a sorted array.

### Important comparison

| Search type | Finds |
|---|---|
| Lower Bound | First element `>= target` |
| Upper Bound | First element `> target` |

### Important lines to remember

```python
if letters[mid] <= target:
    left = mid + 1
else:
    right = mid - 1
```

After the loop:
```python
if left == len(letters):
    return letters[0]

return letters[left]
```

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Binary Search | 704 | Basic Binary Search |
| Search Insert Position | 35 | Lower Bound |
| Find First and Last Position of Element in Sorted Array | 34 | Boundary Binary Search |
| H-Index II | 275 | Binary Search |
| Find Smallest Letter Greater Than Target | 744 | Upper Bound |
