# Google 면접 오답노트

LeetCode 번호가 없는 Google 면접 문제를 문제별 파일로 정리한다.
번호가 있는 문제는 [LeetCode 오답노트](../오답노트/README.md)에 정리한다.

새 문제를 추가할 때는 [템플릿](../오답노트/_TEMPLATE.md)을 참고하고 아래 목록에도 추가한다.

| Problem | 기억할 것 | Updated |
|---|---|---|
| [Earliest Day to Connect Tower Columns](Earliest%20Day%20to%20Connect%20Tower%20Columns.md) | BFS + reachable 유지; 첫 열에서 새로 연결된 영역만 확장; enqueue 시 방문 처리; 타워당 최대 한 번 탐색하므로 전체 O(d), 매일 새 BFS면 O(d²) | Oct 15, 2026 |
| [Longest Substring With Increasing Endpoints](Longest%20Substring%20With%20Increasing%20Endpoints.md) | 문자별 first/last + 알파벳 순회; 더 작은 문자 중 가장 이른 위치와 연결; 마지막 문자 고정은 abca에서 실패; 비교 후 시작 후보 갱신; O(n), O(1) | Oct 15, 2026 |
| [Count Words With a Given Prefix](Count%20Words%20With%20a%20Given%20Prefix.md) | 선형 탐색 + startswith O(n × p), 공간 O(1); 정렬된 배열에서 앞 p글자의 lower/upper bound 차이로 카운트 O(p × log n), 슬라이싱 공간 O(p); 중복도 포함 | Oct 15, 2026 |
| [Group Items by Shared Attributes](Group%20Items%20by%20Shared%20Attributes.md) | 공통 속성의 직접·간접 연결을 DFS로 그룹화; 속성 → 아이템 매핑; push 시 방문 처리; 속성 목록은 pop으로 한 번만 확장; O(n + m) | Oct 15, 2026 |
| [Longest Path in a DAG](Longest%20Path%20in%20a%20DAG.md) | DFS + 수동 memo; dfs(u)는 u에서 시작하는 최장 간선 수; 모든 시작점 비교; DAG라 별도 visited 불필요; 캐시 값 0도 재사용 | Oct 15, 2026 |
| [Tasks in Cyclic Dependencies](Tasks%20in%20Cyclic%20Dependencies.md) | DFS 경로별 append/pop; position으로 사이클 구간만 수집; 전역 visited로 건너뛰면 누락 가능; 백트래킹은 팩토리얼, SCC는 O(V + E) | Oct 15, 2026 |
| [Nearest Favorite City](Nearest%20Favorite%20City.md) | Dijkstra + 최소 힙; favorite을 발견할 때가 아니라 유효한 pop에서 반환; 오래된 항목 건너뛰기; 양수 가중치에서 (시간, 도시)로 동률 처리 | Oct 15, 2026 |
| [Simplify Algebraic Expression](Simplify%20Algebraic%20Expression.md) | 변수별 계수 합산; 항의 sign × 괄호의 group_sign; 괄호 진입·종료 시 부호 초기화; 0·±1 출력 처리 | Oct 15, 2026 |
| [Remove Bad Pairs](Remove%20Bad%20Pairs.md) | 스택 맨 위와 같은 글자·다른 대소문자이면 pop; 연쇄 제거; 빈 입력·양방향 대소문자·경계 위치·연쇄 동작 테스트 | Oct 15, 2026 |
| [Maximum Product of K Elements](Maximum%20Product%20of%20K%20Elements.md) | 홀수 k 먼저 처리; 정렬 양끝 또는 양수 최대 힙·음수 최소 힙으로 쌍 비교; 모두 음수인 홀수 k는 0에 가까운 값; 한 힙 temp 방식은 마지막 한 자리 주의 | Oct 15, 2026 |
| [Package Transfer with Flight Schedules](Package%20Transfer%20with%20Flight%20Schedules.md) | 다익스트라 + 최소 힙; earliest는 공항별 최단 도착 시각; 같은 공항이면 빠른 도착만 유지; 막다른 후보여도 나머지 탐색; 출발 >= 도착 | Oct 15, 2026 |
| [Router Reachability](Router%20Reachability.md) | 활성 라우터 중 최근접 후보만 DFS; 동률이면 분기; 경로별 visited.add → 재귀 → visited.remove; 거리 제곱 비교 | Oct 15, 2026 |
| [Range Assignment Queries](Range%20Assignment%20Queries.md) | 역순 + DSU; find/compression 분리, 쿼리 끝에서 압축; 같은 k는 차분 배열 O(n + q), min/max는 빈틈 주의 | Oct 15, 2026 |
| [Word Transformation](Word%20Transformation.md) | 단어를 노드로 보는 BFS; 한 글자씩 바꿔 이웃 생성; enqueue 시 방문 처리; 단어 수가 아닌 변환 횟수 반환 | Oct 15, 2026 |
| [Divide Array Into Consecutive Groups of Five](Divide%20Array%20Into%20Consecutive%20Groups%20of%20Five.md) | Counter + Greedy: 남은 최솟값의 빈도만큼 연속된 다섯 값 차감; `sorted(count)`는 빈도가 아닌 키 정렬 | Oct 14, 2026 |
| [Ad Scheduler with Cooldown](Ad%20Scheduler%20with%20Cooldown.md) | 최대 힙에는 노출 가능한 광고만 유지; 기본은 직전 광고 하나 보관, follow-up은 쿨다운 큐; 만료 후 힙 복귀; O(log n) | Oct 14, 2026 |
| [Message Logger with Duplicate Suppression](Message%20Logger%20with%20Duplicate%20Suppression.md) | 큐 + 딕셔너리로 10초 지연 출력; 중복은 이전/현재 모두 무효화; 무효 메시지도 최신 매핑에 유지; 삭제 시 객체 동일성 확인 | Oct 14, 2026 |
| [Lexicographically Smallest Closed Walk](Lexicographically%20Smallest%20Closed%20Walk.md) | 사전순 DFS는 정답이지만 지수 시간; BFS 거리 + Greedy로 남은 횟수와 거리의 홀짝을 확인; D < L < R < U | Oct 14, 2026 |
| [Balanced Parentheses After Digit Deletions](Balanced%20Parentheses%20After%20Digit%20Deletions.md) | 왼쪽→오른쪽 DP `(미사용 삭제 대상 수, balance)`; 괄호는 삭제/유지 분기, 숫자는 삭제 대상 소비; 최종 `(0, 0)` 확인 | Oct 14, 2026 |
| [Find All Ones in a Sparse Bit Array](Find%20All%20Ones%20in%20a%20Sparse%20Bit%20Array.md) | 남은 구간 확인 → 첫 True를 이진 탐색; True면 right = mid, False면 left = mid + 1; 종료 시 left를 기록 | Oct 14, 2026 |
