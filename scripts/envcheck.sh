#!/usr/bin/env bash
# 환경 기록 (아무것도 수정·설치하지 않음). 사용: bash scripts/envcheck.sh | tee docs/ENV.md
echo "# ENV $(date '+%F %H:%M %Z')"
echo "## 도구"
for c in python3 node git claude codex; do
  printf -- "- %s: " "$c"
  if command -v "$c" >/dev/null; then "$c" --version 2>&1 | head -1; else echo "없음"; fi
done
echo "## 파이썬 패키지 (O 설치됨 / X 없음)"
python3 - <<'PY'
import importlib.util as u
for m in "pandas numpy scipy sklearn matplotlib flask fastapi uvicorn pytest openpyxl requests".split():
    print("-", m, "O" if u.find_spec(m) else "X")
PY
echo "## 네트워크 (헤더만 요청, 데이터 전송 없음)"
for h in https://github.com https://pypi.org; do
  printf -- "- %s: " "$h"
  curl -sI -m 5 -o /dev/null -w '%{http_code}\n' "$h" 2>/dev/null || echo "실패"
done
echo "## 포트 3000"
if (ss -ltn 2>/dev/null || netstat -ltn 2>/dev/null || lsof -iTCP -sTCP:LISTEN -nP 2>/dev/null) | grep -q '[:.]3000 '; then echo "- 사용 중"; else echo "- 비어 있음"; fi
echo "## 데이터 파일"
find . -maxdepth 3 -type f \( -name '*.csv' -o -name '*.json' -o -name '*.xlsx' -o -name '*.txt' \) \
  -not -path './.git/*' -not -path './.claude/*' -not -path './.agents/*' -not -path './docs/*' \
  | sort | while read -r f; do printf -- "- %s (%s줄)\n" "$f" "$(wc -l < "$f" | tr -d ' ')"; done
