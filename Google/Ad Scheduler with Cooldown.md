# Ad Scheduler with Cooldown

- **Topic:** #heap #queue #design
- **Updated:** Oct 15, 2026

## 문제

광고를 등록하고, 요청할 때마다 **지금 노출 가능한 광고 중 점수가 가장 높은 광고**를 반환한다.

- `insertAd(content, score)`: 광고와 점수를 등록한다.
- `getAd()`: 광고를 반환한 뒤 그 광고의 점수를 감소시킨다. 광고는 삭제되지 않는다.
- 기본 조건: 같은 광고를 연속으로 반환할 수 없다.
- Follow-up: 같은 광고를 다시 반환하려면 다른 광고가 `gap`개 이상 나와야 한다. 연산을 O(1)에 가깝게 유지하라.

예: `A: 5, B: 3`이고 반환할 때마다 1점 감소한다면, 기본 조건에서 `A → B → A → B`. 두 번째 요청에서는 A의 점수가 더 높아도 직전에 반환했으므로 B를 선택한다.

## 기본 풀이: 최대 힙 + 직전 광고 보관

**직전에 반환한 광고 하나를 힙 밖에 보관한다.**

1. `insertAd()`는 최대 힙에 광고를 넣는다.
2. `getAd()`는 힙에서 최고 점수 광고를 먼저 꺼낸다.
3. 이전에 보관하던 광고를 힙에 돌려놓는다.
4. 이번에 꺼낸 광고의 점수를 감소시키고 힙 밖에 보관한 뒤 반환한다.

반드시 **현재 광고를 pop한 다음 이전 광고를 push**한다. 이전 광고를 먼저 넣으면 같은 광고가 연속으로 선택될 수 있다.

- 시간: 두 API 모두 O(log n).
- 전체 저장 공간: O(n). `n`은 등록된 광고 수.

### Python 코드

아래 두 구현은 다음 규칙을 사용한다.

- 반환할 때마다 점수를 **1점 감소**시키며, 0점이나 음수가 되어도 광고를 유지한다.
- 동점이면 **처음 등록한 순서**가 빠른 광고를 선택한다. 힙의 `(음수 점수, 등록 번호, content)`에서 등록 번호가 동점을 처리한다.
- `content`는 문자열이며, 같은 content를 다시 등록하면 `ValueError`를 발생시킨다.
- 선택 가능한 광고가 없으면 `None`을 반환하고, 쿨다운 상태를 유지한다. 실패한 요청은 다른 광고의 노출로 세지 않는다.

```python
import heapq


class BasicAdScheduler:
    def __init__(self):
        self.ready = []
        self.previous = None
        self.contents = set()

    def insertAd(self, content: str, score: int) -> None:
        if content in self.contents:
            raise ValueError("이미 등록된 광고입니다.")

        order = len(self.contents)
        self.contents.add(content)
        heapq.heappush(self.ready, (-score, order, content))

    def getAd(self) -> str | None:
        if not self.ready:
            # 실패해도 직전 광고를 풀어 주면 안 된다.
            return None

        neg_score, order, content = heapq.heappop(self.ready)

        # 현재 광고를 고른 다음에야 직전 광고를 후보로 돌려놓는다.
        if self.previous is not None:
            heapq.heappush(self.ready, self.previous)

        # score -= 1이므로 음수 점수에는 1을 더한다.
        self.previous = (neg_score + 1, order, content)
        return content
```

```python
scheduler = BasicAdScheduler()
scheduler.insertAd("A", 5)
scheduler.insertAd("B", 3)

print([scheduler.getAd() for _ in range(4)])
# ['A', 'B', 'A', 'B']

single = BasicAdScheduler()
single.insertAd("A", 5)
print(single.getAd())  # A
print(single.getAd())  # None: A는 여전히 직전 광고다.
single.insertAd("B", 1)
print(single.getAd())  # B: 새 광고를 넣으면 다시 진행할 수 있다.
print(single.getAd())  # A
```

## Follow-up 풀이: 최대 힙 + 쿨다운 큐

**힙에는 노출 가능한 광고만, 큐에는 아직 기다려야 하는 광고만 넣는다.** 모든 광고에 동일한 고정 `gap`을 적용한다고 가정한다.

1. `getAd()` 시작 시 쿨다운이 끝난 광고를 큐 앞에서 꺼내 힙으로 옮긴다.
2. 힙에서 최고 점수 광고를 꺼내 점수를 감소시킨다.
3. 즉시 힙에 돌려놓지 않고, 다음 노출 가능 위치와 함께 큐에 넣은 뒤 반환한다.

0-based 노출 위치 `t`에서 반환했다면 다음 가능 위치는 **`t + gap + 1`**. 예를 들어 `gap = 2`이면 `A → B → C → A`가 가능하다. 반환에 성공했을 때만 노출 위치를 증가시킨다.

- 고정 gap에서는 큐에 들어간 순서대로 쿨다운이 끝나므로 FIFO 큐(`deque`)를 쓴다.
- 시간: 삽입 O(log n), 반환 O(log n). 큐 자체의 앞/뒤 연산은 O(1).
- 전체 저장 공간: O(n).
- **힙을 사용하면 전체 연산이 O(1)이 되는 것은 아니다.** O(1)에 가까운 구현이 꼭 필요하면 점수가 작은 고정 범위인지 확인하고 점수별 버킷 등을 검토한다.

### Python 코드

`position`은 **지금까지 성공적으로 반환한 광고 수**, 즉 다음 노출의 0-based 위치다. `gap`은 생성 시 정하는 0 이상의 정수이며, `gap = 1`이면 기본 문제와 같다. `gap = 0`이면 같은 광고를 연속으로 반환할 수 있다.

```python
import heapq
from collections import deque


class AdScheduler:
    def __init__(self, gap: int = 1):
        if not isinstance(gap, int) or gap < 0:
            raise ValueError("gap은 0 이상의 정수여야 합니다.")

        self.gap = gap
        self.position = 0
        self.ready = []
        self.cooldown = deque()
        self.contents = set()

    def insertAd(self, content: str, score: int) -> None:
        if content in self.contents:
            raise ValueError("이미 등록된 광고입니다.")

        order = len(self.contents)
        self.contents.add(content)
        heapq.heappush(self.ready, (-score, order, content))

    def getAd(self) -> str | None:
        while self.cooldown and self.cooldown[0][0] <= self.position:
            _, ad = self.cooldown.popleft()
            heapq.heappush(self.ready, ad)

        if not self.ready:
            # 요청 횟수가 아니라 성공한 노출 수로 쿨다운을 센다.
            return None

        neg_score, order, content = heapq.heappop(self.ready)
        next_ad = (neg_score + 1, order, content)
        ready_at = self.position + self.gap + 1
        self.cooldown.append((ready_at, next_ad))
        self.position += 1
        return content
```

```python
scheduler = AdScheduler(gap=2)
scheduler.insertAd("A", 5)
scheduler.insertAd("B", 3)
scheduler.insertAd("C", 1)

print([scheduler.getAd() for _ in range(6)])
# ['A', 'B', 'C', 'A', 'B', 'C']

blocked = AdScheduler(gap=2)
blocked.insertAd("A", 5)
blocked.insertAd("B", 3)
print([blocked.getAd() for _ in range(4)])
# ['A', 'B', None, None]

blocked.insertAd("C", 1)
print(blocked.getAd())  # C
print(blocked.getAd())  # A: B와 C가 나왔으므로 다시 선택 가능
```

모든 광고의 `gap`이 같고 성공한 노출마다 위치가 1씩 증가하므로, 재노출 가능 위치도 큐에 넣는 순서대로 증가한다. 한 위치에서 만료되는 광고는 최대 하나여서 `getAd()`는 O(log n)이다. 광고마다 서로 다른 gap을 적용한다면 만료 순서가 달라지므로 FIFO 큐 대신 재노출 가능 위치를 기준으로 하는 별도의 최소 힙이 필요하다.

## 기억할 것

- 쿨다운 중인 광고를 힙에 두고 유효한 광고가 나올 때까지 pop하면 한 요청에서 최악 O(n log n). 건너뛴 광고도 다시 넣어야 한다.
- **선택할 수 없는 광고는 힙 밖에서 관리한다.** 기본 문제는 직전 광고 하나, follow-up은 쿨다운 큐.
- 점수 감소량, 동점 처리, 동일 content 재등록, 가능한 광고가 없을 때의 반환값은 원문에서 정하지 않았으므로 확인해야 한다. 위 코드는 설명을 위해 정한 규칙을 사용한다.
