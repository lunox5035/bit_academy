# def solution(phone_number):
#     answer=str(phone_number)
#     for i in range(0,len(answer)):
#         if answer[i]=="-":
#             continue
#         elif answer[i]==phone_number[-4]:
#             break
#         else:
#             answer[i]=="*"
#     return answer
# phone_number=input(f"전화번호:")
# print(solution(phone_number))



# from os import remove


# def solution(arr):
#     mind=min(arr)
#     arr.remove(mind)
#     return arr
    
# arr=[4,3,2,1]
# print(solution(arr))

# def solution(a, b):
#     answer = 0
#     if a<b:
#         answer=sum(list(range(a,b+1)))
#     elif b<a:
#         answer=sum(list(range(b,a+1)))
#     else:
#         answer=a
#     return answer


#0, 1, 1, 2, 3, 5,
def solution(n):
    answer = 0
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    answer=a%1234567
    return answer

print(solution(5))


def solution(n):
    answer = 0
    a=1
    b=0
    for i in range(0,n-1):
        c=a+b
        b=a
        a=c
    answer=c%1234567
    return answer