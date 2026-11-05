# probe-harness

Codex CLI와 함께 **웹 서비스형 실무 과제**를 제한 시간 안에 푸는 데 쓰는 범용 작업 틀입니다.
특정 시험 문제나 정답, 완성 코드는 들어 있지 않습니다. 지침 템플릿, 기록 문서 템플릿, 스킬, 위임 프롬프트, 점검 스크립트만 있습니다.
빈칸은 과제를 받은 뒤 사용자가 직접 채웁니다.

## 30초 설치 (작업 폴더에서)
```bash
git clone --depth 1 https://github.com/5solemi5/probe-harness ~/.h && bash ~/.h/install.sh
```
`install.sh`는 현재 폴더에 아래만 복사합니다(기존 파일은 덮어쓰지 않음).
- `AGENTS.md` 뼈대 (목표·절대 규칙·스택·도메인 사실·하드 제약·최적화 기준·역할·작업 규칙·완료 조건)
- `docs/` 기록 템플릿: INTERVIEW · DECISIONS · VERIFICATION · AI_LOG · HANDOFF · SELF_BRIEF
- `scripts/check_data.py` CSV 프로파일러, `scripts/envcheck.sh` 환경 기록 (표준 도구만)
- Codex 스킬 8개(`.agents/skills/`): data-check, verify, log, cross-review, submit-gate, followup-prep, handoff, self-brief
- `.gitignore`, 그리고 git 사용자 정보가 비어 있으면 이 폴더에만 중립값 설정

설치 후: `bash scripts/envcheck.sh | tee docs/ENV.md` → 과제 README·데이터 훑기 → 담당자 질문 → AGENTS.md 빈칸 채우기 → 첫 커밋.

필요할 때만 복사:
- 웹 배포 골격: `cp -n ~/.h/templates/web/{Dockerfile,.dockerignore,.env.example} .`
- 표준 라이브러리 웹 서버·테스트 틀: `~/.h/templates/serve.py`, `~/.h/templates/test_template.py`

git clone이 안 되는 환경이면 `templates/AGENTS.md`의 제목 9개를 기억해 두었다가 직접 입력합니다.

## 스킬 사용 시점 (Codex에서 `$이름` 또는 `/skills`)
| 스킬 | 언제 |
|---|---|
| `$data-check` | 데이터를 처음 받았을 때 — 검증 규칙 후보와 담당자 질문 |
| `$verify` | "됐다"고 말하기 전 매번 |
| `$log` | 결정·AI 결과 판정·담당자 답이 생길 때마다 |
| `$cross-review` | 첫 동작 버전 이후, 제출 1시간 전 |
| `$followup-prep` | 제출 30~40분 전 — 예상 질문·근거 수집·재확인 (답은 안 씀) |
| `$submit-gate` | 제출 20~30분 전 |
| `$handoff` | 세션을 새로 열기 전 |
| `$self-brief` | 제출 직전, 후속 질문 대비 |

## 원칙
1. 판정·검증은 고정 코드, AI는 초안·구현·리뷰. 생성기와 검증기는 분리한다.
2. 한 프롬프트에 한 단계. 단계마다 실행 결과로 확인.
3. 판단은 글로 남긴다(DECISIONS, VERIFICATION, AI_LOG, 커밋 메시지).
4. 결과물은 직접 읽고 설명할 수 있어야 한다.

## 구성
```
install.sh
CHEATSHEET.md    Codex CLI 명령 (설치되지 않음, 열람용)
templates/   AGENTS.md INTERVIEW.md DECISIONS.md VERIFICATION.md AI_LOG.md HANDOFF.md SELF_BRIEF.md
             web/ (Dockerfile .dockerignore .env.example)  serve.py test_template.py
prompts/     위임프롬프트.md  담당자질문은행.md  확인문제_답변틀.md
scripts/     check_data.py  envcheck.sh
.agents/skills/  data-check · verify · log · cross-review · followup-prep · submit-gate · handoff · self-brief
```
데이터 분석형 과제용 이전 버전은 태그 `v1-data`에 있습니다.

MIT License.
