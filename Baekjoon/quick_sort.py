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
    if len(s) <= 1: # 기저조건 = 문장의 길이가 1보다 작거나 같으면 그냥 출력
        return s
    pivot = s[len(s)//2] # 문장의 중간쯤의 숫자를 pivot으로 설정
    middle = [x for x in s if x == pivot ] # pivot이 여러개일 수 있으므로 골라내준다.
    left = [x for x in s if x < pivot] # pivot보다 작은 숫자들을 left에 저장
    right = [x for x in s if x > pivot] # pivot보다 큰 숫자들을 right에 저장

    return left_side(left) + middle + right_side(right) # left와 right 들은 각각에 위치에 맞는 함수(left_side(), right_side())로 재귀시켜준다.

def right_side(s): # 위와 마찬가지
    if len(s) <= 1:
        return s
    pivot = s[len(s)//2]
    middle = [x for x in s if x == pivot ]
    left = [x for x in s if x < pivot]
    right = [x for x in s if x > pivot]

    return left_side(left) + middle + right_side(right)

def quick_sort(s): # 위와 마찬가지
    pivot = s[len(s)//2]
    middle = [x for x in s if x == pivot ]
    left = [x for x in s if x < pivot]
    right = [x for x in s if x > pivot]

    return left_side(left) + middle + right_side(right)
