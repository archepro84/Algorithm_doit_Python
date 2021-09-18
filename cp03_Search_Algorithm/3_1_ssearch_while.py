from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    i = 0
    while True:
        if i >= len(a):
            return False
        if a[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    idx = seq_search([1, 6, 2, 5, 3, 4, 7, 8], 8)
    print(idx)
