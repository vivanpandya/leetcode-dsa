# 2055. Plates Between Candles

[LeetCode Problem](https://leetcode.com/problems/plates-between-candles/)  
**Difficulty:** Medium  
**Pattern:** Prefix Sum + Precomputation + Binary Search / Nearest Candles

---

## Problem Statement

There is a long table with a line of plates and candles arranged on top of it. You are given a **0-indexed** string `s` consisting of characters `'*'` and `'|'` only:

- `'*'` represents a plate.
- `'|'` represents a candle.

You are also given a **0-indexed** 2D integer array `queries`, where `queries[i] = [left_i, right_i]` represents the substring `s[left_i...right_i]` (inclusive).

For each query, find the number of plates that are between candles inside that substring. A plate is between candles if there is at least one candle to its left and at least one candle to its right within the substring.

Return an integer array `answer`, where `answer[i]` is the answer for the `i`th query.

### Example 1

```text
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
```

Explanation:
- Query `[2,5]` contains two plates between the candles.
- Query `[5,9]` contains three plates between the candles.

### Example 2

```text
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
```

Explanation:
- Query `[1,17]` contains nine plates between the outermost candles in that substring.
- The other queries do not contain plates enclosed by two candles.

### Constraints

- `3 <= s.length <= 10^5`
- `s` consists of `'*'` and `'|'` characters.
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= left_i <= right_i < s.length`

---

## 1. Approach

We need to answer up to `10^5` queries, so checking every character inside every query would be too slow.

We can preprocess three pieces of information:

1. **Prefix sum:** `prefix[i]` stores the number of plates (`'*'`) from index `0` through index `i`.
2. **Nearest candle on the left:** `left_candle[i]` stores the closest candle at or before index `i`.
3. **Nearest candle on the right:** `right_candle[i]` stores the closest candle at or after index `i`.

For a query `[left, right]`:

- Find the first candle inside the query using `right_candle[left]`.
- Find the last candle inside the query using `left_candle[right]`.
- If either candle does not exist inside the query, the answer is `0`.
- Otherwise, count the plates strictly between those two candles using the prefix sum.

If the first candle is at index `start` and the last candle is at index `end`, the number of plates is:

```python
prefix[end] - prefix[start]
```

This works because both boundary positions are candles, not plates, so the difference counts only the plates between them.

---

## 2. Algorithm

### Preprocessing

1. Create a prefix sum array of length `n + 1`, initially filled with zero.
2. Traverse `s` from left to right:
   - Copy the previous prefix sum.
   - Add `1` if the current character is `'*'`.
3. Build `left_candle`:
   - Traverse from left to right.
   - Keep the most recent candle index.
   - Store it at every position.
4. Build `right_candle`:
   - Traverse from right to left.
   - Keep the next candle index.
   - Store it at every position.

### Answering each query

For every `[left, right]`:

1. Set `start = right_candle[left]`.
2. Set `end = left_candle[right]`.
3. If `start == -1`, `end == -1`, or `start >= end`, append `0`.
4. Otherwise, append `prefix[end] - prefix[start]`.
5. Return the answer array.

---

## 3. Code

```python
class Solution:
    def platesBetweenCandles(self, s, queries):
        n = len(s)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i]
            if s[i] == '*':
                prefix[i + 1] += 1

        left_candle = [-1] * n
        last_candle = -1

        for i in range(n):
            if s[i] == '|':
                last_candle = i
            left_candle[i] = last_candle

        right_candle = [-1] * n
        next_candle = -1

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                next_candle = i
            right_candle[i] = next_candle

        answer = []

        for left, right in queries:
            start = right_candle[left]
            end = left_candle[right]

            if start == -1 or end == -1 or start >= end:
                answer.append(0)
            else:
                answer.append(prefix[end] - prefix[start])

        return answer
```

---

## 4. Dry Run

Consider:

```python
s = "**|**|***|"
queries = [[2, 5], [5, 9]]
```

Index the string:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Character | `*` | `*` | `|` | `*` | `*` | `|` | `*` | `*` | `*` | `|` |

### Precomputed prefix sum

`prefix[i]` counts plates before index `i` in the original string, using a prefix array of length `n + 1`.

```text
prefix = [0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
```

### Query 1: `[2, 5]`

```python
start = right_candle[2]  # 2
end = left_candle[5]     # 5
```

The substring is:

```text
|**|
```

Number of plates:

```python
prefix[5] - prefix[2]
= 4 - 2
= 2
```

Answer for this query: `2`.

### Query 2: `[5, 9]`

```python
start = right_candle[5]  # 5
end = left_candle[9]     # 9
```

The substring is:

```text
|***|
```

Number of plates:

```python
prefix[9] - prefix[5]
= 7 - 4
= 3
```

Answer for this query: `3`.

Final result:

```python
[2, 3]
```

---

## 5. Why This Works

For every query, a plate counts only if it lies after a candle and before another candle within the query.

- `right_candle[left]` gives the earliest candle that is not before the query.
- `left_candle[right]` gives the latest candle that is not after the query.

Therefore, these two indices are exactly the outermost candles that can enclose valid plates in the query.

If the first candle is missing, the last candle is missing, or both positions are the same or reversed, there cannot be any plates between two candles.

Otherwise, every plate between these two candle positions is valid. The prefix sum difference counts exactly those plates:

```python
prefix[end] - prefix[start]
```

Thus, each query is answered correctly.

---

## 6. Complexity Analysis

Let:
- `n` be the length of string `s`.
- `q` be the number of queries.

### Time Complexity: `O(n + q)`

Preprocessing:
- Building the prefix sum: `O(n)`.
- Building the nearest-left-candle array: `O(n)`.
- Building the nearest-right-candle array: `O(n)`.

Queries:
- Each query takes `O(1)` time.
- All queries take `O(q)` time.

Total:

```text
O(n) + O(n) + O(n) + O(q) = O(n + q)
```

### Space Complexity: `O(n)`

We create three arrays of size `n` (or `n + 1` for the prefix sum):

- `prefix`
- `left_candle`
- `right_candle`

The answer array takes `O(q)` output space.

Auxiliary space, excluding the returned output, is `O(n)`.

---

## 7. Pattern

**Prefix Sum + Precomputation + Range Queries**

Use this pattern when:

- Many queries ask for counts inside different ranges.
- You need to find the nearest valid boundary on either side.
- Repeatedly scanning each range would be too slow.

### Key Logic to Remember

Find the first candle inside the query:

```python
start = right_candle[left]
```

Find the last candle inside the query:

```python
end = left_candle[right]
```

Count plates between them:

```python
prefix[end] - prefix[start]
```

**Main takeaway:** Precompute prefix counts and nearest boundaries once, then answer each range query in constant time.
