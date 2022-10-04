tmpd = {"name":"re", "age":100}
list = [tmpd]
list1 = list
list2 = list.copy()
list3 = [tmpd.copy()]
print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
print()

print("list.append(1)")
list.append(1)
print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
print()

print('tmpd["name"] ="lee" ')
tmpd["name"] ="lee" 
print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)