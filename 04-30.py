#Code09-01.py
class Graph():
    def __init__ (self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]  for _ in range(size)]
    ''' self.graph=[]
        for _ in range(size) :
           tmpList[]
           for _ in range(size) :
               tmpList.append(0)
            self.graph.append(tmpList)'''

#전역 변수 선언
G1 ,G3 = None, None


#메인코드
G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

G3= Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('## G3 방향 그래프 ##')
for row in range(4):
    for ocl in range(4):
        print(G3.graph[row][col], end = ' ')
    print()

#Code09-02.py
##클래스와 함수 선언 부분#
class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

def printGraph(g):
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end = ' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end = ' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end = ' ')
        print()
    print()

#전역 변수 선언 부분 #
G1 = None
nameAry = ['문별', '솔라' , '휘인' , '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5


#메인코드부분#
gSize = 6
G1 = Graph(gSize)
G1.graph[문별][솔라] = 1 ; G1.graph[문별][휘인] = 1
G1.graph[솔라][문별] = 1 ; G1.graph[솔라][쯔위] = 1
G1.graph[휘인][문별] = 1 ; G1.graph[휘인][쯔위] = 1
G1.graph[쯔위][솔라] = 1 ; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1 ; G1.graph[쯔위][화사] = 1
G1.graph[선미][쯔위] = 1 ; G1.graph[선미][화사] = 1
G1.graph[화사][쯔위] = 1 ; G1.graph[화사][선미] = 1

print('## G1 무방향 그래프##')
printGraph(G1)

#Code09-03.py
class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

#전역 변수 선언 부분
G1 = None
stack = []
visitedAry = []

#메인코드
G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

current = 0
stack.append(current)
visitedAry.append(current)

while(len(stack) != 0):
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문순서 -->', end = ' ')
for i in visitedAry :
    print(chr(ord('A')+i), end = ' ')

#Code09-04.py
gSize = 6
def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while(len(stack) != 0):
        next = None
        for vertex in range(4):
            if g.graph[current][vertex] == 1:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break

        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()
    
    if findVtx in visitedAry :
        return True
    else:
        return False

#Code09-05.py
#클래스와 함수 선언 부분
class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end = ' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end = ' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end = ' ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while(len(stack) != 0):
        next = None
        for vertex in range(4):
            if g.graph[current][vertex] == 1:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break

        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()
    
    if findVtx in visitedAry :
        return True
    else:
        return False
    


#전역 변수 선언
G1 = None
nameAry = ['춘천' , '서울' , '속초' , '대전' , '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5


#메인 코드 부분
gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11;G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[춘천][서울] = 11; G1.graph[춘천][서울] = 12; G1.graph[대전][광주] = 20;G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print('##자전거 도로 건설을 위한 전체 연결도##')
printGraph(G1)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize) :
    for k in range (gSize) :
        if G1.graph[i][k] !=0 :
            edgeAry.append([G1.graph[i][k],i,k])

from operator import itemgetter
edgeAry = sorted(edgeAry, key = itemgetter(0), reverse = True)

newAry = []
for i in range(0, len(edgeAry),2):
    newAry.append(edgeAry[i])

index = 0
while (len(newAry)> gSize-1):
    start = newAry[index][1]
    end = newAry[index][2]
    saveCost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN :
        del(newAry[index])
    else:
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index +=1

print('## 최소 비용의 자전거 도로 연결도 ##')
printGraph(G1)



    