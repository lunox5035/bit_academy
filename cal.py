
from importlib.resources import Package


Package
class calculator:               #이름 정의

    def __init__(self) -> None: #init 초기값 설정
        self.result=0           #result 이름 임
    
    def add(self,b):
        self.result+=b

    def diff(self,b):
        self.result-=b