#Code12-01.py
""" def BubbleSort(ary):
    n=len(ary)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if ary[j]>ary[j+1]:
                ary[j],ary[j+1]=ary[j+1],ary[j]
    return ary

dataAry=[188,162,168,120,50,150,177,105]

print(f"정렬 전 --> {dataAry}")
print(f"정렬 후 --> {BubbleSort(dataAry)}") """

#Code12-02.py
""" import random
def BubbleSort(ary):
    n=len(ary)
    count=0
    for end in range(n-1,0,-1):
        changeYN=False
        for cur in range(0,end):
            if ary[cur]>ary[cur+1]:
                ary[cur],ary[cur+1]=ary[cur+1],ary[cur]
                changeYN=True
                count+=1
        if not changeYN:
            break
    return ary,count

dataAry=[random.randint(0,200) for i in range(10)]
print(f"정렬 전 --> {dataAry}")
dataAry,count=BubbleSort(dataAry)
print(f"정렬 후 --> {dataAry}")
print(f'##{count}회로 정렬 완료') """

#Code12-03.py
""" 
def qiuckSort(ary):
    n=len(ary)
    if n<=1:
        return ary
    pivot=ary[n//2]
    leftary,rightary=[],[]

    for num in ary:
        if num<pivot:
            leftary.append(num)
        elif num>pivot:
            rightary.append(num)
    
    return qiuckSort(leftary) + [pivot] +qiuckSort(rightary)

dataAry=[188,150,168,162,105,120,177,50]

print(f"정렬 전 --> {dataAry}")
print(f"정렬 후 --> {qiuckSort(dataAry)}") """

#Code12-04.py

""" def quickSort(ary,count=0):
    n=len(ary)
    if n<=1:
        return ary,count
    pivot=ary[n//2]
    leftary,rightary=[],[]

    for num in ary:
        if num<pivot:
            leftary.append(num)
        elif num>pivot:
            rightary.append(num)
        count+=1
    sorted_left, count = quickSort(leftary, count)
    sorted_right, count = quickSort(rightary, count)
    return sorted_left + [pivot] + sorted_right,count

dataAry=[31,49,175,33,103,76,63,151,166,25]

print(f"정렬 전 --> {dataAry}")
dataAry,count=quickSort(dataAry)
print(f"정렬 후 --> {dataAry}")
print(f"{count}회로 정렬 완료") """

#Code12-04.py
""" def quickSort(ary):
    n=len(ary)
    if n<=1:
        return ary
    pivot=ary[n//2]
    leftAry,midAry,rightAry=[],[],[]

    for num in ary:
        if num<pivot:
            leftAry.append(num)
        elif num==pivot:
            midAry.append(num)
        elif num>pivot:
            rightAry.append(num)
    return quickSort(leftAry) + midAry  + quickSort(rightAry)

dataAry=[120,120,188,150,168,50,50,162,105,120,177,50]
print(f"정렬 전 --> {dataAry}")
dataAry=quickSort(dataAry)
print(f"정렬 후 --> {dataAry}") """

#Code 12-05.py
""" def qSort(arr,start,end):
    if end<=start:
        return
    low=start
    high=end
    pivot=arr[(low+high)//2]
    while low<=high:
        while arr[low]<pivot:
            low+=1
        while arr[high]>pivot:
            high-=1
        if low<=high:
            arr[low],arr[high]=arr[high],arr[low]
            low,high=low+1,high-1

    mid=low
    qSort(arr,start,mid-1)
    qSort(arr,mid,end)

def qucikSort(ary):
    qSort(ary,0,len(ary)-1)
    return ary
dataAry=[188,150,168,162,105,120,177,50]

print(f'정렬 전 --> {dataAry}')
print(f'정렬 후 --> {qucikSort(dataAry)}')

 """

#응용예제1.py
""" import time
import math
import random

def BubbleSort(ary):
    n=len(ary)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if ary[j]>ary[j+1]:
                ary[j],ary[j+1]=ary[j+1],ary[j]
    return ary

def qiuckSort(ary):
    n=len(ary)
    if n<=1:
        return ary
    pivot=ary[n//2]
    leftary,rightary=[],[]

    for num in ary:
        if num<pivot:
            leftary.append(num)
        elif num>pivot:
            rightary.append(num)
    
    return qiuckSort(leftary) + [pivot] +qiuckSort(rightary)

def selectionSortTime(ary):
    start=time.time()
    BubbleSort(ary)
    end=time.time()
    return end-start

def quickSortTime(ary):
    start=time.time()
    qiuckSort(ary)
    end=time.time()
    return end-start



dataNum=int(input('데이터수 : '))
dataAry=[random.randint(0,200)for _ in range(dataNum)]


print(f"선택 정렬 --> {selectionSortTime(dataAry):.5f}")
print(f"퀵 정렬 --> {quickSortTime(dataAry):.5f}")
 """

#Code13-01.py,SelfStudy.py
""" def seqSearch(ary,fData):
    size=len(ary)
    findAry=[]
    for i  in range(size):
        if ary[i]==fData:
            findAry.append(i)
    return findAry

# 전역변수부분
dataAry=[188,50,150,168,50,162,105,120,177,50]
findData=0

#메인함수부분
findData=int(input('* 찾을 값을 입력하세요: '))
print(f'배열 --> {dataAry}')
insPos=seqSearch(dataAry,findData)
if len(insPos)==0:
    print(f'{findData}이(가) 없네요.')

else:
    print(f'{findData}은(는) {insPos} 위치에 있음') """

""" def binSearch(ary,fData):
    start=0
    end=len(ary)-1
    pos=-1
    while start<=end:
        mid=(start+end)//2
        if ary[mid]==fData:
            pos=mid
            return pos
        elif ary[mid]<fData:
            start=mid+1
        else:
            end=mid-1

    return pos

dataAry=[50,60,105,120,150,160,162,168,177,188]
findData=162

print(f'배열 --> {dataAry}')
insPos=binSearch(dataAry,findData)
if insPos==-1:
    print('검색 실패')
else:
    print(findData,'은(는)',insPos, '위치에 있음')
 """
#self study 13-2.py
from math import pi
from operator import le
import random

""" def qSort(arr,start,end):
    if end<=start:
        return
    low=start
    high=end
    pivot=arr[(low+high)//2]
    while low<=high:
        while arr[low]<pivot:
            low+=1
        while arr[high]>pivot:
            high-=1
        if low<=high:
            arr[low],arr[high]=arr[high],arr[low]
            low,high=low+1,high-1

    mid=low
    qSort(arr,start,mid-1)
    qSort(arr,mid,end)

def quickSort(ary):
    qSort(ary,0,len(ary)-1)
    return ary

def binSearch(ary,fData):
    start=0
    end=len(ary)-1
    pos=-1
    count=0
    while start<=end:
        mid=(start+end)//2
        if ary[mid]==fData:
            return mid,count
        elif ary[mid]<fData:
            start=mid+1
        else:
            end=mid-1
        count+=1
    return pos,count

dataAry=[random.randint(0,100000) for _ in range(100000)]
findData=dataAry[random.randint(0,99999)]
dataAry=quickSort(dataAry)
print(f'배열 일부 -->{dataAry[0:5]} ~~~~{dataAry[99995:100000]}')
insPos,count=binSearch(dataAry,findData)
if insPos==-1:
    print(f'{findData}이(가) 없네요.')
else:
    print(f'{findData}은(는) {insPos} 위치에 있음.')
print(f'## {count}회 검색함.') """

#Code13-04.py

""" from operator import itemgetter
def makeIndex(ary,pos):
    beforeAry=[]
    index=0
    for data in ary:
        beforeAry.append((data[pos],index))
        index+=1
    
    sortedAry=sorted(beforeAry,key=itemgetter(0))
    return sortedAry

def bookSearch(ary,fData):
    pos=-1
    start=0
    end=len(ary)-1
    while start<=end:
        mid=(start+end)//2
        if ary[mid][0]==fData:
            return mid[1]
        elif ary[mid]<fData:
            start=mid+1
        elif ary[mid]>fData:
            end=mid-1
    return pos

 """

#응용예제1번
def quickSort(ary):
    n=len(ary)
    if n<=1:
        return ary
    pivot=ary[n//2]
    leftAry,rightAry,midAry=[],[],[]
    for num in ary:
        if num==pivot:
            midAry.append(num)
        elif num<pivot:
            leftAry.append(num)
        elif num>pivot:
            leftAry.append(num)
    return quickSort(leftAry) + midAry + quickSort(rightAry)   
#전역변수
dataAry=['코카콜라','츄파츕스','도시락','삼각김밥','레쓰비캔커피','츄파츕스','도시락','츄파츕스','레쓰비캔커피','코카콜라','코카콜라','도시락','코카콜라','삼각김밥','삼각김밥','바나나맛우유','삼각김밥','츄파츕스','바나나맛우유','코카콜라']

#메인함수
print(f'#오늘 판매된 전체물건(중복O,정렬X)--> {dataAry}')
dataAry=quickSort(dataAry)
print(f'#오늘 판매된 전체물건(중복O,정렬O)--> {dataAry}')

print(f'#오늘 판매된 물품(중복X) -->{list(set(dataAry))}')