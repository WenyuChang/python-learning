myList = [1,2,'a','b',True,False,1.2,4+5j]

print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

myList.append('new item')
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

myList = [3,4,6,1,2,0,-1]
myList.sort()
print('These items are:',myList)

#=============================================================

myList = [3,4,6,1,2,0,-1]
def cmp(x, y):
    if x>y:
        return -1
    elif x==y:
        return 0
    else:
        return 1
myList.sort(cmp)
print('These items are:',myList)

#=============================================================

print(myList.pop())
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

print(myList.index(3))
myList.insert(1,8)
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

myList.remove(8)
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

del myList[0]
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

print('myList[-1]:',myList[-1])
print('myList[1:3]:',myList[1:4])

#=============================================================

listone = [0, 1, 2, 3, 4, 5, 6]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

#=============================================================

myList.extend([100,200,300])
print('The len of my list:', len(myList))
print('These items are:',myList)

#=============================================================

from collections import deque
myQueue = deque(myList)
myQueue.extend([1000,2000,3000])
print('pop:', myQueue.popleft())
print('The len of my list:', len(myQueue))
print('These items are:',myQueue)

#=============================================================

for i, v in enumerate(myList):
    print(i, v)

#=============================================================

listInt = [0, 1, 2, 3, 4, 5, 6]
print("str(): %s" %(str(listInt),))
print("list(): ", list(listInt))
print("tuple(): ", tuple(listInt))

#=============================================================

listInt = [3,4,6,1,2,0,-1]
print("len(): ", len(listInt))
print("max(): ", max(listInt))
print("sum(): ", sum(listInt))
print("sorted(): ",  sorted(listInt))
print("reversed(): ", reversed(listInt))
print("zip(): ", zip(listInt))

#=============================================================

def func(fstr, *args):
    print("func - fstr: ", fstr)
    print("func - *args:", args)
    
func("test",3,4,6,1,2,0,-1)

#=============================================================

listOne = [3,4,6,1,2,0,-1]
listTwo = listOne
listThree = list(listOne)
listTwo.append(10)
listThree.append(11)
print("listOne: " , listOne)
print("listTwo: ", listTwo)
print("listThree: ", listThree)

#=============================================================

myList = [3,4,6,1,2,0,-1]
print('myList[1:3]:',myList[1:3])
print('myList[1:7:2]:',myList[1:7:2])
print('myList[7:1:-1]:',myList[7:1:-1])
myList[1:7:2] = [99,98,97]
print('myList: ',myList)