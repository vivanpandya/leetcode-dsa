<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box">Minimum Number of Operations to Move All Balls to Each Box</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>&#39;0&#39;</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>&#39;1&#39;</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre># 1769. Minimum Number of Operations to Move All Balls to Each Box

[LeetCode Problem](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)  
**Difficulty:** Medium  
**Topics:** String, Prefix Sum, Greedy

---

## 1. Problem Statement

You have `n` boxes. You are given a binary string `boxes` of length `n`, where:

- `boxes[i] == '0'` means the `i`th box is empty.
- `boxes[i] == '1'` means the `i`th box contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Two boxes are adjacent when their indices differ by exactly one.

Return an array `answer` of size `n`, where `answer[i]` is the minimum number of operations needed to move all the balls to the `i`th box.

Each answer is calculated using the initial arrangement of the boxes.

## 2. Examples

### Example 1

```text
Input:  boxes = "110"
Output: [1,1,3]
```

**Explanation:**

- To move all balls to box 0, move the ball from box 1 to box 0: 1 operation.
- To move all balls to box 1, move the ball from box 0 to box 1: 1 operation.
- To move all balls to box 2, move the ball from box 0 two positions and the ball from box 1 one position: 2 + 1 = 3 operations.

### Example 2

```text
Input:  boxes = "001011"
Output: [11,8,5,4,3,4]
```

## 3. Approach — Two Passes (Left and Right Contributions)

For every target box, each ball contributes its distance from that box to the total number of operations.

A direct solution could calculate the distance from every ball to every target box. That takes **O(n²)** time.

We can calculate all answers in **O(n)** using two passes.

### Pass 1: Left to Right

Track two variables:

- `balls`: Number of balls seen so far.
- `operations`: Number of moves those balls need to reach the current position.

At each index:

1. Add `operations` to `answer[i]`.
2. If the current box contains a ball, increment `balls`.
3. Add `balls` to `operations`, because every ball seen so far must move one step farther to reach the next box.

This pass calculates the contribution from the left.

### Pass 2: Right to Left

Reset `balls` and `operations`, then repeat the same process from right to left.

This calculates the contribution from the right. Add these costs to the existing answers.

## 4. Algorithm

1. Let `n = len(boxes)`.
2. Create `answer = [0] * n`.
3. Initialize `balls = 0` and `operations = 0`.
4. Traverse from left to right:
   - Add `operations` to `answer[i]`.
   - If `boxes[i] == '1'`, increment `balls`.
   - Update `operations += balls`.
5. Reset `balls = 0` and `operations = 0`.
6. Traverse from right to left using the same steps.
7. Return `answer`.

## 5. Python Solution

```python
class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        balls = 0
        operations = 0

        # Calculate the contribution from the left.
        for i in range(n):
            answer[i] += operations

            if boxes[i] == '1':
                balls += 1

            operations += balls

        balls = 0
        operations = 0

        # Calculate the contribution from the right.
        for i in range(n - 1, -1, -1):
            answer[i] += operations

            if boxes[i] == '1':
                balls += 1

            operations += balls

        return answer
```

## 6. Dry Run

Consider:

```python
boxes = "110"
```

Initially:

```text
answer = [0, 0, 0]
balls = 0
operations = 0
```

### Pass 1: Left to Right

| Index `i` | `boxes[i]` | Cost added to `answer[i]` | `balls` after processing box | `operations` after update |
|---:|:---:|---:|---:|---:|
| 0 | `'1'` | 0 | 1 | 1 |
| 1 | `'1'` | 1 | 2 | 3 |
| 2 | `'0'` | 3 | 2 | 5 |

After the first pass:

```text
answer = [0, 1, 3]
```

### Pass 2: Right to Left

Reset:

```text
balls = 0
operations = 0
```

| Index `i` | `boxes[i]` | Cost added to `answer[i]` | `balls` after processing box | `operations` after update |
|---:|:---:|---:|---:|---:|
| 2 | `'0'` | 0 | 0 | 0 |
| 1 | `'1'` | 0 | 1 | 1 |
| 0 | `'1'` | 1 | 2 | 3 |

Add the right-side contributions to the existing answers:

```text
answer = [1, 1, 3]
```

**Final output:**

```text
[1, 1, 3]
```

## 7. Why This Works

Moving a ball from position `j` to target position `i` requires exactly `abs(i - j)` adjacent moves.

Therefore, the answer for a target position is the sum of the distances from every ball to that position.

- The left-to-right pass counts the distances contributed by balls to the left.
- The right-to-left pass counts the distances contributed by balls to the right.
- A ball already in the target box contributes zero moves.

Together, the two passes count every ball's contribution to every target position.

## 8. Complexity Analysis

Let `n` be the length of `boxes`.

- **Time Complexity: O(n)** — We traverse the string twice. The total is O(2n) = O(n).
- **Auxiliary Space Complexity: O(1)** — Only a few variables are used apart from the output array.
- **Output Space Complexity: O(n)** — The `answer` array stores one result for each box.

## 9. Pattern

**Two Passes + Greedy + Running Count (Prefix/Suffix Contribution)**

Useful ideas:

- Count how many balls have been encountered.
- Track the total movement cost incrementally.
- Use a left-to-right pass for left-side contributions.
- Use a right-to-left pass for right-side contributions.
- Combine both contributions instead of recalculating every distance.

**Key update in each pass:**

```python
operations += balls
```

Each ball already encountered must move one additional step to reach the next box.

This reduces the straightforward O(n²) approach to an efficient **O(n)** solution.

<strong>Input:</strong> boxes = &quot;110&quot;
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;001011&quot;
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>
