#파이썬 = 절차지향언어

#trye
#a=1
#a=""           int 
#a=[]           str
#a={}           set
#a=()           tuple
#a={key:value}  dict

#동적타이핑(동적데이터타입)
#장점:타입을 지정하지않아도 연산가능
#단점:오류발생가능

#스크립트 언어
#소스코드를 한 줄씩 읽어서 곧바로 실행
#컴파일 없음

#플랫폼 독립적: os 상관없다.

#제어문
#if elif else 
# match case

#반복문
#for in :
#while :
#break continue
#람다(lambda) map, reduce, filler

#함수
#def:
#def sum(a,b):  a,b 매개변수
#   return a+b
#sum(1,2)       1,2 인자값

#def A(*a):     *a 튜플
#def A(**a):    **a 딕셔너리

# name = "kim"  전역변수
#def printName(name):
#   name="lee" 지역변수

#파일입출력
#f=open(파일,mode,encordinf "UTF-8")

#상대경로:현재 작업공간을 기준
#절대경로:컴퓨터의 저장위치를 기준
#c:\test->c:\test\test2
#.\test2
#c:\test\test2


#입력받고 싶을떄 input

#class 
#쓰는 이유 : 중복작업 처리
#객체지향
#class name(상속받을 클래스 이름):
#   def __init__:
#상속 접근 할때 (super())
#def __init__(self):    self self 자신

#improt 다른 곳에서 불러올떄

#정규식 개념 search match
#ex) park@gmaill.com 다음 이메일의 형식의 올고그름을 판단
#import re


#import random


#print(f"{}") #f=format


from tkinter import Y
from xml.dom.expatbuilder import FilterVisibilityController


list1=[9,1,2,3]
def sum(x,t):
    print(f"{x}{y}")
    return x+Y
a=reduce(lambda x,y:sum(x,y,list1))

user ={"id":"id","pass":"pass","name":""}

names= ["kim","lee",'park']
namelist=list(map(lambdax:{"name":x},name))
print(namelist)

findUser = list(fillter(lambda x : x.get("name")=="park",namelist))
print(findUser)


