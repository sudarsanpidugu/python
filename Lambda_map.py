# 1. Write a program to fetch all even numbers from list?
lst = [10,11,13,14,9,8] #[10,14,8]
# print(list(map(lambda i : i%2 == 0,lst))) --------------------------------
# 2. Write a program to fetch all string values from list? 
'''
lst = [10,'a',True,'b',False] #['a', 'b']
print(list(map(lambda i: str(i) if isinstance(i, str) else '', lst)))
'''
# 3. Write a program to fetch all 5 divisibles from list? 
lst = [12,15,27,20,5] #[15,20,5]
# 4. Write a program to count total number of int values in the list?
lst = [10,'a',20,True,30,'b',40] #4
# 5. Write a program to count total number of characters in the string(including space)?. 
'''
st = 'Python language' #15
print(len(list(map(lambda i : len(i),st))))
'''
# 6. Write a program to count total number of words in the string.
'''
st = 'python narayana tech house hyd' #5
print(len(list(map(lambda i: i,st.split()))))
'''
# 7. Write a program to fetch all vowels from the string?
'''
st = 'Python language' #['o','a','u','a','e']
vowels = ['a', 'e', 'i', 'o', 'u']
print(list(map(lambda i: i, filter(lambda i: i in vowels, st))))
'''
# 8. Write a program to count total number of vowels ?
st = 'python narayana' #5
# 9. Write a program to count total number of characters in the string(excluding space)?
st = 'python is a simple language' #23
# 10. Write a program to count total number of consonants in the string?
st = 'python language' #9
# 11. Write a program to fetch all words which starts with vowel from given string?
st = 'Python is simple and easy language' #['is', 'and', 'easy']
# 12. Write a program to fetch all words which ends with consonent in the given string?
st = 'Python is simple and easy language' #['Python', 'is','and', 'easy']
# 13. Write a program to fetch all words which 'a' two or more then two times? 
st = 'Python is simple and easy language' #['language']
# 14. Write a program to count number of characters of each word in the string?
'''
st = 'Python is simple and easy language' #[6,2,6,3,4,8]
print(list(map(lambda i: len(i), st.split())))
'''
# 15. Write a program to fetch the first and last character from each word in the string?
'''
st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
print(list(map(lambda i: i[0]+i[-1] ,st.split())))
'''
# 16. Write a program to fetch all words which contains 'a' character in the string?
st = 'Python is simple and easy language' #['and', 'easy', 'language']
print(list(map(lambda i: i ,st.split)))
# 17. Write a program to fetch all words which does not contain 'e' character in string? 
st = 'Python is simple and easy language' #['Python', 'is', 'and']
# 18. Write a program to fetch all words which contains only 4 or lessthen 4 characters? 
st = 'Python is simple and easy language' #['is', 'and', 'easy']
# 19. Write a program to fetch all words which contain odd number of characters in the string?
st = 'Python is simple and easy language' #['and']
# 20. Write a program to fetch all words which starts and ends with vowel in the string?
st = 'Python is number one language' #['one']
# 21. Write a program to fetch all palindrome words from list? 
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'dada', 'eye', 'malayalam']
# 22. Write a program to fetch all non-palindrome words from list? 
names = ['madam', 'python','dad','language','eye','malayalam'] #['python', 'language']
# 23. Write a program to fetch all palindrome words which starts with 'm' character?
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'malayalam']
# 24. Write a program to fetch all palindrome words which more then 3 characters? 
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam','malayalam']
# 25. Write a program to longest palindrome word?
names = ['madam', 'python','dad','language','eye','malayalam'] #['malayalam']