# Message Logger with Duplicate Suppression

- **Topic:** #queue #hash-map #stream-processing
- **Updated:** Oct 14, 2026
- 문제 번호가 없는 스트림 처리 문제. 아래 예시는 설명을 위해 구성했다.

## 문제

`Status(timestamp, message)`가 timestamp의 비내림차순으로 하나씩 들어온다. 전체 입력 배열은 미리 알 수 없다. `showMessage(status)`를 구현하여 **동일한 문자열의 다른 메시지가 앞뒤 10초 이내에 없을 때만** 출력하라.

중복이 발견되면 새 메시지뿐 아니라 **먼저 도착한 메시지도 숨겨야 한다.** 따라서 도착 즉시 출력할 수 없고, 미래의 중복을 확인하기 위해 10초 동안 기다려야 한다.

이 노트에서는 두 timestamp의 차이가 **10 미만이면 중복**, 정확히 10이면 별개의 유효한 메시지로 정의한다. 원문의 경계가 불명확하다면 면접에서 먼저 확인한다. 서로 다른 문자열은 영향을 주지 않는다.

```text
입력: (1, "foo"), (5, "foo"), (9, "foo"), (23, "foo")

시간이 33에 도달한 후 출력:
[23s] foo
```

`1`, `5`, `9`의 메시지는 중복으로 숨긴다. `23`의 메시지는 이후 10초 동안 중복이 없으면 `33`에 출력할 수 있다. 출력의 `[23s]`는 실제 출력 시각이 아니라 **메시지의 원래 timestamp**이다.

## 풀이: 큐 + 딕셔너리

**큐는 출력 확정 순서를 관리하고, 딕셔너리는 같은 문자열의 가장 최근 메시지를 찾는다.**

- `pending`: 아직 10초 대기가 끝나지 않은 모든 메시지를 도착 순서로 저장하는 `deque`.
- `latest[message]`: 해당 문자열의 가장 최근 `Pending` 객체를 가리킨다.
- `Pending.invalid`: 앞이나 뒤의 중복 때문에 출력할 수 없는지 표시한다.

큐와 딕셔너리는 **같은 객체를 참조**한다. 따라서 딕셔너리에서 찾은 객체의 `invalid`를 바꾸면 큐 안의 이전 메시지도 무효화된다.

### 새 메시지가 들어왔을 때

1. 현재 timestamp를 기준으로 대기가 끝난 큐의 앞부분을 처리한다. 유효한 메시지만 출력한다.
2. `latest`에서 같은 문자열의 이전 객체를 찾는다. 만료 처리를 먼저 했으므로, 남아 있다면 시간 차이는 반드시 10 미만이다.
3. 이전 객체와 새 객체를 **둘 다** 무효화한다.
4. 새 객체를 큐에 넣고 `latest`를 새 객체로 갱신한다. 새 객체가 이미 무효여도 등록해야 한다.

## Python 코드

```python
from collections import deque
from dataclasses import dataclass


@dataclass
class Status:
    timestamp: int
    message: str


@dataclass
class Pending:
    status: Status
    invalid: bool = False


class MessageLogger:
    WINDOW = 10

    def __init__(self):
        self.pending = deque()
        self.latest = {}

    def showMessage(self, status: Status) -> None:
        # 정확히 10초가 지난 메시지부터 확정한다.
        self.advance_time(status.timestamp)

        previous = self.latest.get(status.message)
        current = Pending(status)

        if previous is not None:
            previous.invalid = True
            current.invalid = True

        self.pending.append(current)
        self.latest[status.message] = current

    def advance_time(self, timestamp: int) -> None:
        while (
            self.pending
            and self.pending[0].status.timestamp + self.WINDOW <= timestamp
        ):
            entry = self.pending.popleft()
            status = entry.status

            if not entry.invalid:
                print(f"[{status.timestamp}s] {status.message}")

            # 더 최근 객체를 가리키고 있다면 그 매핑은 유지한다.
            if self.latest.get(status.message) is entry:
                del self.latest[status.message]
```

```python
logger = MessageLogger()

logger.showMessage(Status(1, "foo"))
logger.showMessage(Status(5, "foo"))
logger.showMessage(Status(9, "foo"))
logger.showMessage(Status(23, "foo"))

logger.advance_time(33)
# [23s] foo
```

## 왜 가장 최근 메시지만 찾아도 되는가?

현재 메시지와 10초 미만으로 가까운 이전 메시지가 하나라도 있다면, 가장 최근 메시지도 반드시 10초 미만으로 가깝다. 따라서 현재 메시지의 중복 여부는 `latest` 하나로 판단할 수 있다.

그보다 오래된 메시지는 중간의 같은 문자열 메시지가 도착할 때 이미 무효화되었다. 예를 들어 `1 → 8 → 15`에서는 `8`이 `1`과 자신을 무효화하고, `15`가 `8`과 자신을 무효화하므로 모두 숨겨진다. `1`과 `15`가 직접 10초 이내일 필요는 없다.

시간이 `t + 10`에 도달하면 `t`의 메시지를 무효화할 미래 입력은 더 이상 올 수 없다. 큐는 timestamp 순서이므로 앞에서부터 안전하게 출력 여부를 확정할 수 있다.

## 예시 추적

| 도착 시각 | 처리 | `latest["foo"]` |
| --- | --- | --- |
| 1 | 첫 메시지를 유효한 상태로 대기 | `1, valid` |
| 5 | 1과 5를 모두 무효화 | `5, invalid` |
| 9 | 5와 9를 모두 무효화 | `9, invalid` |
| 23 | 1, 5, 9는 만료되어 버림. 23을 새로 대기 | `23, valid` |
| 33 | 유효한 23을 출력하고 제거 | 없음 |

## 헷갈린 지점 / 기억할 것

- **즉시 출력하면 안 된다.** 이후 메시지가 앞의 메시지를 무효화할 수 있다.
- **무효화된 메시지도 중복 판정에 사용한다.** `1, 8, 15`에서 8을 무시하면 15를 잘못 출력한다.
- **만료된 이전 객체를 꺼낼 때 최신 매핑을 무조건 삭제하면 안 된다.** 예를 들어 `1, 8, 12`에서 12가 도착하면 1만 만료된다. 이때 `latest["foo"]`가 가리키는 8은 남겨야 12도 무효화할 수 있다.
- 위 삭제 조건은 `is`를 사용한다. timestamp나 필드 값이 아니라 **정확히 같은 객체인지** 확인한다. 같은 timestamp의 중복도 올바르게 처리한다.
- **입력이 끊겨도 시간은 흐른다.** 실제 서비스에서는 타이머가 `advance_time()`을 호출해야 마지막 메시지도 출력된다. 이 예시 코드 자체가 타이머를 실행하지는 않는다.
- 타이머와 입력은 같은 시간 기준으로 순서대로 처리해야 한다. 이미 확정한 시간보다 과거인 입력이 나중에 들어오는 상황은 가정하지 않는다. 입력의 동시 처리가 가능하면 직렬화가 필요하다.
- 정확히 10초 차이도 중복으로 정의한다면, 만료 조건을 `timestamp_of_entry + WINDOW < timestamp`로 바꾸고 경계를 지난 뒤 확정해야 한다.

## 복잡도

- 각 메시지는 큐에 한 번 들어가고 한 번 나온다. `n`개 메시지의 총 처리 시간은 평균적인 딕셔너리 연산을 가정하면 **O(n)**, 메시지당 **상각 O(1)**이다. 별도의 타이머 호출 `q`회를 포함하면 총 **O(n + q)**이다.
- 한 번의 호출에서 여러 메시지가 만료되면 그 호출은 O(k)가 걸릴 수 있다.
- 공간은 **O(k)**. `k`는 10초 동안 대기 중인 메시지 수이며, 10초가 고정이어도 유입량에 따라 커진다.

**기억할 한 문장: 10초 동안 큐에 보관하고, 같은 메시지가 오면 이전 것과 새것을 함께 무효화한 뒤, 만료 시 유효한 것만 출력한다.**
