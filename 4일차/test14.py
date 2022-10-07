#계산기 만들기
# 기본적으로 
 

# def add(num1,num2):
#     return num1+num2

# def diff(num1,num2):
#     return num1-num2

# # i=0
# # i= add(i,10)
# # i= diff(i,5)
# # print (i)

# #class 함수집합?
# from importlib.resources import Package
# from unittest import result


# from cal import calculator
# from user import User
# #cal.py에서 가져옴(옮겼음)

# cal1=calculator()
# cal1.add(10)
# cal1.diff(5)
# print(f"cla1\t{cal1.result}")

# cal2=calculator()
# cal2.add(10)
# cal2.diff(5)
# print(f"cla2\t{cal2.result}")

# a=list()
# a.append("1")
# b=list()
# b.append("2")
# print(a)
# print(b)

# #def 함수 function
# result =0
# result = result + 10
# result = result - 2
# print(result)

# result = 0
# result = result + 7
# result = result - 4
# print (result)

#오타 방지 여러번 동시사용가능






# from ast import arg
# from distutils.log import Log
# from user import User


# user1 =User(id="bit",password="1234")
# user1.printUser()
# user1.chang_id("pppp")
# user1.printUser()


# from argparse import ArgumentTypeError
# from anmar import Animal
# from body.Leg import Leg
# from body.human import Humman


# l=Leg("left","park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)





from anmar import Animal
from cat import Cat
from dog import Dog


an=Animal()
print()
an.__setattr__("name","?")  #보라색:함수(괄호필요)
print(an.name)

print(an.__dict__)          #파란색: 변수


#부모꺼 가져다 쓸 수 있음

cat=Cat()
cat.printSound()
print(cat.name)


dog = Dog()
dog.printSound()
print(dog.name)
print(dog.master)
print(dog.__dict__)

#객체
#객체 지향 

