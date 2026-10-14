# LeetCode 2404 — Most Frequent Even Element

**Difficulty:** Easy  
**Topics:** Array, Hash Map, Frequency Counting  
**LeetCode:** https://leetcode.com/problems/most-frequent-even-element/

---

## 1. Question

Given an integer array `nums`, return the **most frequent even element**.

- If there is a tie, return the **smallest** even element.
- If there is no even element, return `-1`.

## 2. Examples

### Example 1

**Input**
```python
nums = [0, 1, 2, 2, 4, 4, 1]
```

**Output**
```python
2
```

**Explanation:** The even elements are `0`, `2`, and `4`. Both `2` and `4` appear twice, so return the smaller one, `2`.

### Example 2

**Input**
```python
nums = [4, 4, 4, 9, 2, 4]
```

**Output**
```python
4
```

**Explanation:** The number `4` is the most frequent even element.

### Example 3

**Input**
```python
nums = [29, 47, 21, 41, 13, 37, 25, 7]
```

**Output**
```python
-1
```

**Explanation:** There are no even elements in the array.

## 3. Approach

Use a **hash map** to count the frequency of each even number.

1. Traverse `nums`.
2. If a number is even, increase its count in the dictionary.
3. Check the frequencies and select the number with the highest frequency.
4. If two numbers have the same frequency, select the smaller number.
5. If the dictionary is empty, return `-1`.

## 4. Algorithm

1. Create an empty dictionary `count`.
2. For every `num` in `nums`:
   - If `num % 2 == 0`, update `count[num]`.
3. Set `result = -1` and `max_freq = 0`.
4. For each `num, freq` in `count`:
   - If `freq > max_freq`, update `max_freq` and `result`.
   - If `freq == max_freq` and `num < result`, update `result`.
5. Return `result`.

## 5. Python Code

```python
class Solution:
    def mostFrequentEven(self, nums):
        count = {}

        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1

        result = -1
        max_freq = 0

        for num, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                result = num
            elif freq == max_freq and num < result:
                result = num

        return result
```

## 6. Dry Run

**Input**
```python
nums = [0, 1, 2, 2, 4, 4, 1]
```

### Step 1: Count even elements

| Even Number | Frequency |
|---|---:|
| 0 | 1 |
| 2 | 2 |
| 4 | 2 |

### Step 2: Find the most frequent even element

- `0` has frequency `1`, so the current result becomes `0`.
- `2` has frequency `2`, which is higher, so the result becomes `2`.
- `4` also has frequency `2`. Since `2 < 4`, keep the result as `2`.

**Output**
```python
2
```

## 7. Complexity Analysis

Let `n` be the length of `nums` and `k` be the number of distinct even values.

- **Time Complexity:** `O(n)` — one pass counts even values and another checks the distinct values.
- **Space Complexity:** `O(k)` — the dictionary stores frequencies of distinct even values.

## 8. Pattern

**Hash Map + Frequency Counting + Tie-Breaking**

Use this pattern when you need to find the most frequent element while handling ties with an additional rule, such as choosing the smallest value.
