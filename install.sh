#!/usr/bin/env bash
# 현재 폴더에 하네스 파일을 복사한다. 이미 있는 파일은 덮어쓰지 않는다.
set -euo pipefail
H="$(cd "$(dirname "$0")" && pwd)"
copy() {  # copy <src> <dst>
  if [ -e "$2" ]; then echo "  skip  $2 (이미 있음)"; else mkdir -p "$(dirname "$2")"; cp -r "$1" "$2"; echo "  add   $2"; fi
}
copy "$H/templates/AGENTS.md" AGENTS.md
copy "$H/templates/CLAUDE.md" CLAUDE.md
for f in INTERVIEW DECISIONS REPORT HANDOFF SELF_BRIEF; do copy "$H/templates/$f.md" "docs/$f.md"; done
copy "$H/scripts/check_data.py" scripts/check_data.py
for s in data-check cross-review handoff self-brief; do copy "$H/.claude/skills/$s" ".claude/skills/$s"; done
[ -d .git ] || { git init -q && echo "  git init"; }
echo "완료. 다음: README/데이터 훑기 → 담당자 인터뷰 → AGENTS.md 빈칸 채우기 → 첫 커밋"
