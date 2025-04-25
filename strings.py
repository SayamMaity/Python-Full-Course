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