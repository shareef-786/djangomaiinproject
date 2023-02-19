#1.Create a string, display it and check its data type
from pydoc import stripid


a='abc'
print(a)
print(type(a))

#'''2.Given the string :
s = "django"
#Use indexing to print out the following:
#‘d’ , ‘o’ , ’jan’ ,’djan’,’go’.
#And Also reverse the above string.'''

print(s[0])
print(s[-1])
print(s[1:4])
print(s[:4])
print(s[-2:])

print(s[::-1])

''#3.Demonstrate following string methods on given string.
s='  Learning Python at LevelUp '    
    #- remove white spaces of string from both 
print(s.lstrip())
print(s.rstrip())
#- show the occurences of character in string
print(s.count('a'))

# #- locate a substring
print(s.find('e'))
#- find the length of string
print(len(s))
#- split the string into substrings
print(s.split())
#- Represent the string in different cases
print(s.title())
print(s.upper())
print(s.lower())

#4.Concatenate the following strings
x="With Levelup I'm on cloud"
y='9'
z=x+' '+y
print(z) 

#5.justify how strings are immutable
#s='mortal'
#s[1]='a'
#print(s)

#'''6.Find the length of string 
mystr = 'levelup Institute'
print(len(mystr))

#'''7.Using suitable string manipulation print the below output
 #            levelup levelup levelup '''
s1='levelup'
s2='levelup'
s3='levelup'
print(s1,s2,s3)
