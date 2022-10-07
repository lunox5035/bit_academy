# def open(filename,tyoe):
    # filename 이 있냐?
    # if type == "w":
        # 글쓰기 모드
    # elif type == "r":
        # 읽기 모드

# f=open("./123.txt",'w')
# f.write("Ai\n빅데이터\n\n파이썬")
# f.close()



# fr=open("./123.txt",'r')
# lines = fr.readlines()
# # lines = ["Ai","빅데이터","","파이썬"]
# for line in lines:
#     print(line) 
# fr.close()

# fw = open("./123.txt",'w')
# for line in lines:
#     if line == "Ai":
#         fw.write("ML")
#     else:
#         fw.write(line)
# fw.close()


# # fw = open("./123.txt",'w')
# # for line in lines:
# #     if line == "Ai":
# #         fw.write(line)
# #     else:
# #         fw.write("\nML")
# # fw.close()

fr = open("./8888.txt",'r',encoding="UTF-8")
lines=fr.readlines()
for line in lines:
    print(line)
fr.close()



fw = open("./8888.txt",'w',encoding="UTF-8")
print(lines)

for line in lines:
    line = line.strip()#공백 제거
    
    if line == "한글":#<="한글\n"상태 \n제거필요
        fw.write("ML")

    elif line == "읽기":
        fw.write("py")

    else:
        fw.write(line)
    fw.write("\n")
fw.close()


#정답
fr = open("./8888.txt",'r',encoding="UTF-8")
lines = fr.readlines()
fr.close()

fw = open("./8888.txt",'w',encoding="UTF-8")
for line in lines:
    update_text = input(f"전 문장: {line}\n 바꿀문장(취소는 c):\t") 
                                # {line}이 추출해 온 값과 같음
    if update_text=="c":
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close()