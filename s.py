def solution(phone_number):
    answer=str(phone_number)
    for i in range(0,len(answer)):
        if answer[i]=="-":
            continue
        elif answer[i]==phone_number[-4]:
            break
        else:
            answer[i]=="*"
    return answer
phone_number=input(f"전화번호:")
print(solution(phone_number))