'''
그래프의 구현
이번 예제에서는 그래프를 구현합니다. 명령은 총 세가지 입니다.

addEdge(v, w) : 그래프에 양방향 간선 (v, w)를 추가합니다. 이 말은 정점 v,w를 간선으로 연결한다는 말입니다.
isEdge(v, w) : v와 w가 인접해있으면 True, 아니면 False를 반환합니다.
getAdj(v) : 정점 v와 인접해있는 모든 정점을 리스트로 반환합니다. 그 순서는 관계없습니다.

요구사항
그래프를 인접행렬(행렬)을 이용하여 구현하세요.

시스템 입력 예시
myGraph = graph(3)

myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)

print(myGraph.isEdge(1, 2))
print(myGraph.isEdge(2, 3))
print(myGraph.getAdj(1))
시스템 출력 예시
True
False
[2, 3]
'''
class graph :
    def __init__(self, n) :
        '''
        정점이 n개가 있는 그래프를 생성합니다.
        '''
        self.doc = {}
        for i in range(n):
            self.doc[i+1] = ''
        
    def addEdge(self, v, w) :
        '''
        간선 (v, w)를 추가합니다
        '''
        self.doc[v] += '{}'.format(w)
        self.doc[w] += '{}'.format(v)
        
        

    def isEdge(self, v, w) :
        '''
        정점 v와 w가 인접해있으면 True, 아니면 False를 반환합니다.
        '''
        if '{}'.format(w) in self.doc[v]:
            return True
        else:
            return False

        

    def getAdj(self, v) :
        '''
        정점 v와 인접한 모든 정점을 리스트로 반환합니다.
        '''
        self.ls = []
        for i in range(len(self.doc[v])):
            self.ls.append(int(self.doc[v][i]))
        return self.ls

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myGraph = graph(3)
    
    myGraph.addEdge(1, 2)
    myGraph.addEdge(1, 3)
    
    print(myGraph.isEdge(1, 2))
    print(myGraph.isEdge(2, 3))
    print(myGraph.getAdj(1))

main()

        
    
