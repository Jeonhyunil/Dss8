"""
quick sort
quick sort를 구현하는 프로그램을 작성하세요.

입력
첫 번째 줄에 nn개의 숫자가 주어집니다.

출력
오름차순으로 정렬된 결과를 출력합니다.

입력 예시
10 2 3 4 5 6 9 7 8 1
출력 예시
1 2 3 4 5 6 7 8 9 10
"""

#My Code
def left_side(s):
    if len(s) <= 1:
        return s
    pivot = s[len(s)//2]
    middle = [x for x in s if x == pivot ]
    left = [x for x in s if x < pivot]
    right = [x for x in s if x > pivot]

    return left_side(left) + middle + right_side(right)

def right_side(s):
    if len(s) <= 1:
        return s
    pivot = s[len(s)//2]
    middle = [x for x in s if x == pivot ]
    left = [x for x in s if x < pivot]
    right = [x for x in s if x > pivot]

    return left_side(left) + middle + right_side(right)

def quick_sort(s):
    pivot = s[len(s)//2]
    middle = [x for x in s if x == pivot ]
    left = [x for x in s if x < pivot]
    right = [x for x in s if x > pivot]

    return left_side(left) + middle + right_side(right)
