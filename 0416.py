#Code07-01.py
""" queue=[None for _ in range(5)]
front=rear=-1

rear+=1
queue[rear]="화사"
rear+=1
queue[rear]="솔라"
rear+=1
queue[rear]="문별"

print("-----큐상태-----")
print("[출구]<--",end='')
for i in queue:
    print(i,end=' ')
print("<--[ "입구]")"""

#Code07-02.py

""" queue=["화사","솔라","문별",None,None]
front=-1
rear=2



if __name__=="__main__":
    print("-----큐상태-----")
    print("[출구]<--",end='')
    for i in queue:
        print(i,end=' ')
    print("<--[ 입구]")
    print("--------------")
    front+=1
    deQueue=queue[front]
    queue[front]=None
    print("deQueue-->",deQueue)
    front+=1
    deQueue=queue[front]
    queue[front]=None
    print("deQueue-->",deQueue)
    front+=1
    deQueue=queue[front]
    queue[front]=None
    print("deQueue-->",deQueue)
    print("--------------")
    print()
    print("--------------")
    print("-----큐상태-----")
    print("[출구]<--",end='')
    for i in queue:
        print(i,end=' ')
    print("<--[ 입구]") """

#Code07-03,04.py

""" def isQueueFull():
    global SIZE,queue,front,rear
    if(rear==SIZE-1):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if isQueueFull():
        print("큐가 꽉 찼습니다.")
    else:
        rear+=1
        queue[rear]=data


#전역변수
SIZE=5
queue=["화사","솔라","문별","휘인",None]
front=-1
rear=3

#메인함수
if __name__=="__main__":
    print(queue)
    enQueue("선미")
    print(queue)
    enQueue("재남")
 """

#Code07-05,06.py
""" def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front==rear):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
    else:
        front+=1
        data=queue[front]
        queue[front]=None
        return data


#전역변수
SIZE=5
queue=["화사",None,None,None,None]
front=-1
rear=0

if __name__=="__main__":
    print(queue)
    retData=deQueue()
    print("추출한 데이터-->",retData)
    print(queue)
    retData=deQueue()
 """

#Code07-11.py
""" def isQueueFull():
    global SIZE,queue,front,rear
    if((rear+1)%SIZE==front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(rear==front):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if isQueueFull():
        print("큐가 꽉찼습니다.")
    else:
        rear=(rear+1)%SIZE
        queue[rear]=data

def deQueue():
    global SIZE,queue,front,rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
    else:
        front=(front+1)%SIZE
        data=queue[front]
        queue[front]=None
        return data

def peek():
    global SIZE,queue,front,rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None
    else:
        return queue[(front+1)%SIZE]


#전역 변수 부분
SIZE=int(input("큐 크기를 입력하세요==>"))
queue=[None for _ in range(SIZE)]
front=rear=0

#메인함수부분
if __name__=="__main__":
    select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")
    while(select!='X' and select!='x'):
        if select=='I' or select=='i':
            inputData=input("입력할 데이터==>")
            enQueue(inputData)
            print("큐상태:",queue)
            print("front:%d,rear:%d"%(front,rear))
        elif select=='E' or select=='e':
            popData=deQueue()
            print("추출한데이터==>",popData)
            print("스택상태:",queue)
            print("front:%d,rear:%d"%(front,rear))
        elif select=='V' or select=='v':
            retData=peek()
            print("top의 데이터확인==>",retData)
            print("스택상태:",queue)
            print("front:%d,rear:%d"%(front,rear))
        else:
            print("입력이 잘못됨")
        select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")
    print("프로그램종료!")     """

#응용예제1번

""" def isQueueEmpty():
    global SIZE,queue,front,rear
    if(rear==-1):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if isQueueEmpty():
        return None
    else:
        data=queue[front]
        queue[front]=None
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        rear-=1
    return data





#전역변수부분
SIZE=5
queue=['정국','뷔','지민','진','슈가']
front=0
rear=4
#메인함수부분
if __name__=="__main__":
    print("대기 줄 상태",queue)    
    while True:        
        if(isQueueEmpty()):
            print("식당영업종료!")
            break
        else:
            out=deQueue()
            print("%s 님 식당에 들어감"%out)
            print("대기 줄 상태",queue)    
 """

#응용예제2번
def isQueueFull():
    global SIZE,queue,rear,front
    if(rear+1)%SIZE==front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,rear,front,waitTime
    if isQueueFull():
        return
    else:
        rear=(rear+1)%SIZE
        queue[rear]=data
        if data=="('환불',4)":
            waitTime+=4
        if data=="('고장',3)":
            waitTime+=3
        if data=="('사용',9)":
            waitTime+=9
        if data=="('기타',1)":
            waitTime+=1




        

#전역변수

SIZE=6
queue=[None for _ in range(SIZE)]
front=rear=0
waitTime=0
#메인함수
if __name__=="__main__":
    while True:
        if isQueueFull():
            print("프로그램종료!")
            break
        else:
            print("귀하의 대기 예상시간은 %d분입니다."%waitTime)
            enQueue("('사용',9)")
            print("현재대기콜 -->",queue)
            print("귀하의 예상대기시간은 %d분입니다"%waitTime)
            enQueue("('고장',3)")
            print("현재대기콜 -->",queue)
            print("귀하의 예상대기시간은 %d분입니다"%waitTime)
            enQueue("('환불',4)")
            print("현재대기콜 -->",queue)
            print("귀하의 예상대기시간은 %d분입니다"%waitTime)
            enQueue("('환불',4)")
            print("현재대기콜 -->",queue)
            print("귀하의 예상대기시간은 %d분입니다"%waitTime)
            enQueue("('고장',3)")
            print("현재대기콜 -->",queue)



