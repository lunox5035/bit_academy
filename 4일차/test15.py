# # 모듈

import calendar
import http
import math
import random
import re
import webbrowser


# print("3.141592")
# print(math.pi)
# calendar.prmonth(2022,10)
# # webbrowser.open("https://naver.com")
# print(random.random()*11+1)
# # 1 <=answer*11<12

# #정규식
# reg = re.compile("[A-z0-9]{4,5}")
# #[들어갈 문자]{글자수,4~5글자}
# id="222"
# print(reg.match(id))
# print(reg.search(id))


# 회원가입
# 비밀번호 특수문자 포함&영어 대문자 포함
# ai 자연어 처리
#나는 오늘 좋다.(날것 그대로의 감정 등)
# 이메일  id@naver.com
# reg =re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
# print(reg.match("park@gmail.com"))

#퀴즈
# 로또 1-45 중복없이 6자리
#random


reg =re.compile("([0-9]{3}+-[0-9]{4}+-[0-9]{4})")
