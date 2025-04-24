#type conversion
a=4
b=3.5
sum=a+b # sum of a and b
print(sum) # int + float = float also float is extra information so considered superior

c="2"
d=3.5
# sum=c+d # sum of c and d
# print(sum) # string + float can't be added so it will give error

#type casting

e=int(c) # converting string to int
sum=e+d # sum of e and d
print(sum) # now sum can be done

# f=float("sayam")# converting string to float can''t be done

g=2
g=str(g) # converting int to string
print(type(g)) # now g is string