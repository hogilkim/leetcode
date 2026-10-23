# Word Transformation

- **Topic:** #bfs #graph #shortest-path #string
- **Updated:** Oct 15, 2026
- LeetCode 127. Word Ladder와 유사하지만, 여기서는 **변환 횟수**를 반환한다. 별도 문제 번호와 입력 크기 제한은 제공되지 않았다.

## 문제

시작 단어 `source`, 목표 단어 `target`, 단어 배열 `arr`가 주어진다. 한 번의 연산으로 현재 단어의 **정확히 한 글자**를 다른 소문자로 바꿀 수 있다. 바꾼 결과는 반드시 `arr` 안에 있어야 한다.

`source`를 `target`으로 바꾸는 **최소 연산 횟수**를 반환한다. 불가능하면 `-1`을 반환한다.

- 모든 단어는 길이가 같고 영어 소문자로만 이루어진다.
- `source`는 `arr`에 없어도 된다. 배열에 있어야 하는 것은 **연산 후의 단어**다.
- `source == target`이면 변환이 필요 없으므로 `0`이다. 이때는 `target`이 `arr`에 없어도 된다.
- 두 단어가 다른데 `target`이 `arr`에 없으면 `-1`이다.
- 글자를 삽입하거나 삭제하거나, 한 번에 여러 글자를 바꿀 수는 없다.

### 예시

```text
source = "hit"
target = "cog"
arr = ["hot", "dot", "dog", "lot", "log", "cog"]

hit → hot → dot → dog → cog
```

각 화살표에서 한 글자만 바뀌고, 바뀐 단어는 모두 `arr`에 있다. 단어는 5개지만 **연산은 4번**이므로 정답은 `4`다.

| source | target | arr | 결과 | 이유 |
| --- | --- | --- | --- | --- |
| `"hit"` | `"hit"` | `[]` | `0` | 이미 목표와 같다 |
| `"hit"` | `"cog"` | `["hot", "dot", "dog"]` | `-1` | 목표가 배열에 없다 |
| `"hit"` | `"cog"` | `["hot", "cog"]` | `-1` | 목표는 있지만 연결되는 변환 경로가 없다 |
| `"hit"` | `"hot"` | `["hot"]` | `1` | 한 글자만 바꾸면 된다 |

## 풀이: 단어를 노드로 보는 BFS

단어 하나를 그래프의 노드로 생각한다. **정확히 한 글자가 다른 두 단어 사이에는 간선이 있다.** 시작 노드는 `source`이며, 이동해서 도착하는 단어는 `arr`에 있어야 한다.

모든 간선의 비용은 연산 한 번으로 동일하다. 따라서 최소 연산 횟수는 이 그래프의 최단 거리이고, **BFS**로 구할 수 있다. 그래프의 모든 간선을 미리 만들 필요 없이 현재 단어에서 갈 수 있는 다음 단어를 생성한다.

### 다음 단어를 만드는 방법

현재 단어의 각 위치에 대해 `'a'`부터 `'z'`까지 넣어 본다. 원래 문자와 같으면 건너뛴다.

```python
next_word = word[:i] + char + word[i + 1:]
```

예를 들어 `word = "hit"`, `i = 1`, `char = "o"`라면 `next_word = "hot"`이다. 이 후보가 아직 방문하지 않은 배열 단어이면 탐색한다.

`remaining = set(arr)`는 **배열에 있으면서 아직 방문하지 않은 단어**를 저장한다. 후보가 여기에 있는지 평균 `O(1)`의 집합 조회로 확인한다. 단, 후보 문자열 생성과 해싱에는 길이에 비례하는 시간이 든다.

### 진행 순서

1. `source == target`이면 `0`을 반환한다.
2. `target`이 `remaining`에 없으면 `-1`을 반환한다.
3. 큐에 `(source, 0)`을 넣고, `source`가 집합에 있으면 제거한다.
4. 큐에서 `(word, steps)`를 꺼내 한 글자씩 바꾼 후보를 만든다.
5. 후보가 `remaining`에 없으면 건너뛴다. 목표라면 `steps + 1`을 반환한다.
6. 나머지 유효한 후보는 **큐에 넣는 시점에 집합에서 제거**하고 `(next_word, steps + 1)`을 큐에 넣는다.
7. 큐가 빌 때까지 목표를 찾지 못하면 `-1`을 반환한다.

## 코드

```python
from collections import deque
from typing import List


class Solution:
    def minOperations(
        self, source: str, target: str, arr: List[str]
    ) -> int:
        if source == target:
            return 0

        remaining = set(arr)
        if target not in remaining:
            return -1

        queue = deque([(source, 0)])
        remaining.discard(source)

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == word[i]:
                        continue

                    next_word = word[:i] + char + word[i + 1:]

                    if next_word not in remaining:
                        continue

                    if next_word == target:
                        return steps + 1

                    # 큐에 넣기 전에 방문 처리한다.
                    remaining.remove(next_word)
                    queue.append((next_word, steps + 1))

        return -1
```

`discard(source)`는 `source`가 집합에 없어도 오류를 내지 않는다. `remove(next_word)`는 바로 앞에서 집합에 있는지 확인했으므로 안전하다.

## 예시 추적

```text
거리 0: hit
거리 1: hot
거리 2: dot, lot
거리 3: dog, log
거리 4: cog → 4 반환
```

`dog`와 `log` 모두 `cog`에 연결되지만 BFS는 거리 3인 노드들을 거리 4인 노드들보다 먼저 처리한다. 따라서 처음 `cog`를 발견할 때의 거리가 최솟값이다.

## 왜 BFS가 최소 횟수를 보장하는가?

큐에는 시작점으로부터의 거리가 작은 순서로 단어가 들어간다. 거리 `d`인 단어에서 새로 발견한 이웃은 거리 `d + 1`이고, 큐의 뒤에 추가되므로 더 가까운 단어들이 먼저 처리된다.

따라서 목표를 처음 발견한 시점에는 더 짧은 경로가 남아 있을 수 없다. 어떤 단어를 처음 발견했을 때도 이미 최단 거리가 정해지므로, 방문 처리 후 다시 탐색할 필요가 없다.

## 복잡도

`N = len(arr)`, `L = 단어 길이`라고 하자. 알파벳 수 26은 상수로 본다.

- **시간: `O(N × L²)`**. 단어마다 최대 `25 × L`개의 후보를 만들고, Python에서 각 후보의 문자열 생성과 해싱에 `O(L)`이 든다. 각 배열 단어는 최대 한 번만 큐에 들어간다.
- **추가 공간: `O(N × L)`**. 집합과 큐에 최대 `O(N)`개의 단어를 관리하며, 탐색 중 생성해 큐에 저장하는 문자열의 길이는 `L`이다.

위 시간 복잡도는 BFS를 진행하는 경우의 상한이다. `source == target`이면 바로 `O(1)`에 반환하며, 목표가 배열에 없으면 집합 생성 후 종료한다.

## 헷갈린 지점 / 기억할 것

- **최소 횟수 + 모든 이동 비용이 동일함 → BFS**. DFS로 처음 찾은 경로가 최단 경로라는 보장은 없다.
- **큐에 넣을 때 방문 처리한다.** 꺼낼 때 처리하면 서로 다른 부모가 같은 단어를 중복으로 큐에 넣을 수 있다.
- `remaining`은 배열 포함 여부와 방문 여부를 동시에 관리하므로 별도의 `visited` 집합이 필요 없다.
- `source == target` 검사를 목표의 배열 포함 여부 검사보다 먼저 해야 한다.
- 목표가 배열에 있다는 것은 필요조건일 뿐이다. 연결 경로가 없으면 여전히 `-1`이다.
- 각 위치를 바꾼 후보는 항상 현재 `word`에서 만든다. 다른 후보를 계속 수정해서 한 번에 여러 글자를 바꾸면 안 된다.
- **반환값은 단어 개수가 아니라 화살표 개수다.** 시작 거리는 `0`, 불가능할 때는 `-1`이다. LeetCode 127의 반환 규칙과 구별한다.
