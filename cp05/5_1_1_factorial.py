from __future__ import annotations

from typing import Any


def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구성"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    print(factorial(3))
