"""unittest 틀: 정상 1개 + 경계 3개. 복사해서 쓴다: cp ~/.h/templates/test_template.py tests/test_core.py
실행: python3 -m unittest discover -s tests -v
"""
import unittest

# from core import process   # 테스트할 함수로 바꾼다


def process(rows):  # 자리표시. 실제 함수를 import하면 지운다.
    return [r for r in rows if r.get("value") not in ("", "-1", None)]


class TestProcess(unittest.TestCase):
    def test_normal(self):
        rows = [{"id": "a", "value": "1"}, {"id": "b", "value": "2"}]
        self.assertEqual(len(process(rows)), 2)

    def test_empty_input(self):
        self.assertEqual(process([]), [])

    def test_sentinel_values(self):
        # 담당자 확인: -1과 빈칸은 측정 실패라 제외한다
        rows = [{"id": "a", "value": "-1"}, {"id": "b", "value": ""}, {"id": "c", "value": "3"}]
        self.assertEqual([r["id"] for r in process(rows)], ["c"])

    def test_duplicate_keys(self):
        # 같은 키가 여러 번 나올 때의 규칙을 여기에 고정한다 (예: 마지막 재측정만 남김)
        rows = [{"id": "a", "value": "1"}, {"id": "a", "value": "2"}]
        self.assertEqual(len(process(rows)), 2)  # 규칙을 정하면 기대값을 바꾼다


if __name__ == "__main__":
    unittest.main()
