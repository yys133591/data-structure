#code 11_1
def findMinIdx(ary) :
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx]>ary[i]) :
            minIdx = i
    return minIdx

testAry = [55,88,33,77]
minPos=findMinIdx(testAry)
print("최솟값 -- >", testAry[minPos])

#Code11-02 
def findMinIdx(ary) :
    minIdx =0
    for i in range(1, len(ary)):
        if (ary[minIdx]> ary[i]) :
            minIdx = i
    return minIdx  

before = [153, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전 -->', before)
for _ in range(len(before)) :
    minPos=findMinIdx(before)
    after.append(before[minPos])
    del (before[minPos])

print('정렬 후 -->', after)

#code 11_3
def selectionSort(ary) :
    n=len(ary)
    for i in range(0,n-1) :
        minIdx = i
        for k in range (i+1, n) :
            if (ary[minIdx]>ary[k]) :
                minIdx = k
        tmp=ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=tmp

    return ary

dataAry = [188,162,168,120,50,150,177,105]

print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)

#Code11-3.py
def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i    
        for k in range(0,n-1):
            if(ary[minIdx]>ary[k]):
                minIdx=k
            tmp=ary[i]
            ary[i]=ary[minIdx]
            ary[minIdx]=tmp
    
    return ary

dataAry = [188,162,168,120,50,150,177,105]

print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)

#Code11-04.py
def findInsertIdx(ary,data):
    findIdx=-1
    for i in range(0,len(ary)):
        if(ary[i]>data):
            findIdx=i
            break
        if findIdx==-1:
            return len(ary)
        else:
            return findIdx

testAry=[]
insPos=findInsertIdx(testAry,55)
print('삽입할 위치-->',insPos)

testAry=[33,55,77,88]
insPos=findInsertIdx(testAry,100)
print('삽입할 위치-->',insPos)



#Code11-05.py
def findInsertIdx(ary,data):
    findIdx=-1
    for i in range(0,len(ary)):
        if(ary[i]>data):
            findIdx=i
            break
        if findIdx==-1:
            return len(ary)
        else:
            return findIdx

before=[188,162,168,120,50,150,177,105]
after=[]

print('정렬 전-->',before)
for i in range(len(before)):
    data=before[i]
    insPos=findInsertIdx(after,data)
    after.insert(insPos,data)
print('정렬 후-->',after)

#Code11-06.py
def insertionSort(ary):
    n=len(ary)
    for end in range(1,n):
        for cur in range(end,0,-1):
            if(ary[cur-1]>ary[cur]):
                ary[cur-1],ary[cur]=ary[cur],ary[cur-1]
    return ary

dataAry=[188,162,168,120,50,150,177,105]

print('정렬 전-->',dataAry)
dataAry=insertionSort(dataAry)
print('정렬 후-->',dataAry)

#Code11-07.py
def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1):
        minIdx=i
        for k in range(i+1,n):
            if(ary[minIdx>ary[k]]):
                minIdx=k
        tmp=ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=tmp
    return ary

moneyary=[7,5,11,6,9,80000,10,6,15,12]

print("용돈 정렬 전-->",moneyary)
moneyary=selectionSort(moneyary)
print('용돈 정렬 후-->',moneyary)
print('용돈 중앙값-->',moneyary[len(moneyary//2)])


#Code11-08.py
import os

def makeFileList(folderName):
    fnameAry=[]
    for dirName,subDirList,fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertSort(ary):
    n=len(ary)
    for end in range(1,n):
        for cur in range(end,0,-1):
            if(ary[cur-1]<ary[cur]):
                ary[cur-1],ary[cur]=ary[cur],ary[cur-1]
    return ary

fileAry=[]

fileAry=makeFileList('C:/Program Files/Common Files')
fileAry=insertionSort(fileAry)
print("파일명 역순 정렬-->",fileAry)