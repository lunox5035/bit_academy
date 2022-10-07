# def sum(a,b):
#     return a+b

# a=input("입력하세요:")
# b=input("입력하세요:")
# print(sum(a,b))

# #형변환 
#  def sum(a,b):
#     print(type(a))
#     print(type(b))
#     try:    #실행중
#         if type(a) == int and type(b) == int:
#             return a+b
#         else:
#             return int(a)+int(b)
#     except: #오류나면 실행됨
#         return f"{a}와{b}중 숫자가 아닌게 있음"

# a=input("입력하세요:")
# b=input("입력하세요:")
# print(sum(a,b))

#파일 입출력
#상대경로 (내 위치에서 가고싶은 곳)
#. 현재위치 (c/test/test1)
#파일위치 : c/test/test12.py
#../trst12.py
#파일위치 : c/test/test2/test14.py
#../test2/test14.py
#절대위치(변하지 않는 위치)
#c:/test/test2/test14.py
#r(read)=읽기 w(write)=쓰기 a(append)=추가




# f = open("./test.txt",'w')  #파일 생성("주소/이름.형식",모드)
# f.write("hi\n")               #내용이름
# f.write("\n")
# f.write("bye")
# f.close()                   #종료


f = open("./test.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)

f = open("./input.py",'w')
f.write("print('hi')")
f.close()

f = open("./test.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)

# tomorrow update & class

fr=open("./123.txt",'r')
lines=fr.readlines()
for line in lines:
    print(line) 





