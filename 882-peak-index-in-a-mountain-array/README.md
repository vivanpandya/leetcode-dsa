# 852. Peak Index in a Mountain Array

[LeetCode Problem](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)

## Topics

- Array
- Binary Search

---

## 1. Problem Statement

You are given an integer **mountain array** `arr` of length `n`.

A mountain array first increases to a **peak element** and then decreases.

Return the **index of the peak element**.

You must solve the problem in `O(log n)` time.

### Example 1

**Input:**
```python
arr = [0, 1, 0]
```

**Output:**
```python
1
```

### Example 2

**Input:**
```python
arr = [0, 2, 1, 0]
```

**Output:**
```python
1
```

### Example 3

**Input:**
```python
arr = [0, 10, 5, 2]
```

**Output:**
```python
1
```

### Constraints

- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a mountain array.

---

## 2. Approach: Binary Search (Peak Finding)

A mountain array has two parts:

1. **Increasing part:** Each element is greater than the previous element.
2. **Decreasing part:** Each element is smaller than the previous element.

The peak is the point where the array changes from increasing to decreasing.

We can find this point using binary search.

### Key Observation

Compare the middle element with the next element:

```python
arr[mid] < arr[mid + 1]
```

There are two possibilities:

**Case 1: We are on the increasing side**

If:

```python
arr[mid] < arr[mid + 1]
```

The next element is greater, so the peak must be to the right.

```python
left = mid + 1
```

**Case 2: We are on the decreasing side or at the peak**

If:

```python
arr[mid] > arr[mid + 1]
```

The peak is either at `mid` or somewhere to its left.

```python
right = mid
```

We use `right = mid`, not `mid - 1`, because `mid` itself could be the peak.

Continue until `left == right`. That index is the peak.

---

## 3. Algorithm

1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Run a loop while `left < right`.
3. Calculate the middle index:
   ```python
   mid = (left + right) // 2
   ```
4. Compare `arr[mid]` with `arr[mid + 1]`.
   - If `arr[mid] < arr[mid + 1]`, move right: `left = mid + 1`.
   - Otherwise, keep `mid` as a possible peak: `right = mid`.
5. When the loop ends, `left` and `right` point to the same index.
6. Return `left`.

---

## 4. Python Code

```python
class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
```

---

## 5. Dry Run

**Input:**

```python
arr = [0, 10, 5, 2]
```

Initially:

```python
left = 0
right = 3
```

### Iteration 1

Calculate `mid`:

```python
mid = (0 + 3) // 2
mid = 1
```

Compare the middle element with the next element:

```python
arr[mid]     = 10
arr[mid + 1] = 5
```

Check:

```python
10 < 5  # False
```

We are at the peak or on the decreasing side. Keep `mid` in the search range:

```python
right = mid
right = 1
```

Now:

```python
left = 0
right = 1
```

### Iteration 2

Calculate `mid`:

```python
mid = (0 + 1) // 2
mid = 0
```

Compare:

```python
arr[mid]     = 0
arr[mid + 1] = 10
```

Check:

```python
0 < 10  # True
```

We are on the increasing side, so the peak must be to the right:

```python
left = mid + 1
left = 1
```

Now:

```python
left = 1
right = 1
```

The loop ends because `left == right`.

### Final Output

```python
return 1
```

The peak element is `10`, at index `1`.

---

## 6. Why This Works

The mountain array increases before the peak and decreases after it.

- When `arr[mid] < arr[mid + 1]`, we are before the peak. Therefore, the peak must be to the right of `mid`.
- When `arr[mid] > arr[mid + 1]`, we are at the peak or after it. Therefore, the peak must be at `mid` or to its left.

Each comparison removes approximately half of the remaining search range.

The loop finishes when only one possible index remains. Since the array is guaranteed to be a mountain array, that index is its peak.

---

## 7. Complexity Analysis

Let `n` be the length of `arr`.

| Operation | Complexity |
|---|---|
| Initialize pointers | `O(1)` |
| Binary search | `O(log n)` |
| Return the peak index | `O(1)` |

**Time Complexity:**

```text
O(log n)
```

**Space Complexity:**

```text
O(1)
```

Only three variables (`left`, `right`, and `mid`) are used. The input array is not modified.

---

## 8. Pattern and Related Problems

**Pattern: Binary Search – Peak Finding**

Recognize this pattern when:
- The array increases and then decreases.
- You need to find the maximum or peak position.
- Comparing a middle element with its neighbor tells you which side contains the peak.

### Related LeetCode Problems

| Problem | Number | Pattern |
|---|---:|---|
| Find Peak Element | 162 | Binary Search – Peak Finding |
| Find Minimum in Rotated Sorted Array | 153 | Modified Binary Search |
| Search in Rotated Sorted Array | 33 | Modified Binary Search |
| H-Index II | 275 | Binary Search on Monotonic Condition |
| Peak Index in a Mountain Array | 852 | Binary Search – Peak Finding |

### Important Lines to Remember

**If the slope is increasing, move right:**

```python
if arr[mid] < arr[mid + 1]:
    left = mid + 1
```

**Otherwise, keep `mid` and search left:**

```python
else:
    right = mid
```

**Return the peak index:**

```python
return left
```

### Important Difference: LeetCode 852 vs. LeetCode 162

Both problems use binary search to find a peak.

- **LeetCode 852 – Peak Index in a Mountain Array:** The input is guaranteed to be a mountain array, so it has one peak.
- **LeetCode 162 – Find Peak Element:** The array can contain multiple peaks, and returning any one of them is allowed.

The same binary-search comparison can be used for both problems.
