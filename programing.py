# 1. Write a program to fetch all even numbers from list? 

lst = [10,11,13,14,9,8] #[10,14,8]
newlst = []
for i in lst:
    if i%2 == 0:
        newlst.append(i)
print(newlst)
   
# 2. Write a program to fetch all string values from list?
'''
lst = [10,'a',True,'b',False] #['a', 'b']
newlst = []

for i in lst:
    if type(i) == str:
        newlst.append(i)
print(newlst)
'''
# 3. Write a program to fetch all 5 divisibles from list?
'''
lst = [12,15,27,20,5] #[15,20,5]
newls = []

for i in lst:
    if i%5 == 0:
        newls.append(i)
print(newls)
'''

# 4. Write a program to count total number of int values in the list?
'''
lst = [10,'a',20,True,30,'b',40] #4
newlst = []

for i in lst:
    if type(i) == int :
            newlst.append(i)
print(len(newlst))
'''
        
# 5. Write a program to count total number of characters in the string(including space)?.
'''

st = 'Python language' #15
print(len(st))

'''

# 6. Write a program to count total number of words in the string. 
'''
st = 'python narayana tech house hyd' #5
new = st.split()
print(len(new))

'''
# 7. Write a program to fetch all vowels from the string? 
'''
st = 'Python language' #['o','a','u','a','e']
newlst = []

for i in st:
    if i in 'aeiou':
        newlst.append(i)
print(newlst)
'''

# 8. Write a program to count total number of vowels?
'''
st = 'python narayana' #5
newlst = []

for i in st:
    if i in 'aeiou':
        newlst.append(i)
print(len(newlst))
'''

# 9. Write a program to count total number of characters in the string(excluding space)? 
'''
st = 'python is a simple language' #23 is wrong ,
# print(len(st))
newlst = []
for i in st:
    if i != ' ':
        newlst.append(i)
print(len(newlst))
'''

# 10. Write a program to count total number of consonants in the string? 
'''
st = 'python language' #9
newlst = []

for i in st:
    if i!= ' ' and i not in 'aeiou'  :
        newlst.append(i)
print(len(newlst))
'''
# 11. Write a program to fetch all words which starts with vowel from given string?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
st1 = st.split()
newlst = []

for i in st1:
    if i[0] in 'aeiou':
        newlst.append(i)
print((newlst))
'''

# 12. Write a program to fetch all words which ends with consonent in the given string?
'''
st = 'Python is simple and easy language' #['Python', 'is','and', 'easy']
s = st.split()
newlst = []

for i in s:
    if i[-1] not in  'aeiou':
        newlst.append(i)
print(newlst)
'''

# 13. Write a program to fetch all words which 'a' two or more then two times?
'''
st = 'Python is simple and easy language' #['language']
s = st.split()
newlst = []

for i in s:
    if i.count('a') >= 2:
        newlst.append(i)
print(newlst)         
'''

# 14. Write a program to count number of characters of each word in the string? 
'''
st = 'Python is simple and easy language' #[6,2,6,3,4,8]
st1 = st.split(' ')
newlst = []
for i in st1:
    newlst.append(len(i))
print(newlst)
'''

# 15. Write a program to fetch the first and last character from each word in the string?

'''
st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
s = st.split()
newlst = []

for i in s:
    if i[0] and i[-1]:
        newlst.append(i[0]+i[-1])
print(newlst)
'''

# 16. Write a program to fetch all words which contains 'a' character in the string?
'''
st = 'Python is simple and easy language' #['and', 'easy', 'language']
s = st.split()
newlst = []

for i in s:
    if i.count('a') >= 1:
        newlst.append(i)
print(newlst)

'''

# 17. Write a program to fetch all words which does not contain 'e' character in string?
'''
st = 'Python is simple and easy language' #['Python', 'is', 'and']
s = st.split()
newlst = []

for i in s:
    if i.count('a') <= 0:
        newlst.append(i)
print(newlst)
'''
# 18. Write a program to fetch all words which contains only 4 or lessthen 4 characters? 
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
s = st.split()
newlst = []

for i in s:
    if len(i) <= 4:
        newlst.append(i)
print(newlst)
'''

# 19. Write a program to fetch all words which contain odd number of characters in the string?
'''
st = 'Python is simple and easy language' #['and']
s = st.split()
newlst = []

for i in s:
    if len(i)%2==1:
        newlst.append(i)
print(newlst)
'''

# 20. Write a program to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is number one language' #['one']
s = st.split()
newlst = []

for i in s:
    if i[0] in 'aeiou' and i[-1] in 'aeiou':
        newlst.append(i)
print(newlst) 
'''

# 21. Write a program to fetch all palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] # #['madam', 'dad', 'eye', 'malayalam']

newlst = []

for i in names:
    if i == i[-1::-1]:
        newlst.append(i)
print(newlst)
'''

# def is_palindrome(i):
#     i = i.lower().replace(" ", "")
#     reversed_word = i[::-1]
#     if i == reversed_word:
#         return True
#     else:
#         return False

# newlst = []

# for i in names:
#     if is_palindrome(i):
#         newlst.append(i)

# print(newlst)


# 22. Write a program to fetch all non-palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['python', 'language']
newlst = []

for i in names:
    if i != i[-1::-1]:
        newlst.append(i)
print(newlst)
'''

# 23. Write a program to fetch all palindrome words which starts with 'm' character?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'malayalam']
newlst = []

for i in names:
    if i == i[-1::-1] and i[0]=='m':
        newlst.append(i)
print(newlst)
'''
        
# 24. Write a program to fetch all palindrome words which more then 3 characters? 
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam','malayalam']
newlst = []

for i in names:
    if i == i[-1::-1] and len(i[-1::-1]) > 3:
        newlst.append(i)
print(newlst)
'''

# 25. Write a program to longest palindrome word? 
'''
names = ['madam','abcdefedcba', 'python','dad','language','eye','malayalam'] #['malayalam']
newlst = []

for i in names:
    if i == i[-1::-1]:
        newlst.append(len(i))
x = max(newlst) 

for i in names:
    if i == i[-1::-1] and len(i) == x:
        print(i)
'''       
        

