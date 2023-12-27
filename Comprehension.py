# 1. Write a Compretesion to fetch all even numbers from list?
''' 
lst = [10,11,13,14,9,8] #[10,14,8] 
print([i for i in lst if i%2 == 0])
'''
# 2. Write a Compretesion to fetch all string values from list? 
'''
lst = [10,'a',True,'b',False] #['a', 'b']
print([i for i in lst if type(i) == str])
'''
# 3. Write a Compretesion to fetch all 5 divisibles from list? 
'''
lst = [12,15,27,20,5] #[15,20,5]
print([i for i in lst if i%5 == 0])
'''
# 4. Write a Compretesion to count total number of int values in the list?
'''
lst = [10,'a',20,True,30,'b',40] #4
print(len([i for i in lst if type(i) == int]))
'''
# 5. Write a Compretesion to count total number of characters in the string(including space)?.
'''
st = 'Python language' #15
print(len(st))
'''
# 6. Write a Compretesion to count total number of words in the string.
'''
st = 'python narayana tech house hyd' #5
print(len([i for i in st.split() ]))
'''
# 7. Write a Compretesion to fetch all vowels from the string? 
'''
st = 'Python language' #['o','a','u','a','e']
print([i for i in st if i in 'aeiou'])
'''
# 8. Write a Compretesion to count total number of vowels?
'''
st = 'python narayana' #5
print(len([i for i in st if i in 'aeiou']))
'''
# 9. Write a Compretesion to count total number of characters in the string(excluding space)?
'''
st = 'python is a simple language' #23
print(len([i for i in st if i != ' ' ]))
'''
# 10. Write a Compretesion to count total number of consonants in the string? 
'''
st = 'python language' #9
print(len([i for i in st if i != " " and i not in 'aeiou']))
'''
# 11. Write a Compretesion to fetch all words which starts with vowel from given string?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
print([i for i in st.split() if i[0] in 'aeiou'])
'''
# 12. Write a Compretesion to fetch all words which ends with consonent in the given string? 
'''
st = 'Python is simple and easy language' #['Python', 'is','and', 'easy']
print([i for i in st.split() if i[-1] not in 'aeiou' ])
'''
# 13. Write a Compretesion to fetch all words which 'a' two or more then two times?
'''
st = 'Python is simple and easy language' #['language']
print([i for i in st.split() if i.count('a') >=2 ])
'''
# 14. Write a Compretesion to count number of characters of each word in the string?
'''
st = 'Python is simple and easy language' #[6,2,6,3,4,8]
print(([len(i) for i  in st.split() ]))
'''
# 15. Write a Compretesion to fetch the first and last character from each word in the string?
'''
st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
print([i[0]+i[-1] for i in st.split() if i[0] and i[-1]])
'''
# 16. Write a Compretesion to fetch all words which contains 'a' character in the string?
'''c 
st = 'Python is simple and easy language' #['and', 'easy', 'language']
print([i for i in st.split() if i.count('a') >=1])
'''
# 17. Write a Compretesion to fetch all words which does not contain 'e' character in string?
'''
st = 'Python is simple and easy language' #['Python', 'is', 'and']
print([i for i in st.split() if i.count('a')<= 0])
'''
# 18. Write a Compretesion to fetch all words which contains only 4 or lessthen 4 characters?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
print([i for i in st.split() if len(i) <=4])
'''
# 19. Write a Compretesion to fetch all words which contain odd number of characters in the string?
'''
st = 'Python is simple and easy language' #['and']
print([i for i in st.split() if len(i)%2 == 1  ])
'''
# 20. Write a Compretesion to fetch all words which starts and ends with vowel in the string?
'''
andst = 'Python is number one language' #['one']
print([i for i in st.split() if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''
# 21. Write a Compretesion to fetch all palindrome words from list? 
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'dada', 'eye', 'malayalam']
print([i for i in names if i == i[-1::-1]])
'''
# 22. Write a Compretesion to fetch all non-palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['python', 'language']
print([i for i in names if i != i[-1::-1]])
'''
# 23. Write a Compretesion to fetch all palindrome words which starts with 'm' character?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'malayalam']
print([i for i in names if i == i[-1::-1] and i[0] == 'm'])
'''
# 24. Write a Compretesion to fetch all palindrome words which more then 3 characters? 
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam','malayalam']
print([i for i in names if i == i[-1::-1] and len(i) > 3])
'''
# 25. Write a Compretesion to longest palindrome word? 

names = ['madam', 'abcdefghgfedcba','abcdefgfedcba', 'python', 'dad', 'language', 'eye', 'malayalam']
l = max([len(i) for i in names if i == i[::-1]])
print([i for i in names if i == i[::-1] and len(i) == l])