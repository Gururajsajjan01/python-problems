# l=[]
# for i in range(2000, 5801):
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(",".join(l))


l = []
a = int(input("enter the number"))
for i in range(1, a):
    if (i%2==0) and (i%3!=0):
        l.append(str(i))

print(",".join(l))