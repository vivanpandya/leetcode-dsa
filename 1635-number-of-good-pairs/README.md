# 1512. Number of Good Pairs

**LeetCode:** [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)  
**Difficulty:** Easy  
**Topics:** Array, Hash Table, Counting

---

## 1. Question

Given an array of integers `nums`, return the number of **good pairs**.

A pair `(i, j)` is called good if:

- `nums[i] == nums[j]`
- `i < j`

### Example 1

**Input**
```text
nums = [1,2,3,1,1,3]
```

**Output**
```text
4
```

**Explanation:** The four good pairs are `(0,3)`, `(0,4)`, `(3,4)`, and `(2,5)`.

### Example 2

**Input**
```text
nums = [1,1,1,1]
```

**Output**
```text
6
```

**Explanation:** Every pair is good.

### Example 3

**Input**
```text
nums = [1,2,3]
```

**Output**
```text
0
```

**Explanation:** No number appears more than once, so there are no good pairs.

### Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## 2. Approach

Use a **hash map** to track how many times each number has appeared.

When the current number has appeared `k` times before, it forms `k` new good pairs with those previous occurrences. Add `k` to the answer, then increase the frequency of the current number.

This counts each good pair exactly once without checking every possible pair.

## 3. Algorithm

1. Create an empty dictionary called `count`.
2. Initialize `pairs = 0`.
3. Traverse each number `num` in `nums`.
4. Add its previous frequency to `pairs` using `count.get(num, 0)`.
5. Increase its frequency in the dictionary by one.
6. Return `pairs`.

## 4. Code

```python
class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        pairs = 0

        for num in nums:
            pairs += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return pairs
```

## 5. Dry Run

**Input:** `nums = [1,2,3,1,1,3]`

| Number | Previous Frequency | Pairs Added | Total Pairs |
|---|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 3 |
| 3 | 1 | 1 | 4 |

**Output:** `4`

## 6. Why This Works

For each number, every occurrence that appeared earlier creates exactly one good pair with the current occurrence. The dictionary stores the number of earlier occurrences, so adding that frequency counts all new pairs formed by the current number. Each pair is counted once, when its second index is visited.

## 7. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)` average, because each number requires constant-time dictionary operations.
- **Auxiliary Space Complexity:** `O(k)`, where `k` is the number of distinct values in `nums` (at most `O(n)`).

## 8. Pattern

**Hash Map + Frequency Counting**

Use this pattern when counting equal-value pairs or when each new element can form pairs with previously seen elements.
