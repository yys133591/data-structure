#Code08-01.py
""" class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None

node1=TreeNode()
node1.data='화사'

node2=TreeNode()
node2.data='솔라'
node1.left=node2

node3=TreeNode()
node3.data='문별'
node1.right=node3

node4=TreeNode()
node4.data='휘인'
node2.left=node4

node5=TreeNode()
node5.data='쯔위'
node2.right=node5

node6=TreeNode()
node6.data='솔라'
node3.left=node6

print(node1.data,end='')
print()
print(node1.left.data,node1.right.data,end='')
print()
print(node1.left.left.data,node1.left.right.data,node1.right.left.data,end='')
 """


#Code08-02.py
""" 
class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None

node1=TreeNode()
node1.data='화사'

node2=TreeNode()
node2.data='솔라'
node1.left=node2

node3=TreeNode()
node3.data='문별'
node1.right=node3

node4=TreeNode()
node4.data='휘인'
node2.left=node4

node5=TreeNode()
node5.data='쯔위'
node2.right=node5

node6=TreeNode()
node6.data='선미'
node3.left=node6

def preorder(node):
    if node==None:
        return
    print(node.data,end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end='->')
    inorder(node.right)

def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end='->')

print('전위순회',end=' ')
preorder(node1)
print('끝')

print('중위순회',end=' ')
inorder(node1)
print('끝')

print('후   위순회',end=' ')
postorder(node1)
print('끝')
 """

#Code08-03.py
""" 
class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None
    
memory=[]
root=None
nameArray=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

node=TreeNode()
node.data=nameArray[0]
root=node
memory.append(None)

for name in nameArray[1:]:
    node=TreeNode()
    node.data=name
    current=root
    while True:
        if name<current.data:
            if name<current.data:
                if current.left==None:
                    current.left=node
                    break
        else:
            if current.right ==None:
                current.right=node
                break
            current=current.right
    memory.append(node)
print("이진 탐색 트리 구성 완료!") """

#Code08-04.py

""" class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None
    
memory=[]
root=None
nameArray=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

node=TreeNode()
node.data=nameArray[0]
root=node
memory.append(None)

for name in nameArray[1:]:
    node=TreeNode()
    node.data=name
    current=root
    while True:
        if name<current.data:
            if name<current.data:
                if current.left==None:
                    current.left=node
                    break
        else:
            if current.right ==None:
                current.right=node
                break
            current=current.right
    memory.append(node)

findName='마마무'

current=root
while True:
    if findName==current.data:
        print(findName,'을(를) 찾음.')
        break
    elif findName <current.data:
        if current.left==None:
            print(findName,'이(가) 트리에 없음')
            break
        current=current.left
    else:
        if current.right==None:
            print(findName,'이(가) 트리에 없음')
            break
        current=current.right
 """

#Code08-04.py
""" class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None
    
memory=[]
root=None
nameArray=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

node=TreeNode()
node.data=nameArray[0]
root=node
memory.append(None)

for name in nameArray[1:]:
    node=TreeNode()
    node.data=name
    current=root
    while True:
        if name<current.data:
            if name<current.data:
                if current.left==None:
                    current.left=node
                    break
        else:
            if current.right ==None:
                current.right=node
                break
            current=current.right
    memory.append(node)

deleteName='마마무'

current=root
parent=None
while True:
    if deleteName==current.data:
        if current.left==None and current.right==None:
            if parent.left==current:
                parent.left=None
            else:
                parent.right=None
            del(current)
        elif current.left !=None and current.right==None:
            if parent.left==current:
                parent.left=current.left
            else:
                parent.right=current.left
            del(current)
        elif current.left==None and current.right != None:
            if parent.left==current:
                parent.left==current
            else:
                parent.right=current.right
            del(current)

        print(deleteName,'이(가) 삭제됨')
        break
    elif deleteName <current.data:
        if current.left ==None:
            print(deleteName,'이(가) 트리에 없음')
            break
        parent=current
        current=current.left
    else:
        if current.right==None:
            print(deleteName,'이(가) 트리에 없음')
            break
        parent=current
        current=current.right
 """

#Code08-05.py
""" class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None

memory=[]
root=None
nameArray=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

node=TreeNode()
node.data=nameArray[0]
root=node
memory.append(node)

for name in nameArray[1:]:
    node=TreeNode()
    node.data=name
    current=root
    while True:
        if name < current.data:
            if current.left==None:
                current.left=node
                break
            current=current.left
        else:
            if current.right==None:
                current.right=node
                break
            current=current.right
    memory.append(node)
 """

#Code 08-06.py
""" 
class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None

memory=[]
rootBook,rootAuth=None,None
import random
bookAry=[['어린왕자','셍떽쥐베리'],['이방인','까뮈'],['부활','톨스토이'],
        ['단테','신곡'],['돈키호테','세르반데스'],['동물농장','조지오웰'],
        ['데미안','헤르만헤세'],['파우스트','괴테'],['대지','펄벅']]
bookAry=random.shuffle(bookAry)

node=TreeNode()
node.data=bookAry[0][0]
rootBook=node
memory.append(node)

for book in bookAry[1:]:
    name=book[0]
    node=TreeNode()
    node.data=name

    current=rootBook
    while True:
        if name<current.data:
            if current.left==None:
                current.left=node
                break
            current=current.left
        else:
            if current.right==None:
                current.right=node
                break
            current=current.right
    memory.append(node)
print("책 이름 트리 구성 완료")

node=TreeNode()
node.data=bookAry[0][1]
rootAuth=node
memory.append(node)

for book in bookAry[1:]:
    name=book[1]
    node=TreeNode()
    node.data=name
    current=rootAuth
    while True:
        if name<current.data:
            if current.left==None:
                current.left=node
                break
            current=current.left
        else:
            if current.right==None:
                current.right=node
                break
            current=current.right
    memory.append(node)
print("작가 이름 트리 구성 완료!")

bookOrAuth=int(input("책검색(1), 작가검색(2)-->"))
findName=input("검색할 책 또는 작가-->")

if bookOrAuth==1:
    root=rootBook
else:
    root=rootAuth
current=root
while True:
    if findName==current.data:
        print(findName,'을(를) 찾음')
        findYN=True
        break
    elif findName<current.data:
        if current.left==None:
            print(findName,'이(가) 목록에 없음')
            break
        current=current.left
    else:
        if current.right==None:
            print(findName,'이(가) 목록에 없음')
            break
        current=current.right """

