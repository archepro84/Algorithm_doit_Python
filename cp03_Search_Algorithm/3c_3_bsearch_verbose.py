from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    pl, pr = 0, len(a) - 1
    pc = (pl + pr) // 2

    while True:
        print(f'pc : {pc}')
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            return -1
        pc = (pl + pr) // 2


if __name__ == '__main__':
    print(bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 7))
