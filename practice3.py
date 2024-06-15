#Code10-1.py
""" def openBox():
    print("종이 상자를 엽니다.^^")
    openBox()
openBox() """

#Code10-2.py
""" def openBox():
    global count
    print("종이상자를엽니다.")
    count-=1
    if count==0:
        print("**반지를 넣고 반환합니다.")
        return
    openBox()
    print("종이 상자를 닫습니다.")
count=10
openBox() """

#Code10-3.py
""" def addNumber(num):
    if num<=1:
        return 1
    return addNumber(num-1)+num
print(addNumber(10))
 """
#Code10-4.py
""" def factorial(num):
    if num<=1:
        print('1 반환')
        return 1
    print("%d * %d! 호출"%(num,num-1))
    retVal=factorial(num-1)

    print("%d * %d!(=%d반환)"%(num,num-1,retVal))
    return num*retVal
print('\n5!=',factorial(5))
 """

#Code10-5.py
""" def countDown(n):
    if n==0:
        print('발사!!')
    else:
        print(n)
        countDown(n-1)

countDown(5) """

#Code10-6.py
""" def printStar(n):
    if n>0:
        printStar(n-1)
        print('*'*n)
printStar(5)        
 """
#Code10-7.py
""" from operator import index

def gugu(dan,num):
    ex=f"{dan}*{num}={dan*num}"
    print(ex.rjust(10," "),end='')
    if dan <9:
        gugu(dan+1,num)
for num in range(1,10):
    gugu(2,num)
    print() """

#Code10-8.py
""" tab=''
def pow(x,n):
    global tab
    tab+=' '
    if n==0:
        return 1
    print(tab + f"{x}*{x}^{n}-1")
    return x*pow(x,n-1)
print('2^4')
pow(2,4) """

#Code10-9.py
""" import random
def arySum(arr,n):
    if n<=0:
        return arr[0]
    return arySum(arr,n-1)+arr[n]

ary=[random.randint(0,255)for _ in range(random.randint(10,20))]
print(ary)
print(f'배열합계-->{arySum(ary,len(ary)-1)}')
    
 """

#Code10-10.py
""" def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print("피보나치 수--> 0 1",end=' ')
for i in range(2,20):
    print(fibo(i),end=' ') """

#Code10-11.py
""" def palindorme(pStr):
    if len(pStr) <=1:
        return True
    if pStr[0] != pStr[-1]:
        return False
    
    return palindorme(pStr[1:len(pStr)-1])

strAry=["reaver","kayak","Borrow or rob","주유소의 소유주","야 너 이번 주 주번이 너야","살금 살금"]

for testStr in strAry:
    print(testStr,end='-->')
    testStr=testStr.lower().replace(" ","")
    if palindorme(testStr):
        print("O")
    else:
        print("X") """

#Code10-12.py
""" from tkinter import *

window=Tk()
canvas=Canvas(window,height=1000,width=1000,bg='white')
canvas.pack()

cx=1000/2
cy=1000/2
r=400
canvas.create_oval(cx-r,cy-r,cx+r,cy+r,width=2,outline="red")

window.mainloop()
 """

""" from tkinter import *

def drawCircle(x,y,r):
    global count
    count+=1
    canvas.create_oval(x-r,y-r,x+r,y+r)
    canvas.create_text(x,y-r,text=str(count),font=('',30))
    if r>=radius/2:
        drawCircle(x-r//2,y,r//2)
        drawCircle(x+r//2,y,r//2)

count=0
wSize=1000
radius=400

window=Tk()
canvas=Canvas(window,height=wSize,width=wSize,bg='white')

drawCircle(wSize//2,wSize//2,radius)
canvas.pack()
window.mainloop()
 """

#응용예제1.py
def ten_by_two(n):
    if n>=1:
        ten_by_two(n//2)
        print(n%2,end='')

def ten_by_eight(n):
    if n>=8:
        ten_by_eight(n//8)
        print(n%8,end='')
    else:
        print(n,end='')

def ten_by_sixteen(n):
    if n>=16:
        ten_by_sixteen(n//16)
        if n%16<=10:
            print(n%16,end='')
        else:
            print(chr(n%16+55),end='')

    else:
        if n<10:
            print(n,end='')
        else:
            print(chr(n+55),end='')

num=int(input("10진수입력 -->"))
print()
print('2진수 : ',end='')
ten_by_two(num)
print()
print('8진수 : ',end='')
ten_by_eight(num)
print()
print('16진수 : ',end='')
ten_by_sixteen(num)
print()