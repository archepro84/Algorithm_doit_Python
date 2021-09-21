from __future__ import annotations

from typing import Any


def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현(Reverse)"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)


if __name__ == '__main__':
    print(recur(4))
