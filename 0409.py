#Code06-01.py
""" stack=[None,None,None,None,None]
top=-1
top+=1
stack[top]="커피"
top+=1
stack[top]="녹차"
top+=1
stack[top]="꿀물"
print("------스택상태------")
for i in range(len(stack)-1,-1,-1):
    print(stack[i]) """
#Code06-02.py
""" stack=["커피","녹차","꿀물",None,None]
top=2
print("------스택상태------")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
print("------------------")
data=stack[top]
stack[top]=None
top-=1
print("pop-->",data)

data=stack[top]
stack[top]=None
top-=1
print("pop-->",data)

data=stack[top]
stack[top]=None
top-=1
print("pop-->",data)
print("------------------")
print("------스택상태------")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])


 """

 #Code06-03.py
""" 
def isStackFull():
     global SIZE,stack,top
     if top>= SIZE-1:
         return True
     else:
         return False

SIZE=5

stack=["커피","녹차","꿀물","콜라","환타"]
top=4
print("스택이 꽉찼는지 유무 ==>",isStackFull()) """
#Code06-04.py
""" def isStackFull():
     global SIZE,stack,top
     if top>= SIZE-1:
         return True
     else:
         return False

def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        print("스택이 꽉찼습니다.")
        return
    top+=1
    stack[top]=data

SIZE=5

stack=["커피","녹차","꿀물","콜라",None]
top=3

print(stack)
push("환타")
print(stack)
push("게토레이")
 """

#Code06-05.py
""" def isStackEmpty():
    global SIZE,stack,top
    if top==-1:
        return True
    else:
        return False

SIZE=5

stack=[None for _ in range(SIZE)]
top=3
print("스택이 비어있는지 여부 ==>",isStackEmpty()) """

#Code 06-06.py
""" def isStackEmpty():
    global SIZE,stack,top
    if top==-1:
        return True
    else:
        return False

def pop():
    global SIZE,stack,top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    data=stack[top]
    stack=None
    top-=1
    return data

SIZE=5
stack=["커피",None,None,None,None]
top=0

print(stack)
retData=pop()
print("추출한데이터-->",retData)
print(stack)
retData=pop()


 """

 #SelfStudy 6-1

""" def push(data):
     global SIZE,stack,top
     if top>=SIZE-1:
        print("스택이 꽉찼습니다.")
     else:
         top+=1
         stack[top]=data 


#전역변수
SIZE=5
stack=["커피","녹차","꿀물",'콜라',None]
top=3

print(stack)
push("환타")
print(stack)
push("게토레이")
 """


#Selfstudy 06-02
""" def pop():
    global SIZE,stack,top
    if top==-1:
        print("스택이 비었습니다.")
        return None
    data=stack[top]
    stack[top]=None
    top-=1
    return data
    

SIZE=5
stack=['커피',None,None,None,None]
top=0

print(stack)
retData=pop()
print("추출한 데이터 -->",retData)
print(stack)
retData=pop() 
 """

#Code06-07


""" def isStackEmpty():
    global SIZE,stack,top
    if(top==-1):
        return True
    else:
        return False

def peek():
    global SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 꽉찼습니다.")
        return None
    return stack[top]
SIZE=5
stack=["커피","녹차","꿀물",None,None]
top=2
print(stack)
retData=peek()
print("top의 데이터확인 -->",retData)
print(stack) """


#Code06-08.py
""" def isStackFull():
    global SIZE,stack,top
    if(top>=SIZE-1):
        return True
    else:
        return False

def isStackEmtpy():
    global SIZE,stack,top
    if(top==-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if isStackFull():
        print("스택이 꽉찼습니다.")
    top+=1
    stack[top]=data

def pop():
    global SIZE,stack,top
    if isStackEmtpy():
        print("스택이 비었습니다.")
        return None
    data=stack[top]
    stack[top]=None
    top-=1
    return data   

def peek():
    if isStackEmtpy():
        print("스택이 비었습니다.")
        return None
    else:
        return stack[top]

#전역변수부분
SIZE=int(input("SIZE크기를 입력하세요:"))
stack=[None for _ in range(SIZE)]
top=-1

#메인함수부분
if __name__=="__main__":
    select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")
    while(select!='X' and select!='x'):
        if select=='I' or select=='i':
            inputData=input("입력할 데이터==>")
            push(inputData)
            print("스택상태:",stack)
        elif select=='E' or select=='e':
            popData=pop()
            print("추출한데이터==>",popData)
            print("스택상태:",stack)
        elif select=='V' or select=='v':
            retData=peek()
            print("top의 데이터확인==>",retData)
            print("스택상태:",stack)

        else:
            print("입력이 잘못됨")
        select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")
    print("프로그램종료!")    
 """

#Code06-10.py
""" def isStackEmpty():
    if(top==-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if(top==SIZE-1):
        print("스택이 꽉찼습니다.")
    top+=1
    stack[top]=data

def pop():
    global SIZE,stack,top
    data=stack[top]
    stack[top]=None
    top-=1
    return data


def checkBracket(expr):
    global SIZE,stack,top
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>': 
            out=pop()
            if ch==')' and out=='(':
                pass
            elif ch==']' and out=='[':
                pass
            elif ch=='}' and out=='{':
                pass
            elif ch=='>' and out=='<':
                pass
            else:
                return False
        else:
            pass
    if isStackEmpty():
        return True
    else:
        return False
        
#전역변수
SIZE=100
stack=[None for _ in range(SIZE)]
top=-1

#메인함수

if __name__=="__main__":
    exprAry=['(A+B)',')A+B(','((A+B)-C','(A+B]','(<A+{B+C}/[C*D]>)']
    for expr in exprAry:
        top=-1
        result=checkBracket(expr)
        print(expr,'==>',result)
 """


#응용예제1번
""" 
def pop():
    global stack,top
    data=stack[top]
    stack[top]=None
    top-=1
    return data

stack=['우리집','주황','초록','파랑','보라','빨강','노랑','과자집']
top=-1

if __name__=="__main__":
    print("과자집에 가는길:",end='')
    for data in stack:
        if data=='우리집':
            pass
        else:
            if data!=stack[-1]:
                print(data,end='--> ')
             else:
                print(data)
    print("우리집에 오는길:",end='')
    for data in stack:
        out=pop()
        if out=='과자집':
            pass
        else:
            if out!='우리집':
                print(out,end='--> ')
            else:
                print(out)
     """

#응용예제 2번
""" def pop():
    global SIZE,stack,top,my_list
    data=stack[top]
    stack[top]=None
    top-=1
    return data
def reVersStack():
    global SIZE,stack,top,my_list
    for data in stack:
        out=pop()
        my_list.append(out)
    for i in my_list:
        print(i,end='')
#전역변수
poem="진달래꽃\n나보기가 역겨워\n가실 때에는\n말없이 고이 보내드리오리다."
stack=list(poem)
SIZE=len(stack)
top=-1
my_list=[]

#메인함수
if __name__=="__main__":
    print("----원본----")
    print(poem)
    print("----거꾸로 처리된 결과----")
    reVersStack()        

 """

 