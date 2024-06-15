"""
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNode(start):
    current=start
    if current.link==None:
        return
    print(current.data,end=' ')
    while current.link !=None:
        current=current.link
        print(current.data,end=' ')

def insertNode(indexData,insertData):
    global memory,head,current,pre
    if indexData>len(Btslist):
        print("잘못된위치입니다.")
    if head.data==Btslist[indexData]:
        node=Node()
        node.data=insertData
        node.link=head
        head=node
        return
    current=head
    while current.link !=None:
        pre=current
        current=current.link
        if current.data==Btslist[indexData]:
            node=Node()
            node.data=insertData
            node.link=current
            pre.link=node
            return
        node=Node()
        node.data=insertData
        current.link=node    
        
    print("%s이(가) 성공적으로 %d번째 위치에 삽입되었습니다." %insertData %indexData)
    
##전역변수
memory=[]
Btslist=['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']
head,pre,current=None,None,None

#메인함수 부분#

if __name__=="__main__":
    node=Node()
    node.data=Btslist[0]
    head=node
    memory.append(node)
    for data in Btslist[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        memory.append(node)

    print("BTS 멤버 리스트:%s"%Btslist)
    insertMember=input("삽입할 멤버의 이름을 입력하세요:")
    memberInDex=int(input("삽입할 위치(인덱스)를 입력하세요:"))
    insertNode(memberInDex,insertMember)
    print("삽입 후 BTS 멤버 리스트: %s"%printNode(head))

"""



"""
###
memory=[]

def addNum(number):
    memory.append(None)
    memLen=len(memory)
    memory[memLen-1]=number

##메인 함수 부분##

if __name__=="__main__":
    while True:
        insertNum=int(input("추가할 값을 입력하세요(종료하려면'0'을 입력하세요):"))
        if insertNum==0:
            break
        print(f"삽입할 항목={insertNum}")
        addNum(insertNum)
        memory.sort()
        print('->'.join(map(str,memory)))
"""
"""
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current==None:
        return
    print(current.data,end=" ")
    while current.link !=None:
        current=current.link
        print(current.data,end=" ")

def makeSimpleLinkedList(nameEmail):
    global memory,head,pre,current
    node=Node()
    node.data=nameEmail
    memory.append(node)
    if head==None:
        head=node
        return
    if head.data[1]>nameEmail[1]:
        node.link=head
        return
    current=head
    while current.link !=None:
        pre=current
        current=current.link
        if current.data[1]>nameEmail[1]:
            pre.link=node
            node.link=current
            return
    current.link=node
memory=[]
head,current,pre=None,None,None
if __name__=="__main__":

    while True:
        name=input("이름-->")
        if name == '' or name == None :
            break
        email=input("이메일-->")
        makeSimpleLinkedList([name,email])
        printNodes(head)
        print()
        """

##원형 리스트 ##
"""
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current.link ==None:
        return
    print(current.data,end=' ')
    while current.link !=start: ##원형리스트 프린트할때는 None 대신 start
        current=current.link
        print(current.data,end=' ')
    print()

def insertNode(findData,insertData):
    global memory,head,current,pre
    if head.data ==findData:
        node=Node()
        node.data=insertData
        node.link=head
        last=head
        while last.link !=head:
            last=last.link
            last.link=node
        head=node
        return
    current=head
    while current.link !=head:
        pre=current
        current=current.link
        if current.data==findData:
            node=Node()
            node.data=insertData
            node.link=current
            pre.link=node
            return
    
    node=Node()
    node.data=insertData
    node.link=head
    current.link=node


        


##전역변수##
memory=[]
head,current,pre=None,None,None
"""
#예제1번
""" class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current.link==None:
        return
    print("%s편의점, 거리:%f"%(chr(current.data[0]),current.data[1]))
    while current.link !=start:
        current=current.link
        print("%s편의점, 거리:%f"%(chr(current.data[0]),current.data[1]))

import random 
import math
## 전역변수##
tuple_list=()
memory=[]
distance_list=[]
head,current,pre=None,None,None

if __name__=="__main__":
    for i in range(10):
        x=random.randint(1,100)
        y=random.randint(1,100)
        tuple_list=(i+65,x,y)
        distance=math.sqrt(x*x+y*y)
        distance_list.append([i+65,distance])
    distance_list.sort(key=lambda x:x[1])
    node=Node()
    node.data=distance_list[0]
    head=node
    node.link=head
    memory.append(node)

    for data in distance_list[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        node.link=head
        memory.append(node)
    printNodes(head)
 """

##예제2번
""" 
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current.link ==None:
        return
    print(current.data,end=' ')
    while current.link!=start:
        current=current.link
        print(current.data,end=' ')
 

def reVerseprint(last):
    current=last
    if current.link ==None:
        return
    print(current.data,end=' ')
    while current.link!=last:
        if current.data==head.data:
            break
        else:
            current=current.link
            print(current.data,end=' ')
 
    






##전역변수##
memory=[]
head,pre,current=None,None,None
dataArray=['다현','정연','쯔위','사나','지효']

##메인함수##

if __name__=="__main__":
    node=Node()
    node.data=dataArray[0]
    head=node
    node.link=head
    memory.append(node)

    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        node.link=head
        memory.append(node)
    print("정방향-->",end=" ")
    printNodes(head)
 
    for data in dataArray[-2:-5:-1]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        node.link=head    
    print()
    print("역방향-->",end=" ")
    reVerseprint(memory[4])

 """

""" def poemprint(poem_wirte):
    print("원문")
    print(poem_wirte)
def countNumber(poem_write):
    poemList=list(poem_write)
    List2={}
    for i in poemList:
        if i in List2:
            List2[i]+=1
        else:
            List2[i]=1
    for i,j in List2.items():
        if j>=4:
            if i==' ' or i=='.':
                pass
            else:
                print("%s--> %d"%(i,j))
            



poem="나 보기가 역겨워 가실 때에는 말없이 고이 보내드리오리다.\n영변(寧邊)에 약산(藥山) 진달래꽃 아름 따다 가실 길에 뿌리오리다.\n가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서.\n나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다."

if __name__=="__main__":
    poemprint(poem)
    print("-----------------")
    print("문자 빈도수(4회이상)")
    print("-----------------")
    countNumber(poem)
    

 """

#Stack 복습
"""
stack=[None,None,None,None,None]
top=-1

top+=1
stack[top]="커피"

top+=1
stack[top]="녹차"

top+=1
stack[top]="꿀물"

print("-----스택상태-----")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
