---
name: handoff
description: 세션을 새로 열기 전, 컨텍스트가 길어졌을 때, 제출 직전에 docs/HANDOFF.md를 사실대로 갱신한다.
---

# 인수인계 갱신

docs/HANDOFF.md를 다음 구조로 갱신한다. 과장 없이 실행해서 확인한 사실만 쓴다.

1. 목표와 성공 기준 (AGENTS.md에서 2줄)
2. 현재 상태: 되는 것 / 안 되는 것 (각각 확인한 명령 포함)
3. 실행 방법 (복사해서 바로 되는 명령)
4. 주요 결정 (DECISIONS.md 번호와 한 줄 요약)
5. 알려진 한계와 위험
6. 다음 할 일 3개 (우선순위 순)

다른 사람이 이 문서만 읽고 10분 안에 이어서 작업할 수 있어야 한다.
갱신 후 `git add docs/HANDOFF.md && git commit -m "docs: HANDOFF 갱신 (<현재 상태 한 줄>)"`을 제안한다.
