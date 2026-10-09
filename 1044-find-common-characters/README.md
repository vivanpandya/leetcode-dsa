# 1002. Find Common Characters

**Difficulty:** Easy

**Topics:** Array, Hash Table, String

**LeetCode:** [Find Common Characters](https://leetcode.com/problems/find-common-characters/)

---

## Problem Statement

Given a string array `words`, return an array of all characters that appear in every string within `words`, including duplicates.

You may return the answer in any order.

### Example 1

**Input:**
```python
words = ["bella", "label", "roller"]
```

**Output:**
```python
["e", "l", "l"]
```

### Example 2

**Input:**
```python
words = ["cool", "lock", "cook"]
```

**Output:**
```python
["c", "o"]
```

### Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

---

## Approach

We use **Hash Maps (Dictionaries)** to count the frequency of each character.

1. Count the frequency of every character in the first word. This becomes our initial set of common characters.
2. For each remaining word, count the frequency of its characters in a separate dictionary.
3. Update each character's frequency to the minimum of its current frequency and its frequency in the current word.
4. Build the result by adding each character as many times as its final frequency.

The minimum frequency ensures that we include only characters common to every word, including duplicates.

## Algorithm

1. Create an empty dictionary called `common`.
2. Count the characters in the first word and store their frequencies in `common`.
3. Iterate through the remaining words:
   - Create an empty dictionary called `count`.
   - Count the frequency of every character in the current word.
   - Update each character's frequency in `common` using the minimum of the two frequencies. If a character is missing from the current word, its frequency becomes zero.
4. Create an empty list called `result`.
5. Add each character to `result` according to its final frequency.
6. Return `result`.

## Code

```python
class Solution:
    def commonChars(self, words):
        common = {}

        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1

        for word in words[1:]:
            count = {}

            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            for ch in common:
                common[ch] = min(common[ch], count.get(ch, 0))

        result = []

        for ch, freq in common.items():
            for _ in range(freq):
                result.append(ch)

        return result
```

## Example Walkthrough

**Input:**
```python
words = ["bella", "label", "roller"]
```

**Step 1: Count characters in `"bella"`**

```python
common = {
    'b': 1,
    'e': 1,
    'l': 2,
    'a': 1
}
```

**Step 2: Process `"label"`**

Character frequencies are updated to their minimum values in both words.

```python
common = {
    'b': 1,
    'e': 1,
    'l': 2,
    'a': 1
}
```

**Step 3: Process `"roller"`**

The character `'b'` and `'a'` are absent, so their frequencies become zero. The character `'l'` appears twice, and `'e'` appears once.

```python
common = {
    'b': 0,
    'e': 1,
    'l': 2,
    'a': 0
}
```

**Final Output:**
```python
["e", "l", "l"]
```

## Why This Works

A character can appear in the answer only as many times as it appears in the word where its frequency is lowest.

By repeatedly taking the minimum frequency across all words, we guarantee that every character in the result appears in every input string. Characters with a frequency of zero are excluded, while duplicates are preserved.

## Time Complexity

**O(n × m)**

Where:
- `n` is the number of words.
- `m` is the maximum length of a word.

We process each word and count its characters. Because the input contains only lowercase English letters, the frequency dictionary has at most 26 distinct keys, so updating the common frequencies takes constant time per word.

## Space Complexity

**O(1) auxiliary space**, excluding the output.

Since the input contains only lowercase English letters, each frequency dictionary can contain at most 26 distinct characters. The output list requires additional space proportional to the number of returned characters.

## Pattern

**Hash Map + Frequency Counting + Minimum Frequency**

This pattern is useful for problems involving:
- Common characters across multiple strings.
- Character frequency comparisons.
- Finding repeated elements shared by multiple collections.
- Identifying the minimum occurrence count across multiple inputs.
