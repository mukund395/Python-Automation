# x=1
# y=1
# z=2
# n=3
# k = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k!=n]
# print(k)


l1 = []
l2=[]
for i in range(int(input("enter the number "))):
    name =  input()
    score = (float(input()))
    l1.append([name, score])
    l2.append(score)
s =sorted(set(l2))[1]

for i, j in sorted(l1):
    if j == s:
        print(i)

