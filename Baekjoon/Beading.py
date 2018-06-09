"""
Elice의 토끼는 암기력을 높이기 위해 구슬 넣기 놀이를 고안했다. 토끼는 nn개의 구슬이 있으며, 각 구슬은 1부터 nn까지의 번호를 하나씩 갖고 있다. 또한, 토끼는 양 쪽이 뚫려있고 투명하지 않은 관을 갖고 있다. 토끼는 nn개의 구슬을 이 파이프에 무작위로 넣은 후에, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 암기함으로써 암기력을 높인다.

토끼는 파이프의 왼쪽에, 혹은 오른쪽에 구슬을 넣을 수 있다. 예를 들어, 파이프의 왼쪽으로 숫자 1의 구슬을 넣고, 파이프의 오른쪽으로 숫자 3의 구슬을 넣고, 마지막으로 파이프의 왼쪽으로 숫자 2의 구슬을 넣게 되면, 최종적으로 구슬의 배치는 2 1 3 이 된다.

토끼가 nn개의 구슬을 파이프에 넣는 행위가 입력으로 주어질 때, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력하는 프로그램을 작성하시오. (단, 파이프의 길이는 nn개의 구슬을 모두 담기에 충분히 길다고 가정하자)

입력
입력의 첫 번째 줄에는 구슬의 개수 nn이 주어진다. 두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어진다. 각 줄은 두 개의 정수 aa, bb로 이루어지며, 이 뜻은 구슬 aa를 왼쪽 혹은 오른쪽으로 넣는다는 의미이다. (bb가 0이면 왼쪽, bb가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.

입력 예시
3
1 0
2 1
3 0
출력 예시
3 1 2
"""

"My Code"
i = input()
ls = []
for _ in range(int(i)):
    a,b = input().split(" ")
    if int(b) == 0:
        ls = [int(a)] + ls
        #입력받는 위치(b)가 0이면 기존 ls의 왼쪽에 더한다.
    else:
        ls = ls + [int(a)]
        #입력받는 위치(b)가 0이 아니면(=1이면) 기존 ls의 오른쪽에 더한다.
print(ls)
