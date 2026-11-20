# 2300. Successful Pairs of Spells and Potions

[LeetCode Problem](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics
- Array
- Two Pointers
- Binary Search
- Sorting

---

## 1. Problem Statement

You are given two positive integer arrays, `spells` and `potions`.

- `spells[i]` represents the strength of the `i`th spell.
- `potions[j]` represents the strength of the `j`th potion.

You are also given an integer `success`.

A spell and potion pair is successful if the product of their strengths is at least `success`:

```text
spells[i] * potions[j] >= success
```

Return an integer array `pairs` where `pairs[i]` is the number of potions that form a successful pair with the `i`th spell.

### Example 1

**Input:**
```python
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
```

**Output:**
```python
[4, 0, 3]
```

**Explanation:**

- Spell `5`: products are `[5, 10, 15, 20, 25]`. Four are at least `7`.
- Spell `1`: products are `[1, 2, 3, 4, 5]`. None are at least `7`.
- Spell `3`: products are `[3, 6, 9, 12, 15]`. Three are at least `7`.

Therefore, the answer is `[4, 0, 3]`.

### Example 2

**Input:**
```python
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
```

**Output:**
```python
[2, 0, 2]
```

**Explanation:**

- Spell `3`: products are `[24, 15, 24]`. Two are successful.
- Spell `1`: products are `[8, 5, 8]`. None are successful.
- Spell `2`: products are `[16, 10, 16]`. Two are successful.

Therefore, the answer is `[2, 0, 2]`.

### Constraints

- `n == spells.length`
- `m == potions.length`
- `1 <= n, m <= 10^5`
- `1 <= spells[i], potions[i] <= 10^5`
- `1 <= success <= 10^10`

---

## 2. Approach: Sorting + Binary Search (Lower Bound)

We need to count how many potions make a successful pair with each spell.

The key observation is that all spell and potion strengths are positive.

For a particular spell:

```text
spell * potion >= success
```

Divide both sides by `spell`:

```text
potion >= success / spell
```

So, for each spell, we need to find the smallest potion strength that is large enough to make the product at least `success`.

### Step 1: Sort the potions

```python
potions.sort()
```

After sorting, all potions from a valid position to the end of the array will also be successful.

### Step 2: Calculate the minimum required potion strength

We need the smallest integer potion strength satisfying:

```text
potion >= success / spell
```

Use integer ceiling division:

```python
required = (success + spell - 1) // spell
```

This calculates the smallest integer greater than or equal to `success / spell`, without using floating-point division.

### Step 3: Find the first valid potion using binary search

Use a lower-bound binary search to find the first index where:

```python
potions[mid] >= required
```

Initialize:

```python
left = 0
right = len(potions)
```

The right boundary is exclusive, so it can also represent the position just after the last potion.

- If `potions[mid] >= required`, this potion may be the first valid one. Keep searching to the left by setting `right = mid`.
- Otherwise, this potion is too small. Search to the right by setting `left = mid + 1`.

### Step 4: Count successful potions

When the loop ends, `left` is the first index containing a valid potion.

Therefore:

```python
count = len(potions) - left
```

If no potion is valid, `left` becomes `len(potions)` and the count is `0`.

Repeat this process for every spell.

---

## 3. Algorithm

1. Sort `potions` in ascending order.
2. Create an empty list called `result`.
3. For each `spell` in `spells`:
   1. Calculate the minimum required potion strength:
      `required = (success + spell - 1) // spell`.
   2. Set `left = 0` and `right = len(potions)`.
   3. While `left < right`:
      - Calculate `mid = (left + right) // 2`.
      - If `potions[mid] >= required`, set `right = mid`.
      - Otherwise, set `left = mid + 1`.
   4. Calculate `count = len(potions) - left`.
   5. Append `count` to `result`.
4. Return `result`.

---

## 4. Python Code

```python
class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()

        result = []

        for spell in spells:
            required = (success + spell - 1) // spell

            left = 0
            right = len(potions)

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= required:
                    right = mid
                else:
                    left = mid + 1

            count = len(potions) - left
            result.append(count)

        return result
```

---

## 5. Dry Run

**Input:**

```python
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
```

First, sort the potions:

```python
potions = [1, 2, 3, 4, 5]
```

### Spell 1: `spell = 5`

Calculate the required potion strength:

```text
required = (success + spell - 1) // spell
         = (7 + 5 - 1) // 5
         = 11 // 5
         = 2
```

Binary search for the first potion greater than or equal to `2`:

| `left` | `right` | `mid` | `potions[mid]` | Decision |
|---:|---:|---:|---:|---|
| 0 | 5 | 2 | 3 | Valid; `right = 2` |
| 0 | 2 | 1 | 2 | Valid; `right = 1` |
| 0 | 1 | 0 | 1 | Too small; `left = 1` |

Now `left = 1`.

```text
count = 5 - 1 = 4
```

Four potions are successful.

### Spell 2: `spell = 1`

```text
required = (7 + 1 - 1) // 1
         = 7
```

No potion is greater than or equal to `7`.

Binary search ends with:

```text
left = 5
count = 5 - 5 = 0
```

Zero potions are successful.

### Spell 3: `spell = 3`

```text
required = (7 + 3 - 1) // 3
         = 9 // 3
         = 3
```

The first potion greater than or equal to `3` is at index `2`.

```text
count = 5 - 2 = 3
```

Three potions are successful.

### Final result

| Spell | Required potion strength | First valid index | Successful potions |
|---:|---:|---:|---:|
| 5 | 2 | 1 | 4 |
| 1 | 7 | 5 | 0 |
| 3 | 3 | 2 | 3 |

**Output:**
```python
[4, 0, 3]
```

---

## 6. Why This Works

Sorting makes the potion strengths non-decreasing.

For each spell, the required potion strength is fixed. Once binary search finds the first potion that meets this requirement, every potion after that position also meets it.

The lower-bound binary search finds exactly that first valid position.

Subtracting the position from the total number of potions gives the number of successful potions.

Repeating this for every spell produces the required answer.

---

## 7. Complexity Analysis

Let:
- `n` = number of spells.
- `m` = number of potions.

| Operation | Time Complexity |
|---|---|
| Sort `potions` | `O(m log m)` |
| Process all spells | `O(n)` |
| Binary search for each spell | `O(log m)` |
| All binary searches | `O(n log m)` |

**Total Time Complexity:**

```text
O(m log m + n log m)
```

**Auxiliary Space Complexity:**

- `O(1)` auxiliary space for the binary search variables, excluding the sorting implementation.
- `O(n)` space for the returned `result` list.

Sorting is performed in place with `potions.sort()`.

---

## 8. Pattern and Related Problems

**Pattern:** Sorting + Lower Bound Binary Search.

Recognize this pattern when:
- You need to count elements that satisfy a threshold.
- The array can be sorted.
- You need the first element greater than or equal to a target.
- Every element after that position also satisfies the condition.

Related LeetCode problems:

| Problem | LeetCode Number | Pattern |
|---|---:|---|
| Search Insert Position | 35 | Lower Bound Binary Search |
| First Bad Version | 278 | First True Binary Search |
| Koko Eating Bananas | 875 | Binary Search on Answer |
| Successful Pairs of Spells and Potions | 2300 | Sorting + Lower Bound |

### Important lines to remember

Calculate the minimum required potion strength:

```python
required = (success + spell - 1) // spell
```

Find the first valid potion:

```python
if potions[mid] >= required:
    right = mid
else:
    left = mid + 1
```

Count all valid potions:

```python
count = len(potions) - left
```
