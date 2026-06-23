# n=int(input("enter the number"))
# d = dict()
# for i in range(1,n+1):
#     d[i]=i*i

# print(d)

n = int(input("enter the number"))
op = input("enter the operation(+,_,*,/):")

d = {}

for i in range(0,n+1):
    if op == "+":
        d[i] = i+i
    elif op == "-":
        d[i] = i-i
    elif op == "*":
        d[i] + i*i
    elif op == "/":
        d[i] = i/i

print(d)
    