#!/usr/bin/env bash
# 현재 폴더에 하네스 파일을 복사한다. 이미 있는 파일은 덮어쓰지 않는다. (Codex 전용)
set -euo pipefail
H="$(cd "$(dirname "$0")" && pwd)"
copy() {  # copy <src> <dst>
  if [ -e "$2" ]; then echo "  skip  $2 (이미 있음)"; else mkdir -p "$(dirname "$2")"; cp -r "$1" "$2"; echo "  add   $2"; fi
}
[ -e AGENTS.md ] && echo "  ! 기존 AGENTS.md 유지됨 — ~/.h/templates/AGENTS.md 를 보고 필요한 규칙을 직접 덧붙일 것"
copy "$H/templates/AGENTS.md" AGENTS.md
for f in INTERVIEW DECISIONS VERIFICATION AI_LOG HANDOFF SELF_BRIEF; do copy "$H/templates/$f.md" "docs/$f.md"; done
copy "$H/scripts/check_data.py" scripts/check_data.py
copy "$H/scripts/envcheck.sh" scripts/envcheck.sh
for s in "$H"/.agents/skills/*/; do
  s="$(basename "$s")"
  copy "$H/.agents/skills/$s" ".agents/skills/$s"   # Codex는 .agents/skills 를 읽는다
done
[ -e .gitignore ] || { printf '__pycache__/\n*.pyc\n.env\n.h/\n.pytest_cache/\n' > .gitignore; echo "  add   .gitignore"; }
[ -d .git ] || { git init -q && echo "  git init"; }
# 새 샌드박스는 git 사용자 정보가 비어 첫 커밋이 실패한다. 이 폴더에만(--local) 중립값을 둔다.
git config user.name  >/dev/null || git config --local user.name  "candidate"
git config user.email >/dev/null || git config --local user.email "candidate@example.invalid"
echo "완료. 다음: bash scripts/envcheck.sh | tee docs/ENV.md → 과제 README·데이터 훑기 → 담당자 질문 → AGENTS.md 빈칸 직접 채우기 → 첫 커밋"
echo "웹 골격이 필요하면: cp -n ~/.h/templates/web/{Dockerfile,.dockerignore,.env.example} ."
echo "프롬프트: cat ~/.h/prompts/위임프롬프트.md   명령: cat ~/.h/CHEATSHEET.md"
