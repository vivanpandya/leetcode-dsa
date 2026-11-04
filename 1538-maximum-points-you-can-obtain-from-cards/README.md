# 1423. Maximum Points You Can Obtain from Cards

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

---

## Problem Statement

There are several cards arranged in a row. Each card has a number of points, given in the integer array `cardPoints`.

In one step, you can take one card from either the beginning or the end of the row. You must take exactly `k` cards.

Return the **maximum score** you can obtain.

## Examples

### Example 1

```text
Input:  cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: Take the three cards from the right: 1 + 6 + 5 = 12.
```

### Example 2

```text
Input:  cardPoints = [2,2,2], k = 2
Output: 4
```

### Example 3

```text
Input:  cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: All cards must be taken.
```

## Constraints

- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`

---

## Approach: Fixed-Size Sliding Window

Instead of directly trying every combination of taking cards from the left and right, think about the cards we **do not take**.

- There are `n` cards in total.
- We must take exactly `k` cards.
- Therefore, we leave exactly `n - k` cards.
- Since cards can only be taken from the two ends, the cards left behind must form one continuous middle subarray.

To get the maximum score, leave behind the **minimum-sum subarray of length `n - k`**.

```text
Maximum score = Total sum - Minimum window sum
```

We can find that minimum window using a fixed-size sliding window.

## Algorithm

1. Find the total sum of all cards.
2. Calculate the window size: `n - k`.
3. If the window size is `0`, all cards must be taken, so return the total sum.
4. Calculate the sum of the first window of size `n - k`.
5. Store this sum in both `window_sum` and `min_sum`.
6. Slide the window through the array:
   - Add the new element entering from the right.
   - Subtract the element leaving from the left.
   - Update `min_sum` if the new window sum is smaller.
7. Return `total - min_sum`.

## Python Code

```python
class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total = sum(cardPoints)

        window_size = n - k

        if window_size == 0:
            return total

        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum

        for right in range(window_size, n):
            window_sum += cardPoints[right]
            window_sum -= cardPoints[right - window_size]

            min_sum = min(min_sum, window_sum)

        return total - min_sum
```

## Dry Run

Input:

```text
cardPoints = [1,2,3,4,5,6,1]
k = 3
```

### Step 1: Calculate the total and window size

```text
Total sum = 1 + 2 + 3 + 4 + 5 + 6 + 1 = 22
Window size = n - k = 7 - 3 = 4
```

We need to find the minimum sum among all continuous windows of size `4`.

### Step 2: Slide the window

| Window | Window sum | Minimum sum |
|---|---:|---:|
| `[1, 2, 3, 4]` | 10 | 10 |
| `[2, 3, 4, 5]` | 14 | 10 |
| `[3, 4, 5, 6]` | 18 | 10 |
| `[4, 5, 6, 1]` | 16 | 10 |

The minimum window sum is `10`.

### Step 3: Calculate the answer

```text
Maximum score = Total sum - Minimum window sum
              = 22 - 10
              = 12
```

**Output: `12`**

The four cards left behind are `[1, 2, 3, 4]`. We take the remaining cards `[5, 6, 1]`, whose total is `12`.

## Why This Works

When we take cards only from the beginning or the end, the cards we do not take must stay together in the middle.

For every selection of exactly `k` cards, the remaining middle section has exactly `n - k` cards. The score of the selected cards equals the total sum minus the sum of that remaining section.

Therefore, maximizing the selected score is equivalent to minimizing the sum of a continuous subarray of length `n - k`. The sliding window checks every such subarray efficiently.

## Complexity Analysis

Let `n` be the number of cards.

- **Time Complexity: `O(n)`** — Calculating the total, initializing the window, and sliding through the array each take linear time.
- **Space Complexity: `O(n)` auxiliary space for this exact code** — The slice `cardPoints[:window_size]` creates a temporary list. Apart from that slice, the algorithm uses `O(1)` extra variables. If the initial window sum is calculated with a loop instead of slicing, auxiliary space becomes `O(1)`.

## Pattern

**Fixed-Size Sliding Window**

Use this transformation when:
- You must select exactly `k` elements from the two ends of an array.
- The unselected elements form one continuous middle subarray.
- You can convert maximizing the selected sum into minimizing the remaining window sum.

**Key formula:**

```python
answer = sum(cardPoints) - minimum_sum_of_window_size_n_minus_k
```

**Important edge case:** If `k == len(cardPoints)`, the window size is `0`, so every card must be taken and the answer is simply the total sum.
