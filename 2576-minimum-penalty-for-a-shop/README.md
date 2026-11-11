# 2483. Minimum Penalty for a Shop

[LeetCode Problem](https://leetcode.com/problems/minimum-penalty-for-a-shop/)  
**Difficulty:** Medium  
**Pattern:** Greedy / One Pass

---

## Problem Statement

You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

- If `customers[i] == 'Y'`, customers come at the `i`th hour.
- If `customers[i] == 'N'`, no customers come at the `i`th hour.

If the shop closes at hour `j` (`0 <= j <= n`), the penalty is calculated as follows:

- For every hour when the shop is open and no customers come, the penalty increases by `1`.
- For every hour when the shop is closed and customers come, the penalty increases by `1`.

Return the **earliest hour** at which the shop must be closed to incur a **minimum penalty**.

If the shop closes at hour `j`, it is closed starting from hour `j`.

### Example 1

```text
Input: customers = "YYNY"
Output: 2
```

Explanation:

- Closing at hour `0`: penalty = `1 + 1 + 0 + 1 = 3`
- Closing at hour `1`: penalty = `0 + 1 + 0 + 1 = 2`
- Closing at hour `2`: penalty = `0 + 0 + 0 + 1 = 1`
- Closing at hour `3`: penalty = `0 + 0 + 1 + 1 = 2`
- Closing at hour `4`: penalty = `0 + 0 + 1 + 0 = 1`

Closing at hour `2` or `4` gives the minimum penalty. Since `2` is earlier, return `2`.

### Example 2

```text
Input: customers = "NNNNN"
Output: 0
```

Explanation: No customers arrive, so closing immediately gives the minimum penalty.

### Example 3

```text
Input: customers = "YYYY"
Output: 4
```

Explanation: Customers arrive every hour, so keeping the shop open for all hours gives the minimum penalty.

### Constraints

- `1 <= customers.length <= 10^5`
- `customers` consists only of `'Y'` and `'N'`.

---

## 1. Approach

We can solve this problem using a **Greedy One-Pass Approach**.

First, imagine that the shop closes at hour `0`. This means it never opens.

- Every `'Y'` represents a customer arriving while the shop is closed, so it adds `1` penalty.
- Every `'N'` is irrelevant because the shop is closed.

Therefore, the initial penalty is simply:

```python
penalty = customers.count('Y')
```

Now, move the closing time one hour to the right.

When we move the closing time past one character:

- If the character is `'Y'`, that hour changes from closed to open. The penalty decreases by `1`.
- If the character is `'N'`, that hour changes from closed to open. The penalty increases by `1`.

We keep track of the smallest penalty and the earliest closing hour that achieves it.

**Important:** Update the answer only when `penalty < best_penalty`, not when it is equal. This preserves the earliest hour when multiple closing times have the same minimum penalty.

---

## 2. Algorithm

1. Count the total number of `'Y'` characters. This is the penalty when closing at hour `0`.
2. Set `best_penalty` to the initial penalty.
3. Set `best_hour = 0`.
4. Traverse the string using `enumerate()`.
5. For each character:
   - If it is `'Y'`, subtract `1` from the current penalty.
   - Otherwise, add `1` to the current penalty.
6. If the current penalty is strictly smaller than `best_penalty`:
   - Update `best_penalty`.
   - Set `best_hour = i + 1`.
7. Return `best_hour`.

---

## 3. Code

```python
class Solution:
    def bestClosingTime(self, customers):
        penalty = customers.count('Y')

        best_penalty = penalty
        best_hour = 0

        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1

            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = i + 1

        return best_hour
```

---

## 4. Dry Run

Consider:

```python
customers = "YYNY"
```

### Initial state

Closing at hour `0` means the shop is closed for all four hours. There are three `'Y'` characters, so:

```python
penalty = 3
best_penalty = 3
best_hour = 0
```

### Iteration table

| `i` | `ch` | Operation | Current penalty | Best penalty | Best hour |
|---:|:---:|---|---:|---:|---:|
| Initial | — | Count all `'Y'` | 3 | 3 | 0 |
| 0 | Y | `penalty -= 1` | 2 | 2 | 1 |
| 1 | Y | `penalty -= 1` | 1 | 1 | 2 |
| 2 | N | `penalty += 1` | 2 | 1 | 2 |
| 3 | Y | `penalty -= 1` | 1 | 1 | 2 |

At the final iteration, the penalty becomes `1`, which equals the best penalty. We do not update the answer because the condition is strictly `<`.

Therefore:

```python
return 2
```

**Output:**

```python
2
```

---

## 5. Why This Works

The initial penalty represents closing the shop at hour `0`.

Each time we move the closing hour one position to the right, exactly one hour changes from closed to open:

- A `'Y'` hour stops causing a penalty, so the penalty decreases by `1`.
- An `'N'` hour starts causing a penalty, so the penalty increases by `1`.

Thus, we can calculate the penalty for every possible closing hour by updating the previous penalty in constant time.

We examine closing hours in increasing order. Since we update the best hour only when the penalty becomes **strictly smaller**, the first hour with the minimum penalty is retained.

Therefore, the algorithm returns the earliest closing hour with minimum penalty.

---

## 6. Complexity Analysis

Let `n` be the length of `customers`.

### Time Complexity: `O(n)`

- `customers.count('Y')` takes `O(n)`.
- The loop visits every character once, taking `O(n)`.
- Each iteration performs constant-time operations.

Total: `O(n) + O(n) = O(n)`.

### Space Complexity: `O(1)`

We use only a fixed number of variables (`penalty`, `best_penalty`, `best_hour`, `i`, and `ch`). No additional array or data structure is created.

---

## 7. Pattern

**Greedy + One Pass + Running State**

Recognize this pattern when:

- You need to evaluate every possible split or boundary.
- Moving the boundary changes the answer by a small, predictable amount.
- Recalculating the entire answer at every boundary would be inefficient.

Instead of calculating every penalty from scratch, update the current penalty as the boundary moves.

### Key Logic to Remember

```python
if ch == 'Y':
    penalty -= 1
else:
    penalty += 1
```

And to preserve the earliest minimum:

```python
if penalty < best_penalty:
    best_penalty = penalty
    best_hour = i + 1
```

**Main takeaway:** Start with the penalty at closing hour `0`, then update it in one pass as the shop's closing time moves forward.
