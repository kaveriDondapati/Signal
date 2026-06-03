import math
#  expalnation 
# n=6
# l=[2,1,5,1,3,2]
# k=2
# f=0
# m=[]

# for i in range(1,n,k):
#     f=f+i
#     m.append(f)

# s=max(m)
# print(s)

n=5
l=[4,2,7,1,9]
k=1
f=0
m=[]

for i in range(1,n,k):
    f=f+i
    m.append(f)

s=max(m)
print(s)