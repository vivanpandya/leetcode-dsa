# 2364. Count Number of Bad Pairs

**LeetCode:** [2364. Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/)  
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Counting

---

## 1. Question

You are given a 0-indexed integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

Return the total number of bad pairs in `nums`.

### Example 1

**Input**
```text
nums = [4,1,3,3]
```

**Output**
```text
5
```

**Explanation:** All five possible pairs are bad, so the answer is `5`.

### Example 2

**Input**
```text
nums = [1,2,3,4,5]
```

**Output**
```text
0
```

**Explanation:** Every pair satisfies the good-pair condition, so there are no bad pairs.

### Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 2. Approach

Checking every pair would take `O(n²)` time, which is too slow for an array of up to `100,000` elements.

Instead, count **good pairs** and subtract them from the total number of pairs.

A pair `(i, j)` is good when:

`j - i == nums[j] - nums[i]`

Rearranging the equation:

`nums[i] - i == nums[j] - j`

Therefore, a pair is good if both indices have the same key:

`key = nums[i] - i`

Use a hash map to count how many times each key has appeared. When processing a new element, every previous occurrence of the same key forms one good pair with it.

The total number of index pairs is:

`n * (n - 1) // 2`

Finally:

`bad_pairs = total_pairs - good_pairs`

## 3. Algorithm

1. Set `n = len(nums)`.
2. Calculate `total_pairs = n * (n - 1) // 2`.
3. Initialize an empty dictionary `count` and set `good_pairs = 0`.
4. Traverse `nums` with each index `i` and value `num`.
5. Calculate `key = num - i`.
6. Add `count.get(key, 0)` to `good_pairs`.
7. Increase `count[key]` by one.
8. Return `total_pairs - good_pairs`.

## 4. Code

```python
class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        total_pairs = n * (n - 1) // 2

        count = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += count.get(key, 0)
            count[key] = count.get(key, 0) + 1

        return total_pairs - good_pairs
```

## 5. Dry Run

**Input:** `nums = [4,1,3,3]`

Total possible pairs:

`4 * (4 - 1) // 2 = 6`

| Index `i` | `nums[i]` | Key `nums[i] - i` | Previous matching keys | Good pairs so far |
|---:|---:|---:|---:|---:|
| 0 | 4 | 4 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 2 | 3 | 1 | 0 | 0 |
| 3 | 3 | 0 | 1 | 1 |

There is `1` good pair: `(1, 3)`.

`bad_pairs = 6 - 1 = 5`

**Output:** `5`

## 6. Why This Works

The good-pair condition is `j - i == nums[j] - nums[i]`. Rearranging gives `nums[i] - i == nums[j] - j`. Thus, two indices form a good pair exactly when their keys `nums[index] - index` are equal.

For every current index, the frequency of its key tells us how many earlier indices form a good pair with it. Each good pair is counted exactly once. Every index pair is either good or bad, so subtracting the number of good pairs from the total gives the correct number of bad pairs.

## 7. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)` average, because each element is processed once with average constant-time hash map operations.
- **Auxiliary Space Complexity:** `O(n)`, because the dictionary can store up to `n` distinct keys.

## 8. Pattern

**Hash Map + Counting Pairs + Mathematical Rearrangement**

When a pair condition contains both indices and values, try rearranging the equation to create a key for each element. Then count matching keys with a hash map instead of checking all pairs.
