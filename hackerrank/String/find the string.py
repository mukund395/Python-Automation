# in this challenge, the user enters a string and a substring. You have to print the number of times that the
# substring occurs in the given string. String traversal will take place from left to right, not from right to left.

s= "ininini"
k ="ini"
count = 0
for i in range(0,(len(s)-len(k)+1)):
    if k == str(s[i:i+len(k)]):
        count+=1
print(count)



count=0
for i in range(len(s)):
    count += s.count(k,i,len(k)+i)
print(count)

