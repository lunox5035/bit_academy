#  2부터30까지 소수리스트 뽑아내기
# from curses.ascii import isprint


listi=list(range(2,31))     #2~30리스트
for i in range(2,31):       
    for e in range(2,i):    #나누는 수, 1과 i가 아닌 수 
        if i==e:            
            continue        
        elif i%e==0:        #소수가 아닌 수 제거
            listi.remove(i)
            break
print(set(listi))           #출력

#정답
answer=[]
for i in range(2,31):
    isprimary = True        # 소수인가? / 논리연산 지정
    # i
    for j in range(2,i):
        if i%j==0:
            isprimary=False #논리연산의 거짓 지정
    if isprimary:           #논리연산의 참인 경우 ∴ 거짓 지정 후 연산 X
        answer.append(i)
print(answer)
    




