# LeetCode 2225 — Find Players With Zero or One Losses

**Difficulty:** Medium  
**Topics:** Hash Map, Set, Sorting  
**LeetCode:** https://leetcode.com/problems/find-players-with-zero-or-one-losses/

---

## 1. Question

You are given an integer array `matches`, where `matches[i] = [winner_i, loser_i]` means that `winner_i` defeated `loser_i`.

Return a list `answer` of size `2`:
- `answer[0]`: All players who have **not lost any matches**.
- `answer[1]`: All players who have lost **exactly one match**.

Both lists must be sorted in increasing order. Only include players who have played at least one match.

## 2. Examples

### Example 1

**Input**
```python
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
```

**Output**
```python
[[1,2,10],[4,5,7,8]]
```

**Explanation:** Players `1`, `2`, and `10` have zero losses. Players `4`, `5`, `7`, and `8` have exactly one loss. Players `3`, `6`, and `9` have two losses.

### Example 2

**Input**
```python
matches = [[2,3],[1,3],[5,4],[6,4]]
```

**Output**
```python
[[1,2,5,6],[]]
```

**Explanation:** Players `1`, `2`, `5`, and `6` have zero losses. Players `3` and `4` each have two losses, so nobody has exactly one loss.

## 3. Approach

Use a **hash map** to count each player's losses and a **set** to track every player who participated.

For each match `[winner, loser]`:
1. Add both players to the set.
2. Increase the loser's loss count.

After processing all matches:
- Players with zero losses go into `zero_losses`.
- Players with exactly one loss go into `one_loss`.
- Sort both lists in increasing order.

## 4. Algorithm

1. Create an empty dictionary `losses` and an empty set `players`.
2. For each `[winner, loser]` in `matches`:
   - Add both players to `players`.
   - Increment `losses[loser]`.
3. Create empty lists `zero_losses` and `one_loss`.
4. For every player:
   - If `losses.get(player, 0) == 0`, append them to `zero_losses`.
   - If `losses.get(player, 0) == 1`, append them to `one_loss`.
5. Sort both lists.
6. Return `[zero_losses, one_loss]`.

## 5. Python Code

```python
class Solution:
    def findWinners(self, matches):
        losses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] = losses.get(loser, 0) + 1

        zero_losses = []
        one_loss = []

        for player in players:
            loss_count = losses.get(player, 0)

            if loss_count == 0:
                zero_losses.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()

        return [zero_losses, one_loss]
```

## 6. Dry Run

Consider:

```python
matches = [[1,3], [2,3], [3,6], [5,6]]
```

### Step 1: Count losses

| Match | Winner | Loser | Updated loss count |
|---|---:|---:|---|
| `[1,3]` | 1 | 3 | Player 3 → 1 |
| `[2,3]` | 2 | 3 | Player 3 → 2 |
| `[3,6]` | 3 | 6 | Player 6 → 1 |
| `[5,6]` | 5 | 6 | Player 6 → 2 |

At the end:
- Players: `{1, 2, 3, 5, 6}`
- Loss counts: `{3: 2, 6: 2}`

### Step 2: Classify players

| Player | Losses | Category |
|---|---:|---|
| 1 | 0 | Zero losses |
| 2 | 0 | Zero losses |
| 3 | 2 | Excluded |
| 5 | 0 | Zero losses |
| 6 | 2 | Excluded |

**Output**
```python
[[1, 2, 5], []]
```

## 7. Complexity Analysis

Let `n` be the number of matches and `p` be the number of distinct players.

- **Time Complexity:** `O(n + p log p)` — count losses and collect players in expected `O(n)` time, classify in `O(p)`, and sort the output lists in `O(p log p)`.
- **Space Complexity:** `O(p)` — store distinct players, loss counts, and the output lists.

## 8. Pattern

**Hash Map + Set + Sorting**

Use this pattern when you need to track entities, count events for each entity, classify them by their counts, and return sorted groups.
