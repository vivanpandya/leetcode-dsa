# 2215. Find the Difference of Two Arrays

**LeetCode:** [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/)  
**Difficulty:** Easy  
**Topics:** Array, Hash Table, Hash Set

---

## 1. Question

Given two 0-indexed integer arrays `nums1` and `nums2`, return a list `answer` of size `2` where:

- `answer[0]` contains all **distinct** integers in `nums1` that are **not present** in `nums2`.
- `answer[1]` contains all **distinct** integers in `nums2` that are **not present** in `nums1`.

The integers in the returned lists may be in any order.

### Example 1

**Input**
```text
nums1 = [1,2,3]
nums2 = [2,4,6]
```

**Output**
```text
[[1,3],[4,6]]
```

**Explanation:**
- `1` and `3` are in `nums1` but not in `nums2`.
- `4` and `6` are in `nums2` but not in `nums1`.

### Example 2

**Input**
```text
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
```

**Output**
```text
[[3],[]]
```

**Explanation:** `3` is in `nums1` but not in `nums2`. Every distinct value in `nums2` is present in `nums1`.

### Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

## 2. Approach

Use **hash sets** to efficiently check which values are present in each array.

1. Convert `nums1` and `nums2` into sets. This automatically removes duplicates.
2. Use set difference:
   - `set1 - set2` gives values only in `nums1`.
   - `set2 - set1` gives values only in `nums2`.
3. Convert the differences into lists and return them inside a list of size `2`.

## 3. Algorithm

1. Create `set1 = set(nums1)`.
2. Create `set2 = set(nums2)`.
3. Calculate `answer1 = list(set1 - set2)`.
4. Calculate `answer2 = list(set2 - set1)`.
5. Return `[answer1, answer2]`.

## 4. Code

```python
class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = list(set1 - set2)
        answer2 = list(set2 - set1)

        return [answer1, answer2]
```

## 5. Dry Run

**Input:**
```python
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
```

**Step 1: Convert the arrays to sets.**

```python
set1 = {1, 2, 3}
set2 = {1, 2}
```

Duplicates are removed automatically.

**Step 2: Find values only in `nums1`.**

```python
set1 - set2 = {3}
```

So, `answer1 = [3]`.

**Step 3: Find values only in `nums2`.**

```python
set2 - set1 = set()
```

So, `answer2 = []`.

**Output:**
```python
[[3], []]
```

## 6. Why This Works

A set stores each distinct value only once. The set difference `set1 - set2` contains exactly the values that belong to `set1` but not to `set2`. Similarly, `set2 - set1` contains exactly the values that belong to `set2` but not to `set1`. Returning both differences therefore satisfies the problem requirements.

## 7. Complexity Analysis

Let `n` be the length of `nums1` and `m` be the length of `nums2`.

- **Time Complexity:** `O(n + m)` average, to build the sets and calculate their differences.
- **Auxiliary Space Complexity:** `O(n + m)` for the sets and result lists.

## 8. Pattern

**Hash Set + Set Difference**

Use this pattern when you need to find distinct elements that appear in one collection but not another, remove duplicates, or compare membership between two arrays.
