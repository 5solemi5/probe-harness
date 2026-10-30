# probe-harness

AI 코딩 에이전트(Claude Code / Codex)와 함께 **데이터 기반 실무 과제**를 4시간 안에 푸는 데 쓰는 범용 작업 틀입니다.
특정 시험 문제나 정답은 들어 있지 않습니다. 지침 템플릿, 문서 템플릿, 위임 프롬프트, 데이터 점검 스크립트만 있습니다.

## 30초 설치 (작업 폴더에서)
```bash
git clone --depth 1 https://github.com/5solemi5/probe-harness ~/.h && bash ~/.h/install.sh
```
`install.sh`는 현재 폴더에 아래만 복사합니다(기존 파일은 덮어쓰지 않음).
- `AGENTS.md`, `CLAUDE.md` 뼈대 (빈칸은 담당자 인터뷰 후 직접 채움)
- `docs/` 문서 템플릿: INTERVIEW · DECISIONS · REPORT · HANDOFF · SELF_BRIEF
- `scripts/check_data.py` CSV 프로파일러, `scripts/envcheck.sh` 환경 기록 (표준 도구만)
- 스킬 5개(data-check, cross-review, handoff, self-brief, verify): Claude용 `.claude/skills/`, Codex용 `.agents/skills/`
- `.gitignore`, 그리고 git 사용자 정보가 비어 있으면 이 폴더에만 중립값 설정

설치 후 할 일: `bash scripts/envcheck.sh | tee docs/ENV.md` → 담당자 인터뷰 → AGENTS.md 빈칸 채우기 → 첫 커밋.
명령이 헷갈리면 `cat ~/.h/CHEATSHEET.md`. 웹 서버 골격과 테스트 틀은 필요할 때만 복사: `~/.h/templates/serve.py`, `~/.h/templates/test_template.py`.

git clone이 안 되는 환경이면 `prompts/위임프롬프트.md`의 내용을 기억해 두었다가 직접 입력합니다.

## 원칙
1. 판정·계산은 고정 코드, AI는 초안·해석·리뷰.
2. 한 프롬프트에 한 단계. 단계마다 실행 결과로 확인.
3. 판단은 글로 남긴다(INTERVIEW, DECISIONS, 커밋 메시지).
4. 결과물은 직접 읽고 설명할 수 있어야 한다.

## 구성
```
install.sh
CHEATSHEET.md    Claude Code · Codex 명령 (설치되지 않음, 열람용)
templates/   AGENTS.md CLAUDE.md INTERVIEW.md DECISIONS.md REPORT.md HANDOFF.md SELF_BRIEF.md
             serve.py test_template.py (필요할 때만 복사)
prompts/     위임프롬프트.md  담당자질문은행.md  확인문제_답변틀.md
scripts/     check_data.py  envcheck.sh
.claude/skills/  data-check · cross-review · handoff · self-brief · verify
```

MIT License.
