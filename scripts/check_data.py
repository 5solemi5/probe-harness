#!/usr/bin/env python3
"""CSV 데이터 계약 점검 (표준 라이브러리만). 분석·결론은 하지 않는다.

사용법: python3 scripts/check_data.py data/            (폴더 안 모든 .csv)
        python3 scripts/check_data.py a.csv b.csv --keys lot_id,wafer_no

파일별로 행 수, 열별 결측·고유값 수·숫자 범위·의심 값(-1, -999, 9999, 0 비율, 빈 문자열),
날짜처럼 보이는 열의 최소~최대, 지정한 키의 중복 수를 출력한다.
"""
import argparse
import csv
import glob
import os
import re
from collections import Counter

SENTINELS = {"-1", "-9", "-99", "-999", "-9999", "9999", "99999", "NA", "N/A", "null", "NULL", "None", "nan", "NaN", "?"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def as_float(v):
    try:
        return float(v)
    except ValueError:
        return None


def profile(path, keys):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    print(f"\n## {os.path.basename(path)} — {len(rows)}행, {len(rows[0]) if rows else 0}열")
    if not rows:
        return
    print("| 열 | 결측/빈값 | 고유값 | 숫자범위 | 의심값 | 상위값 |")
    print("|---|---|---|---|---|---|")
    for col in rows[0].keys():
        vals = [r[col] for r in rows]
        empty = sum(1 for v in vals if v is None or v.strip() == "")
        cnt = Counter(vals)
        nums = [x for x in (as_float(v) for v in vals if v) if x is not None]
        rng = f"{min(nums):g}~{max(nums):g}" if nums and len(nums) > 0.9 * (len(vals) - empty) else ""
        if not rng and sum(1 for v in vals if v and DATE_RE.match(v)) > 0.9 * len(vals):
            ds = sorted(v for v in vals if v)
            rng = f"{ds[0]} ~ {ds[-1]}"
        sus = {v: c for v, c in cnt.items() if v in SENTINELS}
        if nums:
            neg = sum(1 for x in nums if x < 0)
            zero = sum(1 for x in nums if x == 0)
            if neg:
                sus["음수"] = neg
            if zero > 0.05 * len(nums):
                sus["0"] = zero
        top = ", ".join(f"{k}({c})" for k, c in cnt.most_common(3))
        print(f"| {col} | {empty} | {len(cnt)} | {rng} | {sus or ''} | {top[:60]} |")
    present = [k for k in keys if k in rows[0]]
    if present:
        kc = Counter(tuple(r[k] for k in present) for r in rows)
        dup = sum(c - 1 for c in kc.values() if c > 1)
        print(f"\n키 {present} 중복 행: {dup} (고유 키 {len(kc)})")
    full_dup = sum(c - 1 for c in Counter(tuple(r.values()) for r in rows).values() if c > 1)
    print(f"완전히 같은 행 중복: {full_dup}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--keys", default="", help="중복을 셀 키 열 (쉼표 구분)")
    a = ap.parse_args()
    files = []
    for p in a.paths:
        files += sorted(glob.glob(os.path.join(p, "*.csv"))) if os.path.isdir(p) else [p]
    keys = [k for k in a.keys.split(",") if k]
    for f in files:
        profile(f, keys)
    print("\n※ 이 출력은 '확인 필요' 목록입니다. 의심값의 의미는 담당자에게 확인하세요.")


if __name__ == "__main__":
    main()
