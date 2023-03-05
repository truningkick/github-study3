'''
a, b = input().split(',')
a = int(a)
b = int(b)
print('{} is {} years old'.format(a, b))	#1 is 2 years old
print(type(a))	#<class 'int'>
print("안녕 %d야"%(a))


#미분방정식 만들기

inval = input("초기값을 입력하세요:\t")
print(inval)

print(type(inval))
'''
'''
import array as arr
int_arr = arr.array('i', [1,2,3])

int_arr.insert(1,4)
int_arr.remove(1)
int_arr
print("elements in array :", end="")
for i in range(0, len(int_arr)):
    print(int_arr[i], end = "")
print()

ilist = [1,2,3,4,5,6,7,8,9,3]
iarray = arr.array('i',ilist)
iarray[3] = 5
print(iarray.index(3))
print(iarray)
'''
#두 수의 합 찾기: 배열에서 2개 숫자를 선택해 더한 값이 목푯값이 되도록 만들 때
#입력값 : 2,7, 10, 19
#목표값 : 9

import array as arr
'''

inputlist = [1,2,3,4,5,6,7,8,9,10]
# arr.array('i',[2,7,10,19,5,4,-10])
inputarr = arr.array('i',inputlist)
resurtarr = arr.array('i',[])
target = 9

for i in range(0, len(inputarr)-1):
    for j in range(i+1, len(inputarr)):
        if inputarr[i] + inputarr[j] == 9:
            rearr = arr.array('i',[])
            rearr.append(i)
            rearr.append(j)
            print(rearr)

for i in range(0,len(inputarr)-1):
    for j in range(i+1,len(inputarr)):
        if target == inputarr[i]+inputarr[j]:
            resurtarr.append(i)
            resurtarr.append(j)


a,b = inputarr.index(2), inputarr.index(7)
resurtarr.append(a)
resurtarr.append(b)
listt = [a,b]
print(listt)
'''
#두수의 합 찾기
'''
List = [2,7,8,11]
a = List

def twosum(num:a, target:int) -> list:
    hashtable = {}

    for i in range(0,len(num)):
        print(i)
        value = target - num[i]
        if hashtable.get(value) is not None and hashtable[value] != i:
            return sorted([i, hashtable[value]])
        
        hashtable[num[i]] = i
    print(hashtable)
    return[-1,-1]

cc=twosum(a,9)
print(cc)
print("end")
'''

# 입력값 1<= a1, a2 <= 1000000
# target  = X
# 수열의 크기 = N

#예제 : N=9, input=5,12,7,10,9,1,2,3,11, target = 13
# output :만족하는 건 몇쌍? 
'''
inputlist = [5,12,7,10,9,1,2,3,11]
target = 13
resultC = 0
def sumtwo(nums:inputlist, target:target, resultC:int) -> int:
    hashlist = {}
    for i in range(0,len(inputlist)):
        value = target-nums[i]
        if hashlist.get(value) is not None and hashlist[value] != i :
            print("조건만족!, 기록실시")
            resultC += 1

        hashlist[nums[i]] = i
    return(resultC)
        
print("결과:%d"%(sumtwo(inputlist, target,resultC)))
'''

#시험감독
#시험장 : N, i번 시험장 : Ai명
#감독관 : 총감독관 / 부감독관
# 총감독관은 한시험장에서 감시 가능 응시자 : B / 한명만이 존재
# 부감독관은 '' : C / 여러명이 있을 수 있음
# 각 시험장마다 ㅁ응시생 모두 감시 필요, 필요한 감독관의 수는? 
# input: 시험장 수 N
# 각 시험자 응시자 수 A
# B, C
'''
n = int(input("시험장 수 N :\t"))
a_i = []
summ=0
for n in range(1,n+1):
    print("%d번째 시험장 인원:"%(n),end="")
    a_i.append(int(input("각 시험장 응시자 수 A_i :\t")))
for n in a_i:   # 총 시험생 수 
    summ += n
b = int(input("총감독관 감시 가능 인원 B :\t"))
c = int(input("부감독관 감시 가능 인원 C :\t"))
blist = []
clist = [] #부감독관 수
for m in range(0,n+1): #총감독관 수
    if (summ - m*b)%c == 0:
        for p in range(0,50): #부감독관 수
            if p == ((summ-m*b)/c) :
                print(p)
                blist.append(m)
                clist.append(p)
    else:
        continue
rere=[]
for n in range (0,len(blist)):
    rere.append(blist[n]+clist[n])
        
print("필요한 감독관 수는 %d명 이다."%(min(rere)))
#한 시험장 당 감시 가능인원을 모두 채우지는 않지만, 일부만 채우더라도 감독관은 필요한 것을 고려하지 않았음! 수정.
'''
#1.5 배열에서 삽입 위치 찾기 
#target값이 배열보다 작을 댸 오류 발생 
'''
nums = []
print(" * if you end input? put on '999' ! ")
inin = 0
while(1):
    inin = int(input("input value?: "))
    if inin == 999:
        break
    nums.append(inin)

inputarr = arr.array('i',nums)    
tar = int(input("target값을 입력해 :"))
inputarr = sorted(inputarr)
indexlist=[]

def rowval(data):   # 배열에서 가장 작은 수 찾기
    result = data[0]
    for value1 in data:
        
        if value1 < result:
            result = value1
    return result


def ox(val1,val2):  # inputarr == target? 여부 
    for val3 in val2:
        if val3 == val1:
            return 1
    return 0
    

if bool(ox(tar,inputarr)) == 1 :
    bb = inputarr.index(tar)
    print("target number will be located %d index in input array" %(bb))

elif bool(ox(tar,inputarr)) == 0 :
    for i in range(0, len(inputarr)):
        if tar - inputarr[i] >= 0:
            indexlist.append( tar - inputarr[i] )   # target과의 차가 가장 작은수를 찾기 위해

    indexA = rowval(indexlist) # index of low vlaue in input value
    result = indexlist.index(indexA) # 차가 가장 작은 위치 
    print("target number is located in %d index in input array" %(result+1))

'''
#노트 레이아웃을 이용한 문제접근 및 풀이  
#이진탐색 적극 활용 요망 !
#GooD
nums = []
print(" * if you end input? put on '999' ! ")
inin = 0
while(1):
    inin = int(input("input value?: "))
    if inin == 999:
        break
    nums.append(inin)

inputarr = arr.array('i',nums)    
tar = int(input("target값을 입력해 :"))
inputarr = sorted(inputarr)


def serchN(data, tar):
    high = len(data)-1
    low = 0
    beforeL = 0
    mid = int( (low + high) / 2 )
    while(1):
        if data[mid] > tar: high = mid  # low
        elif data[mid] < tar: low = mid # high
        elif data[mid] == tar: return mid
        mid = int((low+high)/2)
        if mid < 1 : return 0

print( "target is located in %d index on input array" %(serchN(inputarr,tar)) )










