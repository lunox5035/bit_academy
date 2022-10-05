# from itertools import count


# def solution(phone_number):
#     answer=""
#     nums=str(phone_number)
#     answer ="*"*(len(nums)-4)+nums[-4:]
#     return answer

# phone_number=input(f"핸드폰 번호")
# print(solution)

#정답

def solution(phone_number):
    answer=""
    for i in range(0,len(answer)):
        if i <len(phone_number)-4:
            answer +="*"
        else:
            answer +=phone_number[i]
    return answer


#뒷자리4개와 -만 살리기


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


#정답

def solution(phone_number):
    answer=""
    for i in range(0,len(answer)):
        if i <len(phone_number)-4:
            if phone_number[i]=="-":
                answer+="-"
            else:
                answer +="*"
        else:
            answer +=phone_number[i]
    return answer








