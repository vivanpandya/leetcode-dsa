# 1394. Find Lucky Integer in an Array

- **LeetCode:** [Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/)
- **Difficulty:** Easy
- **Topics:** Array, Hash Table, Counting

## Problem Statement

Given an array of integers `arr`, a **lucky integer** is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer, return `-1`.

## Examples

### Example 1
**Input**
```text
arr = [2,2,3,4]
```
**Output**
```text
2
```
**Explanation:** The only lucky number in the array is `2` because its frequency is `2`.

### Example 2
**Input**
```text
arr = [1,2,2,3,3,3]
```
**Output**
```text
3
```
**Explanation:** `1`, `2`, and `3` are all lucky numbers. Return the largest one, `3`.

### Example 3
**Input**
```text
arr = [2,2,2,3,3]
```
**Output**
```text
-1
```
**Explanation:** There are no lucky numbers in the array.

## Constraints

- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`

## Approach

Use a hash map (frequency dictionary) to count how many times each integer appears. Then check each number: if its frequency equals the number itself, it is a lucky integer. Keep the largest lucky integer found. Initialize the answer to `-1`, so it remains `-1` if no lucky integer exists.

## Algorithm

1. Create an empty dictionary named `frequency`.
2. Traverse `arr` and increase the count of each value.
3. Initialize `answer = -1`.
4. Traverse the dictionary's values and frequencies.
5. If `num == count` and `num > answer`, update `answer = num`.
6. Return `answer`.

## Python Solution

```python
class Solution:
    def findLucky(self, arr):
        frequency = {}

        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        answer = -1

        for num, count in frequency.items():
            if num == count and num > answer:
                answer = num

        return answer
```

## Dry Run

For `arr = [1,2,2,3,3,3]`:

| Number | Frequency | Lucky? |
|---:|---:|---|
| 1 | 1 | Yes, because `1 == 1` |
| 2 | 2 | Yes, because `2 == 2` |
| 3 | 3 | Yes, because `3 == 3` |

The lucky integers are `1`, `2`, and `3`. The largest is `3`, so the function returns `3`.

## Why This Works

The dictionary records the exact frequency of every distinct number. A number is lucky precisely when its frequency equals its value. Checking all distinct numbers and keeping the largest one therefore returns the largest lucky integer. If none satisfies the condition, the initial answer `-1` is returned.

## Complexity Analysis

Let `n` be the length of `arr` and `k` be the number of distinct values.

- **Time Complexity:** `O(n)` average — building the frequency map takes `O(n)`, and checking its `k` entries takes `O(k)`, where `k <= n`.
- **Space Complexity:** `O(k)` — the dictionary stores one entry per distinct value; in the worst case, this is `O(n)`.

## Pattern

**Hash Map / Frequency Counting** — useful when a problem asks how often each value appears or requires comparing a value with its frequency.
