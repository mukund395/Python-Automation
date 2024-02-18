# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

n = 4
mid_right = []
k=[]
l=[]
p = 2*n-1+2*n-2
for i in range(1,n+1):
    l.append(chr(65+i-1))
for i in reversed(range(1, n+1)):
    print("_".join(l[-1:i - n - 1:-1] + l[i - 1::]).center(p, "-"))
for i in range(2,n+1):
    print("_".join(l[-1:i-n-1:-1]+l[i-1::]).center(p,"-"))





# methhod 1
# n=5
# l1 = list(map(chr, range(97, 123)))
# p = l1[n - 1::1] +l1[1:n]
# t = len("_".join(p))
# for i in range(1,n+1):
#     print("-".join(l1[n-1:n-i:-1]+l1[n-i:n]).center(t,"-"))
# for i in reversed(range(1,n)):
#     print("-".join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(t, "-"))

# print(p)

# for i in range():
#     pass







#
#
# -----------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
# n,m = input().split()
# l=[]
# n=int(n)
# m=int(m)

# j=3
# x="WELCOME"
# for i in range(1,int(n//2+1)):
#     l.append("-"*((m-j)//2) +".|."*((2*i)-1)+"-"*((m-j)//2)+"\n" )
#     j+=6
# print("".join(l)+x.center(m,"-")+"\n"+"".join(l[-1::-1]))

