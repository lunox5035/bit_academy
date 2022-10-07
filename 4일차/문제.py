from turtle import write


fr = open("./8888.txt","r",encoding="UTF-8")
lines=fr.readlines()
fr.close()


fw=open("./8888.txt","w",encoding="UTF-8")


for line in lines:
    print(f"바꿀 내용:{line}")          #변경위치 가시화
    c_txt=input(f"입력내용(취소는c)")   #변경할 값 받기

    if c_txt=="c":                      
        fw.write(line)                 #취소시 기존 내용입력
    else:
        fw.write(c_txt)                 #변경할 값입력
    fw.write("\n")                      #공백제거

fw.close()








