"""
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 n이 주어질 때, n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 갯수를 반환하는 함수 solution을 완성해 주세요.

제한사항
괄호 쌍의 개수 N : 1 ≤ n ≤ 14, N은 정수
"""

def solution(n):
    if n ==1:
        return 1
    ls = ["()"]
    for i in ls:
        if len(ls[-1]) == 2*(n+1): # n+1개의 괄호가 출현할때까지 반복
            break
        ls.append(i+"()")
        ls.append("()"+i)
        ls.append("("+i+")") # n개의 올바른 괄호의 집합을 이용해 n+1개의 괄호를 구하려 했지만 틀린듯 하다.
    ls= [x for x in ls if len(x) == 2*n] # 내가 필요한 n개의 괄호로만 이루어진 것들을 고른다.
    ls = list(set(ls))

    return len(ls)
