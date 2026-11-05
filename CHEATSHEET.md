# 명령 치트시트 (Codex CLI)

표기: ✅ 공식 문서에서 확인 / ⚠ 최신 문서 기준, 시험 버전에서 직접 확인 / ❓ 미확인
시작 직후 30초: `codex --version` → Codex에서 `/` 를 입력해 명령 목록을 본다. `/status`로 모델·권한 확인.

## Codex CLI (v0.163.0)
| 할 일 | 명령 | |
|---|---|---|
| 시작 | `codex`, 쓰기 허용 조합 `codex -s workspace-write -a on-request` | ✅ |
| 모델 | `/model` (0.163은 메뉴에서 선택, 인라인 인자는 0.164부터) | ✅ |
| 승인·권한 | **`/permissions`** (예전 이름 `/approvals`) | ⚠ |
| 계획 | `/plan [프롬프트]` | ✅ |
| 새 대화 / 압축 / 상태 | `/new` / `/compact` / `/status` | ✅ |
| 변경 보기 / 리뷰 | `/diff` / `/review` | ✅ |
| 스킬 | `/skills` 또는 `$data-check`, `$verify`, `$log`, `$submit-gate` … (`.agents/skills/` 에서 찾음) | ⚠ |
| 이어하기 | `/resume`, 셸에서 `codex resume` | ✅ |
| 비대화 실행 | `codex exec "프롬프트"` — 기본은 **읽기 전용**. 쓰려면 `-s workspace-write` | ✅ |
| exec 결과 저장 | `-o 파일` | ✅ |
| 하지 말 것 | `codex update`·업데이트 권유 수락 (**규정 금지**), `/feedback` (로그 전송), `--yolo` | |

AGENTS.md는 짧게: 루트부터 현재 폴더까지의 AGENTS.md를 이어 붙이고 합계 32 KiB에서 자른다. ✅

## 웹 미리보기
- 서버는 `0.0.0.0:3000` 에 띄운다. `127.0.0.1` 이면 미리보기에 안 보일 수 있다.
- 확인: `curl -s localhost:3000/healthz` (경로는 AGENTS.md 완료 조건대로)
- 오래 도는 서버는 AI 밖 별도 터미널 탭에서 직접 실행한다

## Docker
- `docker build -t app . && docker run --rm -p 3000:3000 --env-file .env app`
- 빌드가 안 되면 사유를 실행 안내 문서에 기록한다
- 포트가 이미 쓰이면: `lsof -i :3000` → `kill <PID>`

## git (증거 남기기)
- `git add -A && git commit -m "무엇을, 왜 + 결과 숫자"` — 단계마다
- AI가 망가뜨렸을 때: `git diff` 로 보고 `git restore <파일>` 또는 `git revert <커밋>`
- 시험 중 **push 금지, GitHub 로그인 금지**
