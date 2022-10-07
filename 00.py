import random

# random.random(1,45)
for e in range(0,5):
    a=[]
    for i in range(0,6):
        a.append(int(random.random()*45+1))
    print(a)


#정답
lotto=[]
for i in range(0,5):
    numbers=[]    
    while len(numbers)<6:
        num=int(random.random()*45+1)
        tmpNumbers = numbers.copy()
        tmpNumbers.append(num)
        setNumbers = set(tmpNumbers.copy())
        if len(setNumbers) == len(tmpNumbers):
            numbers.append(num)
    lotto.append(numbers)
for text in lotto
    print(text)



reg =re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
reg =re.compile("([0-9]{3}-[0-9]{3,4}-[0-9]{4})")

