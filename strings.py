str1='hello world'
str2="hi there"
str3='''hello world'''
str4="""hi there"""
#all are valid strings

#escape characters
str5='hello\'s world' #single quote inside single quote
print(str5) #hello's world

str6="hello\n world" #new line
print(str6) #hello

str7="hello\t world" #tab space
print(str7) #hello    world

# #string concatenation
str8="hello" + " world" #concatenation
print(str8) #hello world


str9="hello"
str10=" world"
finalstr= str9 + str10 #concatenation
print(finalstr) #hello world

print(len(finalstr)) #length of string

len1=len(str9) #length of string
print(len1) #5

finalstr1= str9 + " beautiful" + str10 #concatenation
print(finalstr1) #hello world
print(len(finalstr1)) #length of string

finalstr1= str9 + " " + str10 #concatenation
print(finalstr1) #hello world
print(len(finalstr1)) #length of string


#indexing

str="hello world"
print(str[0]) #h
print(str[5]) #space

print(str[-1]) #d

# str[2] = "d"# TypeError: 'str' object does not support item assignment
# print(str)

#slicing
print(str[0:5]) #hello
print(str[6:]) #world
print(str[:4]) #hell
print(str[0:6]) #hello 

print(str[2:len(str)]) #llo world

print(str[-5:-1]) #world
print(str[-1:-4]) #empty string, slicing does not work in reverse order
print(str[-5:])