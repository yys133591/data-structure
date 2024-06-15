#Code11-01.py
""" def findMinIdx(ary):
    minIdx=0

    for i in range(1,len(ary)):

        if ary[i]<ary[minIdx]:
            minIdx=i
        
    return minIdx

testAry=[55,88,33,77]
minPos=findMinIdx(testAry)
print(f'최솟값-->{testAry[minPos]}')

 """

#self study 11-1.py
""" def findMinIdx(ary):
    maxIdx=0

    for i in range(1,len(ary)):

        if ary[i]>ary[maxIdx]:
            maxIdx=i
        
    return maxIdx

testAry=[55,88,33,77]
maxPos=findMinIdx(testAry)
print(f'최댓값-->{testAry[maxPos]}') """

#Code11-02.py
""" def findMinIdx(ary):
    minIdx=0

    for i in range(1,len(ary)):

        if ary[i]<ary[minIdx]:
            minIdx=i
        
    return minIdx

#전역번수
before=[188,162,168,120,50,150,177,105]
after=[]

#메인함수부분
print('정렬 전-->',before)
for _ in range(len(before)):
    minPos=findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print(f"정렬 후--> {after}")

 """

#Code11-03.py
""" def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if ary[minIdx]>ary[k]:
                minIdx=k
        temp=ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=temp
    return ary

dataAry=[188,162,168,120,50,150,177,105]
print(f'정렬 전-->{dataAry}')
print(f"정렬 후--> {selectionSort(dataAry)}") """

#Sample12-1.py
""" def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if ary[minIdx]>ary[k]:
                minIdx=k
        temp=ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=temp
        print(f'step{i+1} {ary}')
    return ary
#전역변수
dataAry=[5,3,8,4,9,1,6,2,7]

#메인함수
print(f"정렬 전-->{dataAry}")
print()
print(f"정렬 후--> {selectionSort(dataAry)}") """
#Code11-04.py
""" def findInsertIdx(ary,data):
    n=len(ary)
    findIdx=-1
    for i in range(0,n):
        if ary[i]>data:
            findIdx=i
            break
    if findIdx==-1:
        return n
    else:
        return findIdx

testAry=[]
insPos=findInsertIdx(testAry,55)
print(f"삽입할 위치--> {insPos}")
 
testAry=[33,77,88]
insPos=findInsertIdx(testAry,55)
print(f"삽입할 위치--> {insPos}")

testAry=[33,55,77,88]
insPos=findInsertIdx(testAry,100)
print(f"삽입할 위치--> {insPos}")

 """
#Code11-05.py
""" def findInsertIdx(ary,data):
    n=len(ary)
    findIdx=-1
    for i in range(0,n):
        if ary[i]>data:
            findIdx=i
            break
    if findIdx==-1:
        return n
    else:
        return findIdx

before=[188,162,168,120,50,150,177,105]
after=[]

print(f'정렬 전--> {before}')
for i in range(0,len(before)):
    inPos=findInsertIdx(after,before[i])
    after.insert(inPos,before[i])
print(f'정렬 후--> {after}') """

#Self Study 11-2.py
""" def findInsertIdx(ary,data):
    n=len(ary)
    findIdx=-1
    for i in range(0,n):
        if ary[i]>data:
            findIdx=i
            break
    if findIdx==-1:
        return n
    else:
        return findIdx

import random
before=[random.randint(0,200) for _ in range(10)]
after=[]

for i in range(0,len(before)):
    data=before[i]
    insPos=findInsertIdx(after,data)
    after.insert(insPos,data)

print(f"정렬 전 --> {before}")
print(f"정렬 후 -->{after}") """

#Code11-06.py
""" def InsertionSort(ary):
    n=len(ary)
    for end in range(1,n):
        for cur in range(end,0,-1):
            if ary[cur-1]>ary[cur]:
                ary[cur],ary[cur-1]=ary[cur-1],ary[cur]
    return ary

dataAry=[188,162,168,120,50,150,177,105]

print(f'정렬 전 --> {dataAry}')
print(f'정렬 후 --> {InsertionSort(dataAry)}')
 """

#Code 11-07.py
""" def selectionSort(ary):
    n=len(ary)
    
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if ary[k]>ary[minIdx]:
                minIdx=k
        ary[i],ary[minIdx]=ary[minIdx],ary[i]

    return ary

moneyAry=[7,5,11,6,9,80000,10,6,15,12]

print(f"용돈 정렬 전 --> {moneyAry}")
print(f"용돈 정렬 후 --> {selectionSort(moneyAry)}")
print(f"용돈 중앙값 --> {moneyAry[len(moneyAry)//2]}")
 """

#Code11-08.py
""" import os
def makeFileList(folderName):
    fnameAry=[]
    for dirName, suDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertionSort(ary):
    n=len(ary)
    for end in range(1,n):
        for cur in range(end,0,-1):
            if ary[cur-1]<ary[cur]:
                ary[cur-1],ary[cur]=ary[cur],ary[cur-1]
    return ary

fileAry=[]

fileAry=makeFileList('/Users/smy/Desktop/24년도 1학기/자료구조기초')
fileAry=insertionSort(fileAry)
print(f"파일명 역순 정렬 --> {fileAry}") """

#응용예제1.py
""" def insertionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if ary[k][1]<ary[minIdx][1]:
                minIdx=k
        ary[i],ary[minIdx]=ary[minIdx],ary[i]
    return ary


#전역변수
scoreAry=[['선미',88],['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]

print(f"정렬 전 -->{scoreAry}")
print(f"정렬 전 -->{insertionSort(scoreAry)}")
print("## 성적별 조 편성표 ##")
for i in range(len(scoreAry)//2):
    print(f"{scoreAry[i][0]} : {scoreAry[-1-i][0]}")
 """

#응용예제2.py
""" import random
def makeOneDimension(ary):
    result=[]
    for col in range(len(ary)):
        for row in range(len(ary[col])):
            result.append(ary[col][row])
    return result

def insertionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if ary[k]<ary[minIdx]:
                minIdx=k
        ary[i],ary[minIdx]=ary[minIdx],ary[i]
    return ary

#전역변수 
randomAry=[[random.randint(1,200) for j in range(4)] for i in range(4)]
randomAry=makeOneDimension(randomAry)

print(f"1차원 변경 후, 정렬 전 --> {randomAry}")
print(f"1차원 변경 후, 정렬 후 --> {insertionSort(randomAry)}")
print(f"중앙값 --> {randomAry[len(randomAry)//2]}") """