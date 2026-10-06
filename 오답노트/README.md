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
| 45 | [Jump Game II](45.%20Jump%20Game%20II.md) | See the solution — BFS greedy, updating the window `[l, r]` → `[r + 1, farthest]` per jump | Sep 24, 2026 |
| 134 | [Gas Station](134.%20Gas%20Station.md) | Greedy: 누적합이 음수가 되면 현재 출발점부터 `i`까지 제외하고 `i + 1`에서 다시 시작; 전체 합이 음수면 불가능 | Sep 28, 2026 |
| 300 | [Longest Increasing Subsequence](300.%20Longest%20Increasing%20Subsequence.md) | DP: `lis[i]`는 `i`에서 시작하는 최장 길이; 오른쪽부터 `1 + lis[j]`로 갱신; 다시 풀기 | Sep 29, 2026 |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.md) | Preorder의 첫 값이 root; inorder에서 왼쪽 크기를 구해 preorder를 분할; slice마다 index는 0부터 다시 시작 | Oct 1, 2026 |
| 416 | [Partition Equal Subset Sum](416.%20Partition%20Equal%20Subset%20Sum.md) | 백트래킹 대신 부분합 DP (0/1 Knapsack); 가능한 합을 set에 저장하고 이전 집합으로 다음 집합을 갱신 | Oct 5, 2026 |
| 435 | [Non-overlapping Intervals](435.%20Non-overlapping%20Intervals.md) | Greedy: 겹치면 끝점이 작은 구간 유지; 겹침은 `<`; 안 겹치면 `prev` 갱신; 마지막 구간까지 확인 | Oct 5, 2026 |
| 560 | [Subarray Sum Equals K](560.%20Subarray%20Sum%20Equals%20K.md) | 누적합 + 해시맵: 이전 `prefix - k`의 등장 횟수를 더한 뒤 현재 누적합 등록; `{0: 1}`로 시작 | Oct 5, 2026 |
| 694 | [Number of Distinct Islands](694.%20Number%20of%20Distinct%20Islands.md) | DFS 경로에 `"b"`로 복귀를 기록해야 서로 다른 가지 구조를 구분할 수 있다 | Oct 6, 2026 |
| 785 | [Is Graph Bipartite?](785.%20Is%20Graph%20Bipartite%3F.md) | Neighbors must be on different teams: alternate `1` / `-1` with BFS, reject same-team edges, and check every connected component | Oct 6, 2026 |
| 743 | [Network Delay Time](743.%20Network%20Delay%20Time.md) | Shortest paths from `k`: use Dijkstra; return the maximum shortest time, or `-1` if any node is unreachable | Oct 6, 2026 |
