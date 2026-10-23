# Group Items by Shared Attributes

- **Topic:** #graph #dfs #bfs #connected-components #hashmap
- **Updated:** Oct 15, 2026
- 대화에서 정리한 문제로, 별도 LeetCode 번호와 입력 크기 제한은 제공되지 않았다.

## 문제

문자열의 2차원 배열 `attributes`가 주어진다. `attributes[i]`는 인덱스 `i`인 아이템의 속성 목록이다. **공통 속성이 하나라도 있는 아이템들을 같은 그룹으로 묶고**, 각 그룹의 아이템 인덱스 목록을 반환한다.

- 직접 공통 속성이 없어도 다른 아이템을 통해 연결되면 같은 그룹이다.
- 모든 아이템은 정확히 하나의 그룹에 포함된다.
- 다른 아이템과 연결되지 않은 아이템은 혼자 그룹을 이룬다.
- 그룹의 순서와 그룹 안의 인덱스 순서는 상관없다.

### 예시 1

```text
attributes = [
    ["red", "large"],
    ["blue", "small"],
    ["large", "round"],
    ["small"],
    ["green"],
]

결과: [[0, 2], [1, 3], [4]]
```

아이템 `0`, `2`는 `"large"`를, 아이템 `1`, `3`은 `"small"`을 공유한다. 아이템 `4`는 혼자 남는다.

### 예시 2: 간접 연결도 같은 그룹

```text
attributes = [["a"], ["a", "b"], ["b"]]

아이템 0 → 속성 "a" → 아이템 1 → 속성 "b" → 아이템 2

결과: [[0, 1, 2]]
```

아이템 `0`, `2` 사이에는 직접 공통 속성이 없지만, 아이템 `1`이 두 아이템을 연결한다.

## 풀이: 속성별 인덱스 매핑 + DFS

아이템을 노드로 보고, 공통 속성이 있으면 연결된 것으로 생각한다. 구해야 하는 그룹은 이 무방향 그래프의 **연결 요소(connected component)**다.

모든 아이템 쌍을 비교하거나 같은 속성의 아이템들을 모든 쌍으로 연결할 필요는 없다. 대신 `attribute_to_items[attr]`에 해당 속성을 가진 아이템 인덱스를 저장한다.

1. 모든 속성을 순회하며 `속성 → 아이템 인덱스 목록` 매핑을 만든다.
2. 아직 방문하지 않은 아이템에서 새로운 그룹의 DFS를 시작한다.
3. 스택에서 아이템을 꺼내 그룹에 추가한다.
4. 그 아이템의 각 속성으로 연결되는 이웃들을 찾는다. 방문하지 않은 이웃은 **스택에 넣을 때** 방문 처리한다.
5. 속성의 이웃 목록은 `pop(attr, [])`으로 꺼내면서 매핑에서 삭제한다. 같은 속성의 이웃 목록을 반복 탐색하지 않는다.
6. 스택이 비면 연결 요소 하나가 완성되므로 결과에 추가한다.

## 코드

```python
from collections import defaultdict


class Solution:
    def groupItems(self, attributes: list[list[str]]) -> list[list[int]]:
        attribute_to_items = defaultdict(list)

        for i, attrs in enumerate(attributes):
            for attr in attrs:
                attribute_to_items[attr].append(i)

        visited = set()
        groups = []

        for i in range(len(attributes)):
            if i in visited:
                continue

            stack = [i]
            visited.add(i)
            group = []

            while stack:
                item = stack.pop()
                group.append(item)

                for attr in attributes[item]:
                    # 각 속성의 이웃 목록은 한 번만 탐색한다.
                    neighbors = attribute_to_items.pop(attr, [])

                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

            groups.append(group)

        return groups
```

## 왜 속성 매핑을 삭제해도 되는가?

속성 하나를 처음 탐색할 때 그 속성을 가진 모든 아이템을 확인한다. 아직 방문하지 않은 아이템은 전부 스택에 넣고, 이미 방문한 아이템은 이미 탐색 대상으로 등록되어 있다. 따라서 그 속성의 이웃 목록을 다시 읽어도 새로 발견할 아이템은 없다.

매핑에서 속성을 삭제해도 각 아이템의 원래 `attributes`는 유지된다. 예시 2에서 `"a"` 매핑을 삭제해도 아이템 `1`을 꺼냈을 때 그 아이템의 `"b"`를 통해 아이템 `2`로 이어갈 수 있다.

DFS는 공통 속성으로 연결된 아이템만 추가하며, 발견한 아이템의 모든 속성을 계속 탐색한다. 따라서 한 시작점에서 도달할 수 있는 모든 아이템을 정확히 하나의 그룹으로 모은다. 바깥 반복문은 분리된 그룹과 고립된 아이템도 처리한다.

## 복잡도

`n`은 아이템 수, `m = sum(len(attrs) for attrs in attributes)`는 전체 속성 등장 횟수다. 해시 연산을 평균 `O(1)`로 가정한다.

- **시간: `O(n + m)`.** 매핑 구성에 `O(m)`, 모든 아이템 순회에 `O(n)`, 각 아이템의 속성 확인에 총 `O(m)`이 든다. 매핑의 이웃 목록도 속성마다 한 번만 확장하므로 전체 길이 합은 `m`이다.
- **공간: `O(n + m)`.** 속성 매핑에 `O(m)`, 방문 집합·스택·결과에 `O(n)`이 든다.

## 기억할 것 / 헷갈릴 지점

- 그룹 기준은 **직접 또는 간접 연결**이다. 시작 아이템과 속성을 직접 공유하는 아이템만 모으면 간접 연결을 놓친다.
- `visited`는 모든 그룹에서 공유한다. 스택에 넣는 순간 방문 처리하면 같은 아이템이 중복으로 들어가지 않는다.
- 아이템 방문 처리와 속성 목록 삭제는 역할이 다르다. `visited`만 쓰고 속성 목록을 계속 읽으면, 모든 아이템이 같은 속성을 가질 때 이웃 목록을 반복 스캔해 `O(n²)`이 될 수 있다.
- `pop(attr, [])`의 기본값 덕분에 이미 처리한 속성을 만나도 빈 목록으로 넘어간다. 입력 배열은 수정하지 않는다.
- 빈 입력은 `[]`를 반환한다. 빈 속성 목록이 허용된다면 그 아이템은 독립된 그룹이 된다. 한 아이템에 같은 속성이 중복되어도 방문 처리 덕분에 결과 인덱스는 중복되지 않는다.
- BFS도 가능하다. 스택 대신 `collections.deque`를 쓰고 `popleft()`로 꺼내면 된다. 방문 처리와 속성 목록 삭제 방식, 시간·공간 복잡도는 같다.
- 관련 문제: [721. Accounts Merge](../오답노트/721.%20Accounts%20Merge.md) — 공통 이메일로 계정들을 병합하는 것도 연결 요소를 찾는 문제다.
