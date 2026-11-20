# 4. Median of Two Sorted Arrays

[LeetCode Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/)

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Topics
- Array
- Binary Search
- Divide and Conquer

---

## 1. Problem Statement

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n`, return the median of the two sorted arrays.

The overall runtime complexity should be `O(log(m + n))`.

The median is:
- The middle element when the total number of elements is odd.
- The average of the two middle elements when the total number of elements is even.

### Example 1

**Input:**
```python
nums1 = [1, 3]
nums2 = [2]
```

**Output:**
```python
2.0
```

**Explanation:**

The combined sorted array is `[1, 2, 3]`. The middle element is `2`.

### Example 2

**Input:**
```python
nums1 = [1, 2]
nums2 = [3, 4]
```

**Output:**
```python
2.5
```

**Explanation:**

The combined sorted array is `[1, 2, 3, 4]`.

The median is `(2 + 3) / 2 = 2.5`.

### Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## 2. Approach: Binary Search on Partition

A simple approach is to merge both arrays and sort them. However, that takes more than the required logarithmic time.

The optimal approach uses **Binary Search on Partition**.

The main idea is to divide both sorted arrays into two halves:

- Left half: contains the smaller elements.
- Right half: contains the larger elements.

We need a valid partition where:

```text
max(left half) <= min(right half)
```

The left half must contain:
- The same number of elements as the right half when the total length is even.
- One extra element when the total length is odd.

### Step 1: Binary search the smaller array

```python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

This keeps the binary search range as small as possible and ensures the partition in the second array remains valid.

### Step 2: Initialize the search boundaries

```python
m, n = len(nums1), len(nums2)
low, high = 0, m
```

We search for how many elements from `nums1` should be placed in the left half.

### Step 3: Calculate both partition positions

```python
i = (low + high) // 2
j = (m + n + 1) // 2 - i
```

- `i` is the number of elements taken from `nums1` for the left half.
- `j` is the number of elements taken from `nums2` for the left half.

The `+1` makes the left half contain one extra element when the total length is odd.

### Step 4: Find the four boundary values

```python
maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
minRight1 = float('inf') if i == m else nums1[i]

maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
minRight2 = float('inf') if j == n else nums2[j]
```

These variables represent:
- `maxLeft1`: largest element on the left side of `nums1`.
- `minRight1`: smallest element on the right side of `nums1`.
- `maxLeft2`: largest element on the left side of `nums2`.
- `minRight2`: smallest element on the right side of `nums2`.

Infinity handles partitions at the beginning or end of an array without causing index errors.

### Step 5: Check whether the partition is valid

```python
maxLeft1 <= minRight2 and maxLeft2 <= minRight1
```

If both conditions are true, every element in the combined left half is less than or equal to every element in the combined right half.

### Step 6: Calculate the median

If the total length is even:

```python
(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
```

If the total length is odd:

```python
max(maxLeft1, maxLeft2)
```

### Step 7: Adjust binary search

If the partition is not valid:

- If `maxLeft1 > minRight2`, move the partition in `nums1` to the left.
- Otherwise, move the partition in `nums1` to the right.

---

## 3. Algorithm

1. If `nums1` is longer than `nums2`, swap the arrays.
2. Store their lengths in `m` and `n`.
3. Initialize `low = 0` and `high = m`.
4. While `low <= high`:
   1. Calculate `i = (low + high) // 2`.
   2. Calculate `j = (m + n + 1) // 2 - i`.
   3. Find `maxLeft1`, `minRight1`, `maxLeft2`, and `minRight2`.
   4. If `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`:
      - If the total length is even, return the average of the maximum left value and minimum right value.
      - Otherwise, return the maximum left value.
   5. If `maxLeft1 > minRight2`, set `high = i - 1`.
   6. Otherwise, set `low = i + 1`.
5. Return the median when a valid partition is found.

---

## 4. Python Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (
                        max(maxLeft1, maxLeft2) +
                        min(minRight1, minRight2)
                    ) / 2.0
                else:
                    return float(max(maxLeft1, maxLeft2))

            elif maxLeft1 > minRight2:
                high = i - 1
            else:
                low = i + 1
```

---

## 5. Dry Run

**Input:**

```python
nums1 = [1, 2]
nums2 = [3, 4]
```

Both arrays are already sorted, and `nums1` is the smaller array.

```text
m = 2
n = 2
low = 0
high = 2
```

### First iteration

```text
i = (0 + 2) // 2 = 1
j = (2 + 2 + 1) // 2 - 1 = 1
```

Boundary values:

```text
maxLeft1 = nums1[0] = 1
minRight1 = nums1[1] = 2

maxLeft2 = nums2[0] = 3
minRight2 = nums2[1] = 4
```

Check the partition:

```text
maxLeft1 <= minRight2
1 <= 4  -> True

maxLeft2 <= minRight1
3 <= 2  -> False
```

The partition is invalid. Since `maxLeft2` is greater than `minRight1`, we need to move the partition in `nums1` to the right:

```python
low = i + 1
low = 2
```

### Second iteration

```text
i = (2 + 2) // 2 = 2
j = (2 + 2 + 1) // 2 - 2 = 0
```

Boundary values:

```text
maxLeft1 = nums1[1] = 2
minRight1 = inf

maxLeft2 = -inf
minRight2 = nums2[0] = 3
```

Check the partition:

```text
maxLeft1 <= minRight2
2 <= 3  -> True

maxLeft2 <= minRight1
-inf <= inf  -> True
```

The partition is valid.

The total length is even, so:

```text
median = (max(2, -inf) + min(inf, 3)) / 2
       = (2 + 3) / 2
       = 2.5
```

**Output:**
```python
2.5
```

---

## 6. Why This Works

Both input arrays are already sorted. We do not need to merge them to find the middle elements.

Instead, binary search finds a partition that places the correct number of elements on the left and right sides.

When the partition is valid:

```text
max(left half) <= min(right half)
```

Therefore:
- For an odd total length, the largest element in the left half is the median.
- For an even total length, the median is the average of the largest left element and smallest right element.

Moving the partition left or right based on the boundary comparisons lets binary search find the valid partition efficiently.

---

## 7. Complexity Analysis

Let:
- `m` = length of `nums1`.
- `n` = length of `nums2`.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(log(min(m, n)))` | Binary search is performed on the smaller array. Each iteration performs constant-time operations. |
| Auxiliary Space | `O(1)` | Only a fixed number of variables are used. |

The required `O(log(m + n))` time bound is satisfied because `log(min(m, n))` is no greater than `log(m + n)`.

---

## 8. Pattern and Related Problems

**Pattern:** Binary Search on Partition.

Recognize this pattern when:
- Two sorted arrays need to be combined logically.
- You need a median or a middle boundary.
- Merging the arrays would be too slow.
- You can binary search a partition and compare its boundary elements.

Related LeetCode problems:

| Problem | LeetCode Number | Pattern |
|---|---:|---|
| Find First and Last Position of Element in Sorted Array | 34 | Binary Search |
| Search in Rotated Sorted Array | 33 | Modified Binary Search |
| Find Minimum in Rotated Sorted Array | 153 | Binary Search |
| Median of Two Sorted Arrays | 4 | Binary Search on Partition |

### Important points to remember

```python
j = (m + n + 1) // 2 - i
```

The `+1` ensures the left half gets the extra element when the total length is odd.

```python
maxLeft = float('-inf')
minRight = float('inf')
```

Use negative infinity for an empty left side and positive infinity for an empty right side.

```python
maxLeft1 <= minRight2 and maxLeft2 <= minRight1
```

Both conditions must be true for a valid partition.
