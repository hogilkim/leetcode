# Google Interview LeetCode Checklist

66 unique LeetCode problems matched to the interview notes and supplied report summary, grouped by LeetCode difficulty. New additions start unchecked.

- **Exact:** the same core problem, or explicitly linked in the notes.
- **Variant:** a close match with changed rules or output.
- **Related:** practice for part of the interview problem; not a direct equivalent.
- **Reported:** explicitly named in the supplied 2026 report summary; original reports have not been independently verified.

The difficulty applies to the linked LeetCode problem, not necessarily to the interview variation. Unmapped custom questions are excluded.

## Easy (8)

- [o] [278. First Bad Version](https://leetcode.com/problems/first-bad-version/) — **Exact:** first bad commit/version through an API.
- [ ] [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) — **Reported:** explicitly named in the supplied 2026 report summary.
- [ ] [359. Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) — **Exact:** ordinary 10-second logging suppression. **Variant:** suppressing both duplicates requires delayed output and retrospective invalidation.
- [o] [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) — **Variant:** maximum-product selection with negative numbers; LeetCode fixes K = 3.
- [ ] [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) — **Related:** bounded top-K heap for movie ratings; similarity-graph traversal is separate.
- [ ] [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/) — **Exact:** repeatedly remove adjacent copies of a letter with opposite cases.
- [ ] [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) — **Variant:** S→T reachability; remove defective routers or model traversable grid cells as vertices.
- [ ] [2506. Count Pairs Of Similar Strings](https://leetcode.com/problems/count-pairs-of-similar-strings/) — **Variant:** magical pairs have equal distinct-character sets; the interview counts triplets defining adjacent substrings within one string instead of pairs from a given word array. See the Round 1 practice notes below.

## Medium (40)

- [o] [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — **Variant:** first/last character occurrences in a sorted string; additionally filter characters occurring more than twice.
- [o] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — **Exact** if the Kadane question asks for standard maximum subarray sum.
- [o] [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) — **Exact/variant:** merge overlapping intervals; the interview variation was unspecified.
- [o] [91. Decode Ways](https://leetcode.com/problems/decode-ways/) — **Exact:** count interpretations under the 1–26 alphabet mapping.
- [o] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — **Reported:** explicitly named in the supplied 2026 report summary.
- [o] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) — **Related:** distinguish enclosed water from water connected to the outside ocean.
- [o] [146. LRU Cache](https://leetcode.com/problems/lru-cache/) — **Related:** cache implementation; distributed-cache architecture requires separate system design.
- [o] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) — **Related:** four-directional grid traversal and component counting; also a foundation for counting islands in a binary tree.
- [o] [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — **Variant:** detect cyclic task dependencies; identifying every node actually in a cycle requires additional work.
- [o] [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) — **Related:** minimum machines/resources when execution intervals are fixed.
- [o] [351. Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) — **Exact:** explicitly linked in the interview notes.
- [o] [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — **Related:** practice for the unspecified knapsack DP variation.
- [o] [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — **Related:** greedy interval selection.
- [o] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — **Related:** prefix sums with a hash map; a possible match for the unspecified hashmap optimization.
- [o] [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) — **Related:** minimum completion time with repeated-task cooldowns.
- [o] [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) — **Related:** conditional character choices that permit balanced parentheses; does not model digit-controlled deletions.
- [o] [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) — **Exact:** longest tree path whose nodes have the same value.
- [o] [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) — **Related:** aggregate counts and return top N; adapt keys to users and counts to total words.
- [o] [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) — **Exact:** translations count as identical shapes; rotations and reflections remain distinct.
- [ ] [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) — **Variant:** group items transitively through shared attributes; emails serve as attributes.
- [o] [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) — **Variant:** weighted shortest paths; choose the nearest favorite city instead of the time to reach every node.
- [ ] [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) — **Related:** heap-based selection while avoiding consecutive identical ads.
- [o] [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) — **Related:** alternating colors across tree layers; the interview has fixed colors and a binary-root constraint.
- [ ] [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) — **Related:** dictionary subsequence checking; requiring every length≥3 subsequence to appear is stronger.
- [o] [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) — **Exact:** partition into consecutive groups while handling duplicates.
- [o] [939. Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) — **Variant:** axis-aligned rectangles from points; change minimum area to maximum area for the interview version.
- [o] [962. Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/) — **Variant:** longest substring whose first character is smaller than its last; use strict inequality and return width + 1.
- [o] [963. Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/) — **Exact:** explicitly linked. **Variant:** arbitrary-orientation maximum-area rectangles change the objective.
- [o] [1102. Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/) — **Related:** bottleneck-path objective after assigning each cell its distance from the cat.
- [o] [1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) — **Related:** organizational-tree deletion; the engineer-only tree instead promotes descendants to a surviving ancestor.
- [ ] [1167. Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) — **Related:** Huffman's repeated merging of the two smallest weights; does not construct character codes.
- [o] [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) — **Variant:** swap land/water roles to count enclosed water components; assigning lakes to a particular island is additional work.
- [ ] [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) — **Related:** search sorted strings by prefix; the interview asks for a count rather than suggestions.
- [ ] [1296. Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) — **Exact:** partition into consecutive groups; set K = 5.
- [ ] [1801. Number of Orders in the Backlog](https://leetcode.com/problems/number-of-orders-in-the-backlog/) — **Variant:** order-book matching using buy/sell prices and priority queues.
- [ ] [1807. Evaluate the Bracket Pairs of a String](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/) — **Variant:** replace dictionary keys between delimiters; use %key% instead of (key).
- [ ] [1813. Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii/) — **Exact:** two sentences differ only by insertion of one contiguous phrase.
- [ ] [1882. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/) — **Related:** assign tasks across machines using availability tracking.
- [ ] [1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) — **Variant:** split overlapping people’s schedules into intervals with constant active membership; return names instead of color sums and include empty gaps. See the Round 1 practice notes below.
- [ ] [2812. Find the Safest Path in a Grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) — **Variant:** maximize the minimum distance from the cat along a mouse's path; adapt obstacles, endpoints, and the distance definition.

## Hard (18)

- [ ] [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) — **Exact:** explicitly linked in the interview notes.
- [ ] [68. Text Justification](https://leetcode.com/problems/text-justification/) — **Exact:** explicitly linked in the interview notes.
- [ ] [127. Word Ladder](https://leetcode.com/problems/word-ladder/) — **Variant:** minimum single-character transformations through dictionary words; LeetCode returns sequence length rather than operation count.
- [ ] [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/) — **Reported:** explicitly named in the supplied 2026 report summary.
- [ ] [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) — **Related:** explore deletions that produce balanced parentheses; lacks digit-controlled deletion constraints.
- [ ] [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) — **Related:** dynamically activate grid cells and maintain connectivity for the tower-construction API.
- [ ] [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) — **Reported:** explicitly named in the supplied 2026 report summary.
- [ ] [358. Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) — **Related:** ad cooldown/gap follow-up; scores and dynamic insertions require adaptation.
- [ ] [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) — **Reported:** explicitly named in the supplied 2026 report summary; practice the O(n²k) DP formulation, then binary search on the answer with a greedy feasibility check.
- [ ] [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) — **Related:** cache eviction by frequency.
- [ ] [715. Range Module](https://leetcode.com/problems/range-module/) — **Related:** range updates and interval tracking; arbitrary numeric range assignment requires adaptation.
- [ ] [770. Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) — **Variant:** simplify symbolic expressions and combine coefficients; LeetCode supports more operations.
- [ ] [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) — **Related:** count distinct subsequences for the question requiring all subsequences to be special.
- [ ] [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) — **Exact:** explicitly linked; weighted interval scheduling.
- [ ] [1970. Last Day Where You Can Still Cross](https://leetcode.com/problems/last-day-where-you-can-still-cross/) — **Exact:** explicitly linked. **Variant:** tower construction activates cells and connects left/right boundaries instead of flooding cells and checking top/bottom connectivity.
- [ ] [2050. Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) — **Related:** longest weighted dependency path in a DAG.
- [ ] [2188. Minimum Time to Finish the Race](https://leetcode.com/problems/minimum-time-to-finish-the-race/) — **Reported:** explicitly named in the supplied 2026 report summary.
- [ ] [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) — **Exact:** explicitly linked; scheduling with available and occupied rooms.

## Round 1 practice notes: schedules and magical string pairs

- **Schedule question (LC 1943 variant):** given `[name, start, end]` shifts, return `[start, end, active_names]` for each interval between consecutive event times, including gaps with `[]`. Treat shifts as `[start, end)`. Sort start/end events, emit the previous interval with the current active names, then apply all events at the next time. Maintain counts per person to handle overlapping shifts for the same name. Time: `O(n log n + P)`; auxiliary space: `O(n)`, excluding output, where `P` is the total number of names emitted. Example: Mary `[10, 40)` and John `[30, 50)` produce `[10, 30, [Mary]]`, `[30, 40, [Mary, John]]`, and `[40, 50, [John]]`.
- **Magical triplets question (LC 2506 variant):** for lowercase string `s`, count `0 <= i <= j < k < len(s)` such that `set(s[i:j+1]) == set(s[j+1:k+1])`. Encode each character set as a 26-bit mask. Precompute mask-to-count dictionaries for substrings starting at each index; sweep left to maintain dictionaries for substrings ending at `j`. Extending a substring adds its character with bitwise OR, and each update also adds the one-character substring. At each boundary, add `left_count[mask] * right_count[mask]` for matching masks. Each dictionary has at most 26 masks because growing a substring only adds letters. Time and auxiliary space: `O(26n)`. Examples: `"aaa" -> 4`, `"abab" -> 1`, `"abc" -> 0`.

Related practice: [1525. Number of Good Ways to Split a String](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/) compares distinct-character counts across a split of the entire string; magical pairs require equal character sets and allow arbitrary outer endpoints. It is not included in the checklist totals.

## 2026 report-summary practice notes

The supplied summary attributes these patterns to publicly shared Google SWE reports on Glassdoor, Blind, and LeetCode Discuss. Original report links were not supplied; treat these as prep leads, not a verified exact-question list. LC 200 and 416 were already listed above, so their entries were not duplicated.

- **Graph follow-ups:** practice constraints introduced mid-round after a Number of Islands opener, grid traversal with extra state when movement depends on the previous step, and topological reasoning for rankings derived from pairwise results.
- **DP optimization:** explain the initial formulation, identify the bottleneck, and derive a faster solution when the problem allows it; LC 410 is the example named in the summary.
- **Trie + hash map:** practice using the structures together. The summary mentions an August medium-hard problem and a Strong Hire outcome but does not identify an exact LeetCode match.
- **Union-Find correctness:** explain path compression and union-by-rank, justify correctness, and compare with DFS/BFS alternatives.

**Caveat from the supplied summary:** dated first-hand reports from recent months are scarce, and much of the public information describes patterns rather than exact questions. Treat claims of an “exact 2026 question list” cautiously.

games:
flip game II
https://leetcode.com/problems/predict-the-winner/description/ medium
https://leetcode.com/problems/can-i-win/description/ medium
https://leetcode.com/problems/stone-game/description/?envType=company&envId=google&favoriteSlug=google-thirty-days medium
https://leetcode.com/problems/stone-game-ii/description/ medium

First round Q:
https://leetcode.com/discuss/post/2095524/google-onsite-interview-29th-may-by-iamt-jbii/
