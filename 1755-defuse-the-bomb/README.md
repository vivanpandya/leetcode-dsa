# 1652. Defuse the Bomb

[LeetCode Problem](https://leetcode.com/problems/defuse-the-bomb/)  
**Difficulty:** Easy  
**Pattern:** Sliding Window + Circular Array

---

## 1. Question

You are given a circular array `code` of length `n` and an integer `k`.

- If `k > 0`, replace each element with the sum of the next `k` elements.
- If `k < 0`, replace each element with the sum of the previous `-k` elements.
- If `k == 0`, replace every element with `0`.

The array is circular: after the last element comes the first element, and before the first element comes the last element. Return the decrypted array.

## 2. Examples

### Example 1

**Input:**
```python
code = [5,7,1,4]
k = 3
```
**Output:**
```python
[12,10,16,13]
```

Explanation:
- Index 0: `7 + 1 + 4 = 12`
- Index 1: `1 + 4 + 5 = 10`
- Index 2: `4 + 5 + 7 = 16`
- Index 3: `5 + 7 + 1 = 13`

### Example 2

**Input:**
```python
code = [1,2,3,4]
k = 0
```
**Output:** `[0,0,0,0]`

### Example 3

**Input:**
```python
code = [2,4,9,3]
k = -2
```
**Output:** `[12,5,6,13]`

Explanation: Use the previous two elements:
- Index 0: `3 + 9 = 12`
- Index 1: `2 + 3 = 5`
- Index 2: `4 + 2 = 6`
- Index 3: `9 + 4 = 13`

## 3. Approach

We use **Sliding Window** to avoid calculating the sum of `k` elements from scratch for every index.

There are three cases:

1. If `k == 0`, return an array of zeros.
2. If `k > 0`, calculate the sum of the next `k` elements for index 0. Then slide the window by removing the outgoing element and adding the incoming element.
3. If `k < 0`, calculate the sum of the previous `-k` elements for index 0. Then slide the window in the same way.

Because the array is circular, use modulo `% n` to wrap indices around the array.

## 4. Algorithm

1. Find the length `n` and create a result array filled with zeros.
2. If `k == 0`, return the result.
3. Initialize `window = 0`.
4. If `k > 0`:
   - Calculate the sum of the next `k` elements for index 0.
   - For each index, store the current window sum.
   - Remove the outgoing element and add the incoming element.
5. If `k < 0`:
   - Convert `k` to `-k`.
   - Calculate the sum of the previous `k` elements for index 0.
   - For each index, store the current window sum.
   - Remove the outgoing element and add the incoming element.
6. Return the result.

## 5. Code

```python
class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        window = 0

        if k > 0:
            # Sum the next k elements for index 0
            for i in range(1, k + 1):
                window += code[i % n]

            # Slide the window
            for i in range(n):
                result[i] = window
                window -= code[(i + 1) % n]
                window += code[(i + k + 1) % n]

        else:
            k = -k

            # Sum the previous k elements for index 0
            for i in range(1, k + 1):
                window += code[-i]

            # Slide the window
            for i in range(n):
                result[i] = window
                window -= code[(i - k) % n]
                window += code[i]

        return result
```

## 6. Dry Run

### Positive `k`

Input:
```python
code = [5,7,1,4]
k = 3
```

First window for index 0:
```python
window = code[1] + code[2] + code[3]
window = 7 + 1 + 4
window = 12
```

Then slide the window:

| Index | Window elements | Sum | Result |
|---|---|---:|---:|
| 0 | `7 + 1 + 4` | 12 | 12 |
| 1 | `1 + 4 + 5` | 10 | 10 |
| 2 | `4 + 5 + 7` | 16 | 16 |
| 3 | `5 + 7 + 1` | 13 | 13 |

Output: `[12,10,16,13]`

### Negative `k`

Input:
```python
code = [2,4,9,3]
k = -2
```

Convert `k` to `2`. The first window uses the previous two elements of index 0:

```python
window = code[3] + code[2]
window = 3 + 9
window = 12
```

Then slide:

| Index | Previous elements | Sum | Result |
|---|---|---:|---:|
| 0 | `3 + 9` | 12 | 12 |
| 1 | `2 + 3` | 5 | 5 |
| 2 | `4 + 2` | 6 | 6 |
| 3 | `9 + 4` | 13 | 13 |

Output: `[12,5,6,13]`

## 7. Complexity

Let `n` be the length of `code`.

- **Time Complexity:** `O(n)` — Calculate the first window once, then slide through the array.
- **Space Complexity:** `O(n)` — The result array stores `n` values. Auxiliary working space is `O(1)`.

## 8. Pattern

**Sliding Window + Circular Array**

Key ideas:
- Calculate the first window sum once.
- Remove the element leaving the window.
- Add the element entering the window.
- Use modulo `% n` to wrap around the circular array.

This avoids recalculating all `k` elements for every position.

---

## Original Constraints

- `n == code.length`
- `1 <= n <= 100`
- `1 <= code[i] <= 100`
- `-(n - 1) <= k <= n - 1`
