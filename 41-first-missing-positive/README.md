# 41. First Missing Positive

**LeetCode:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)  
**Difficulty:** Hard  
**Topics:** Array, Hash Table, In-Place Index Placement

---

## 1. Question

Given an unsorted integer array `nums`, return the **smallest positive integer** that is not present in `nums`.

The algorithm must run in **O(n) time** and use **O(1) auxiliary space**.

### Examples

#### Example 1

**Input**
```text
nums = [1,2,0]
```

**Output**
```text
3
```

**Explanation:** The numbers `1` and `2` are present, so the smallest missing positive integer is `3`.

#### Example 2

**Input**
```text
nums = [3,4,-1,1]
```

**Output**
```text
2
```

**Explanation:** `1` is present, but `2` is missing.

#### Example 3

**Input**
```text
nums = [7,8,9,11,12]
```

**Output**
```text
1
```

**Explanation:** The smallest positive integer `1` is missing.

### Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## 2. Approach

Use **in-place index placement**. For an array of length `n`, the smallest missing positive must be in the range `1` to `n + 1`.

Each number `x` in the range `1 <= x <= n` belongs at index `x - 1`:

- `1` belongs at index `0`.
- `2` belongs at index `1`.
- `3` belongs at index `2`.

Rearrange the array so every valid number is placed at its correct index. Ignore values that are non-positive, greater than `n`, or duplicates that are already in the correct position.

Then scan the array. The first index `i` where `nums[i] != i + 1` gives the answer `i + 1`. If all positions match, return `n + 1`.

## 3. Algorithm

1. Set `n = len(nums)` and initialize `i = 0`.
2. While `i < n`:
   - If `nums[i]` is in the range `1` to `n`, and `nums[nums[i] - 1] != nums[i]`, swap the current value with the value at its correct index.
   - Otherwise, increment `i`.
3. Traverse the array from left to right.
4. If `nums[i] != i + 1`, return `i + 1`.
5. If every value is in the correct position, return `n + 1`.

## 4. Code

```python
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

## 5. Dry Run

**Input:** `nums = [3,4,-1,1]`

| Step | Operation | Array |
|---|---|---|
| Initial | Start | `[3,4,-1,1]` |
| 1 | Place `3` at index `2` | `[-1,4,3,1]` |
| 2 | `-1` is outside the valid range; move forward | `[-1,4,3,1]` |
| 3 | Place `4` at index `3` | `[-1,1,3,4]` |
| 4 | Place `1` at index `0` | `[1,-1,3,4]` |

Now scan the rearranged array:

- Index `0`: expected `1`, found `1`.
- Index `1`: expected `2`, found `-1`.

The first mismatch is at index `1`, so the answer is `1 + 1 = 2`.

**Output:** `2`

## 6. Why This Works

Only the values from `1` through `n` can determine whether one of the first `n` positive integers is missing. The algorithm places every such value at index `value - 1` whenever possible. Duplicate values cannot cause an endless loop because a swap occurs only when the destination does not already contain that value.

After placement, the first index `i` that does not contain `i + 1` identifies the smallest missing positive integer. If all `n` positions contain their expected values, then all integers from `1` through `n` exist, so the answer is `n + 1`.

## 7. Complexity Analysis

- **Time Complexity:** `O(n)`. Each successful swap places a value in its correct position, and there are at most `O(n)` such placements. The final scan is also `O(n)`.
- **Auxiliary Space Complexity:** `O(1)`. The algorithm rearranges `nums` in place and uses only a constant number of extra variables.

## 8. Pattern

**In-Place Index Placement / Cyclic Sort**

Use this pattern for problems involving missing positive integers, values in a known range, or placing numbers at indices corresponding to their values.
