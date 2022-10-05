# #파이썬은 절차 지향
# #자바 객체지향(OPP)
# # 함수
# #define 정의
# # sum(a,b)
# # return 변환
# # sum(a,b) => a,b 매개 변수
# #isPirmaryKey = True cammel case
# #is_primary_key=True snake case
# def sum(a,b):
#     return a+b
# print(sum(1,2)) #sum (1,2) => 1,2 인수
# print(sum(3,5))
# # argument 매개변수
# def sum1(*args):# * 여러개, 튜플
#     print(args)
#     pppp=0
#     for arg in args:
#         pppp+=arg
#     return pppp
# print(sum1(1,2,3,4,5))

# def printFunc(**kwargs): # 딕션러리 
#     print(kwargs)
# printFunc(a=1)

# def makeHuman(name, age):
#     return{"name":name,"age":age}
# human1=makeHuman("kim",30)
# human2=makeHuman("lee",34)
# print(human1)
# print(human2)

# def isPrimaryNumper(num):
#     isprimary = True # 소수인가?
#     for j in range(2,num):
#         if num%j==0:
#             isprimary=False
#             break
#     if isprimary:
#         return f"{num}은 소수입니다."
#     else:
#         return f"{num}은 소수가 아닙니다"

# print(isPrimaryNumper(6))

def isPrimaryNumpers(*nums):
    for num in nums:
        isprimary = True # 소수인가?
        for j in range(2,num):
            if num%j==0:
                isprimary=False
                break
        if isprimary:
            print (f"{num}은 소수입니다.")
        else:
            print (f"{num}은 소수가 아닙니다")

#print(isPrimaryNumpers(9,4,2,11,16)) =>retune X 반환 X
isPrimaryNumpers(9,4,2,11,16)

name="park" # 전역변수(함수 밖 변수)

def setName1(name):
    print(name)
    name=name # 지역변수
    print(name)
setName1("kim")
print(name)

#코딩테스트
# 1.백준(31%)난이도 있음
# 2.프로그래머스(30%)



