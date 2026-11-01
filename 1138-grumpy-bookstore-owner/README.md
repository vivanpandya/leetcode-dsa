# 1052. Grumpy Bookstore Owner

[LeetCode Problem](https://leetcode.com/problems/grumpy-bookstore-owner/)  
**Difficulty:** Medium  
**Pattern:** Sliding Window

---

## 1. Question

A bookstore is open for `n` minutes.

- `customers[i]` is the number of customers entering during minute `i`.
- `grumpy[i] == 1` means the owner is grumpy, so those customers are not satisfied.
- `grumpy[i] == 0` means those customers are already satisfied.
- The owner can use a technique once to remain not grumpy for `minutes` consecutive minutes.

Return the maximum number of satisfied customers.

## 2. Examples

### Example 1

**Input:**
```python
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
```

**Output:** `16`

**Explanation:** Customers already satisfied = `1 + 1 + 1 + 7 = 10`. The best window adds `1 + 5 = 6` more customers. Total = `16`.

### Example 2

**Input:**
```python
customers = [1]
grumpy = [0]
minutes = 1
```

**Output:** `1`

## 3. Approach

We use a **Fixed-Size Sliding Window**.

There are two parts:

1. `satisfied`: Count all customers who are already satisfied (`grumpy[i] == 0`) across the entire array.
2. `extra`: Find the maximum number of additional customers we can satisfy by choosing one window of length `minutes`. Only count customers where `grumpy[i] == 1`, because the others are already counted.

First calculate the extra customers in the initial window. Then slide the window:
- Add the incoming customer count if that minute is grumpy.
- Remove the outgoing customer count if that minute was grumpy.
- Update the maximum extra customers.

Finally return `satisfied + max_extra`.

## 4. Algorithm

1. Set `satisfied = 0`.
2. Traverse the whole array and add `customers[i]` when `grumpy[i] == 0`.
3. Calculate `extra` for the first `minutes` positions, adding only grumpy minutes.
4. Set `max_extra = extra`.
5. Slide the window across the remaining array:
   - Add the incoming position if it is grumpy.
   - Subtract the outgoing position if it was grumpy.
   - Update `max_extra`.
6. Return `satisfied + max_extra`.

## 5. Code

```python
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        satisfied = 0
        extra = 0

        # Count customers who are already satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # Calculate extra customers in the first window
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        # Slide the window
        for right in range(minutes, len(customers)):
            # Add the incoming minute
            if grumpy[right] == 1:
                extra += customers[right]

            # Remove the outgoing minute
            if grumpy[right - minutes] == 1:
                extra -= customers[right - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra
```

## 6. Dry Run

Input:

```python
customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
minutes = 3
```

### Step 1: Already satisfied customers

Add values where `grumpy[i] == 0`:

- Index 0: `1`
- Index 2: `1`
- Index 4: `1`
- Index 6: `7`

So:

```python
satisfied = 1 + 1 + 1 + 7 = 10
```

### Step 2: First window (indices 0–2)

Only grumpy positions contribute to `extra`. Index 1 has 0 customers, so:

```python
extra = 0
max_extra = 0
```

### Step 3: Slide the window

| Window indices | Incoming | Outgoing | Current extra | Maximum extra |
|---|---:|---:|---:|---:|
| 0–2 | Initial window | — | 0 | 0 |
| 1–3 | +2 (index 3) | −0 (index 0) | 2 | 2 |
| 2–4 | +0 (index 4) | −0 (index 1) | 2 | 2 |
| 3–5 | +1 (index 5) | −0 (index 2) | 3 | 3 |
| 4–6 | +0 (index 6) | −2 (index 3) | 1 | 3 |
| 5–7 | +5 (index 7) | −0 (index 4) | 6 | 6 |

Therefore:

```python
max_extra = 6
```

### Step 4: Final answer

```python
answer = satisfied + max_extra
answer = 10 + 6
answer = 16
```

**Output:** `16`

## 7. Complexity

Let `n` be the length of the arrays.

- **Time Complexity:** `O(n)` — the array is traversed a constant number of times.
- **Space Complexity:** `O(1)` — only a few variables are used.

## 8. Pattern

**Fixed-Size Sliding Window**

Use this pattern when finding the maximum or minimum result over a continuous window of a fixed size.

**Key lesson:** Calculate the base result over the entire array first. Then use the sliding window to find the maximum additional benefit.

---

## Original Constraints

- `n == customers.length == grumpy.length`
- `1 <= minutes <= n <= 2 * 10^4`
- `0 <= customers[i] <= 1000`
- `grumpy[i]` is either `0` or `1`.
