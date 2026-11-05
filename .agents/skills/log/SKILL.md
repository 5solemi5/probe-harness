---
name: log
description: 설계 결정을 내렸거나, AI 결과를 받아들이거나 고치거나 버렸을 때, 담당자 답을 받았을 때 docs 기록을 한 줄씩 추가한다.
---

# 작업 기록

사용자가 알려 준 사실만 적는다. 근거가 없으면 "근거 없음"이라고 쓰고 지어내지 않는다.

- 설계 결정 → `docs/DECISIONS.md`에 D번호 항목 추가 (결정 / 이유 / 대안 / 포기한 것 / 보완)
- AI 결과 판정 → `docs/AI_LOG.md` 표에 한 줄 (시각 / 맡긴 것 / 수용·수정·폐기 / 근거 명령·출력)
- 담당자 답 → `docs/INTERVIEW.md` 표에 한 줄, 그리고 AGENTS.md "도메인 사실"에 `[T+분]` 형식으로 반영
- 검증 → `docs/VERIFICATION.md` 표에 한 줄

시각은 `T+분`(과제 시작 기준)으로 쓴다. 추가한 줄을 보여 주고 커밋을 제안한다:
`git add docs AGENTS.md && git commit -m "docs: <무엇을 기록했는지 한 줄>"`
