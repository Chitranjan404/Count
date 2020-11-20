d=[2,4,3,2,1,4,6,8,9,5,3,5]
print d
a=input("Enter the no. you want to find:")
temp=0
b=len(d)
for i in range(0,b):
 if(d[i]==a):
  temp=temp+1
print 'The count of',a,'is',temp
