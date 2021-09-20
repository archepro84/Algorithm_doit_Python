import copy
from typing import Any, Sequence


def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)
    a.append(key)
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    # deepcopy를 하지않은 seq의 길이로 계산한다.
    return False if i == len(seq) else i


if __name__ == '__main__':
    idx = seq_search([1, 6, 2, 5, 3, 4, 7, 8], 99)
    print(idx)
