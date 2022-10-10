#정적 
from typing import overload


class Calc:
    @staticmethod#@ = 어너테이션
    def add(a,b):
        print(a,b)
    @staticmethod #스택틱 매소드
    @overload
    def diff(s,a,b):
        print(a+b) #3개
    @staticmethod #스택틱 매소드
    @overload
    def diff(a,b):
        print(a+b) #2개

    def printCount(cls):
        print(cls.count)
