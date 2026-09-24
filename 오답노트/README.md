# 오답노트

Things I have to remember, one note per problem.
Solutions live in the repo root (`<번호>. <Title>.py`); the note here has the same name with `.md`.

New note: copy `_TEMPLATE.md`, then add a row below.

| # | Problem | 기억할 것 | Updated |
|---|---------|-----------|---------|
| 704 | [Binary Search](704.%20Binary%20Search.md) | Equality is checked inside the loop, so `idx` is ruled out — shrink with `idx ± 1`, never `r = idx` | Sep 6, 2026 |
| 78 | [Subsets](78.%20Subsets.md) | Append `subset.copy()` to `res` in the base case `i >= len(nums)` — a subset is complete only when every index has been decided | Sep 11, 2026 |
| 15 | [3Sum](15.%203Sum.md) | solve again | Sep 12, 2026 |
| 238 | [Product of Array Except Self](238.%20Product%20of%20Array%20Except%20Self.md) | solve again | Sep 14, 2026 |
| 424 | [Longest Repeating Character Replacement](424.%20Longest%20Repeating%20Character%20Replacement.md) | try again | Sep 16, 2026 |
| 286 | [Walls and Gates](286.%20Walls%20and%20Gates.md) | Mark a cell visited when you enqueue it, not when you pop it — otherwise the same coordinate gets pushed twice; solve again | Sep 16, 2026 |
| 567 | [Permutation in String](567.%20Permutation%20in%20String.md) | Use `ord(c) - ord("a")` for indexing; compare permutations with a 26-slot count array; solve again | Sep 17, 2026 |
| 739 | [Daily Temperatures](739.%20Daily%20Temperatures.md) | solve again | Sep 18, 2026 |
| 153 | [Find Minimum in Rotated Sorted Array](153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.md) | Be careful with the `if` conditions for binary search | Sep 20, 2026 |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md) | Use the BST property: both smaller → go left, both larger → go right, otherwise `root` is the LCA | Sep 21, 2026 |
| 35 | [Search Insert Position](35.%20Search%20Insert%20Position.md) | `while l < r` with `r = len(nums)`: loop ends at `l == r`, `l` is the insert slot; `r = mid` keeps the candidate, `l = mid + 1` guarantees progress | Sep 23, 2026 |
