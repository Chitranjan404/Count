d= []
a=input("Enter no. of elements in the list:")
for i in range(0,a):
 listA=raw_input("enter list elements:")
 d.append(listA)
print d
b=raw_input("Enter the no. you want to find:")
c=d.count(b)
print c

