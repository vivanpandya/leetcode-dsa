# 697. Degree of an Array

**LeetCode:** [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)  
**Difficulty:** Easy  
**Topics:** Array, Hash Map

---

## 1. Question

Given a non-empty array of non-negative integers `nums`, the **degree** of the array is the maximum frequency of any one of its elements.

Find the smallest possible length of a **contiguous subarray** of `nums` that has the same degree as the original array.

### Examples

#### Example 1

**Input**
```text
nums = [1,2,2,3,1]
```

**Output**
```text
2
```

**Explanation:** The degree is `2` because both `1` and `2` appear twice. The shortest subarray with the same degree is `[2,2]`, whose length is `2`.

#### Example 2

**Input**
```text
nums = [1,2,2,3,1,4,2]
```

**Output**
```text
6
```

**Explanation:** The degree is `3` because `2` appears three times. The shortest subarray containing all three occurrences of `2` is `[2,2,3,1,4,2]`, whose length is `6`.

### Constraints

- `1 <= nums.length <= 50,000`
- `0 <= nums[i] <= 49,999`

---

## 2. Approach

Use three hash maps (Python dictionaries) to record information about every number:

- `count[num]`: frequency of `num`.
- `first[num]`: index where `num` first appears.
- `last[num]`: index where `num` most recently appears.

First, traverse the array to build these dictionaries. The maximum value in `count` is the array's degree.

For every number whose frequency equals the degree, the shortest subarray containing all its occurrences starts at its first occurrence and ends at its last occurrence. Its length is:

`last[num] - first[num] + 1`

Return the minimum such length.

## 3. Algorithm

1. Initialize `count`, `first`, and `last` as empty dictionaries.
2. Traverse `nums` with `enumerate()`.
3. Increment `count[num]` for each number.
4. If `num` has no first index yet, save the current index in `first[num]`.
5. Update `last[num]` to the current index.
6. Find the maximum frequency in `count`; this is the degree.
7. For every number whose frequency equals the degree, calculate `last[num] - first[num] + 1`.
8. Return the minimum calculated length.

## 4. Code

```python
class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1

            if num not in first:
                first[num] = i

            last[num] = i

        degree = max(count.values())
        shortest = len(nums)

        for num, freq in count.items():
            if freq == degree:
                length = last[num] - first[num] + 1
                shortest = min(shortest, length)

        return shortest
```

## 5. Dry Run

For `nums = [1, 2, 2, 3, 1]`, the recorded information is:

| Number | Frequency | First index | Last index |
|---|---:|---:|---:|
| `1` | 2 | 0 | 4 |
| `2` | 2 | 1 | 2 |
| `3` | 1 | 3 | 3 |

The degree is `2`.

- For `1`: `last[1] - first[1] + 1 = 4 - 0 + 1 = 5`.
- For `2`: `last[2] - first[2] + 1 = 2 - 1 + 1 = 2`.

The minimum length is `2`.

**Output:** `2`

## 6. Why This Works

A subarray has the same degree as the original array only if it contains every occurrence of at least one number whose frequency equals the original degree. To include all occurrences of a particular number, a contiguous subarray must extend from that number's first occurrence to its last occurrence. Therefore, `last[num] - first[num] + 1` is the shortest possible span for that number. Taking the minimum span among all numbers with the maximum frequency gives the answer.

## 7. Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)` average. We traverse the array once to build the dictionaries and once over the distinct numbers to find the shortest span.
- **Auxiliary Space Complexity:** `O(n)` because the dictionaries can store information for every distinct number.

## 8. Pattern

**Hash Map + First and Last Occurrence Tracking**

Use this pattern when you need to find the shortest contiguous subarray that includes all occurrences of an element with maximum frequency.
