# 881. Boats to Save People

**Difficulty:** Medium  
**LeetCode:** https://leetcode.com/problems/boats-to-save-people/

---

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the `i`th person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of their weights is at most `limit`.

Return the **minimum number of boats** to carry every given person.

### Example 1

**Input:** `people = [1,2], limit = 3`  
**Output:** `1`  
**Explanation:** One boat carries people with weights `1` and `2`.

### Example 2

**Input:** `people = [3,2,2,1], limit = 3`  
**Output:** `3`  
**Explanation:** Three boats carry `(1, 2)`, `(2)`, and `(3)`.

### Example 3

**Input:** `people = [3,5,3,4], limit = 5`  
**Output:** `4`  
**Explanation:** Four boats carry `(3)`, `(3)`, `(4)`, and `(5)`.

### Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

---

## 1. Question

Find the minimum number of boats needed to carry everyone. Each boat can carry **at most two people**, and their combined weight cannot exceed `limit`.

## 2. Example

```text
Input:  people = [3,2,2,1], limit = 3
Output: 3
```

After sorting, `people = [1, 2, 2, 3]`.

- Person with weight `1` can share a boat with a person weighing `2`.
- The other person weighing `2` needs a separate boat.
- The person weighing `3` needs a separate boat.

Total: **3 boats**.

## 3. Approach

Use **Greedy + Two Pointers**.

1. Sort `people` in increasing order.
2. Set `left` to the lightest person and `right` to the heaviest person.
3. Every boat must carry the heaviest remaining person.
4. If the lightest and heaviest people fit together (`people[left] + people[right] <= limit`), put them in the same boat and move `left` forward.
5. Move `right` backward because the heaviest person has been carried.
6. Count one boat for each iteration, and continue until `left > right`.

If the lightest person cannot fit with the heaviest person, the heaviest person must go alone.

## 4. Algorithm

1. Sort the `people` array.
2. Initialize `left = 0`, `right = len(people) - 1`, and `boats = 0`.
3. While `left <= right`:
   - If `people[left] + people[right] <= limit`, increment `left` because both people can share a boat.
   - Decrement `right` because the heaviest remaining person is assigned to a boat.
   - Increment `boats`.
4. Return `boats`.

## 5. Code

```python
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats
```

## 6. Dry Run

For `people = [3,2,2,1]`, `limit = 3`, sort first:

`people = [1,2,2,3]`

| Step | `left` weight | `right` weight | Decision | Boats |
|---|---:|---:|---|---:|
| 1 | 1 | 3 | `1 + 3 > 3`; weight 3 goes alone | 1 |
| 2 | 1 | 2 | `1 + 2 <= 3`; both share a boat | 2 |
| 3 | 2 | 2 | One person remains; send them alone | 3 |

Return `3`.

## 7. Complexity

- **Time Complexity:** `O(n log n)` because sorting takes `O(n log n)` and the two-pointer scan takes `O(n)`.
- **Auxiliary Space:** `O(1)` auxiliary space for the two pointers and counter, excluding the sorting implementation's internal space. Python's `sort()` may use additional temporary memory.

## 8. Pattern

**Greedy + Two Pointers (after sorting)**

Use this pattern when pairing items under a limit and trying to minimize the number of groups or containers. Pair the heaviest remaining item with the lightest whenever they fit; otherwise, send the heaviest item alone.
