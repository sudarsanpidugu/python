# 1. Write a Function to fetch all even numbers from list? 
'''
lst = [10,11,13,14,9,8] #[10,14,8]
def fetchEvenNum(lst):
    
    newlst = []
    for i in lst:
        if i%2 == 0:
            newlst.append(i)
    print(newlst)
fetchEvenNum(lst)

lst = [10,50,20,15,30,14,12,8,9,4,3]
fetchEvenNum(lst)
'''
# 2. Write a Function to fetch all string values from list?
'''
lst = [10,'a',True,'b',False] #['a', 'b']
def Fetch_String_value(lst):
    
    newlst = []

    for i in lst:
        if type(i) == str:
            newlst.append(i)
    print(newlst)
Fetch_String_value(lst)
'''
# 3. Write a Function to fetch all 5 divisibles from list?
'''
lst = [12,15,27,20,5] #[15,20,5]
def Fetch_Five_Divisibles(lst):
    
    newls = []

    for i in lst:
        if i%5 == 0:
            newls.append(i)
    print(newls)
Fetch_Five_Divisibles(lst)
'''
# 4. Write a Function to count total number of int values in the list?
'''
lst = [10,'a',20,True,30,'b',40] #4

def CountNum_int_Value(lst):
     
    newlst = []
    for i in lst:
        if type(i) == int :
                newlst.append(i)
    print(len(newlst))
CountNum_int_Value(lst)    
''' 
# 5. Write a Function to count total number of characters in the string(including space)?.
'''

st = 'Python language' #15

def count_num_char(st):
    print(len(st))
    
count_num_char(st)

'''

# 6. Write a Function to count total number of words in the string. 
'''
st = 'python narayana tech house hyd' #5
def count_total_number (st):
    new = st.split()
    print(len(new))
count_total_number (st)
'''
# 7. Write a Function to fetch all vowels from the string? 
'''
st = 'Python language' #['o','a','u','a','e']
def Fetch_all_vowels(st):
    newlst = []
    for i in st:
        if i in 'aeiou':
            newlst.append(i)
    print(newlst)
Fetch_all_vowels(st)
'''
# 8. Write a Function to count total number of vowels?
'''
st = 'python narayana' #5
def count_num_vowels(st):
    newlst = []
    for i in st:
        if i in 'aeiou':
            newlst.append(i)
    print(len(newlst))
count_num_vowels(st)
'''
# 9. Write a Function to count total number of characters in the string(excluding space)? 
'''
st = 'python is a simple language' #23 is wrong ,
# print(len(st))
def number_char_exclu(st):
    newlst = []
    for i in st:
        if i != ' ':
            newlst.append(i)
    print(len(newlst))
number_char_exclu(st)
'''
# 10. Write a Function to count total number of consonants in the string? 
'''
st = 'python language' #9
def count_num_consonents(st):
    newlst = []
    for i in st:
        if i!= ' ' and i not in 'aeiou'  :
            newlst.append(i)
    print(len(newlst))
count_num_consonents(st)
'''
# 11. Write a Function to fetch all words which starts with vowel from given string?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
def fetch_all_words_start_vowel(st):
    st1 = st.split()
    newlst = []
    for i in st1:
        if i[0] in 'aeiou':
            newlst.append(i)
    print((newlst))
fetch_all_words_start_vowel(st)
'''
# 12. Write a Function to fetch all words which ends with consonent in the given string?
'''
st = 'Python is simple and easy language' #['Python', 'is','and', 'easy']
def fetch_all_words_end_vowel(st):
    s = st.split()
    newlst = []
    for i in s:
        if i[-1] not in  'aeiou':
            newlst.append(i)
    print(newlst)
fetch_all_words_end_vowel(st)
'''
# 13. Write a Function to fetch all words which 'a' two or more then two times?
'''
st = 'Python is simple and easy language' #['language']
def fetch_all_words_a_morethenTwo (st):
    s = st.split()
    newlst = []
    for i in s:
        if i.count('a') >= 2:
            newlst.append(i)
    print(newlst)         
fetch_all_words_a_morethenTwo (st)
'''
# 14. Write a Function to count number of characters of each word in the string? 
'''
st = 'Python is simple and easy language' #[6,2,6,3,4,8]
def Num_cher_eachWord (st):
    st1 = st.split(' ')
    newlst = []
    for i in st1:
        newlst.append(len(i))
    print(newlst)
Num_cher_eachWord (st)
'''
# 15. Write a Function to fetch the first and last character from each word in the string?
'''
st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
def First_Last_char_eachWord(st):
    s = st.split()
    newlst = []
    for i in s:
        if i[0] and i[-1]:
            newlst.append(i[0]+i[-1])
    print(newlst)
First_Last_char_eachWord(st)
'''
# 16. Write a Function to fetch all words which contains 'a' character in the string?
'''
st = 'Python is simple and easy language' #['and', 'easy', 'language']
def Fetch_allWord_contains_a(st):
    s = st.split()
    newlst = []
    for i in s:
        if i.count('a') >= 1:
            newlst.append(i)
    print(newlst)
Fetch_allWord_contains_a(st)
'''

# 17. Write a Function to fetch all words which does not contain 'e' character in string?
'''
st = 'Python is simple and easy language' #['Python', 'is', 'and']
def Fetch_allWord_doesnot_contain_e(st):
    s = st.split()
    newlst = []
    for i in s:
        if i.count('a') <= 0:
            newlst.append(i)
    print(newlst)
Fetch_allWord_doesnot_contain_e(st)
'''
# 18. Write a Function to fetch all words which contains only 4 or lessthen 4 characters? 
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
def FetchallWords_contains_4orlessthen4_characters(st):
    s = st.split()
    newlst = []
    for i in s:
        if len(i) <= 4:
            newlst.append(i)
    print(newlst)
FetchallWords_contains_4orlessthen4_characters(st)
'''
# 19. Write a Function to fetch all words which contain odd number of characters in the string?
'''
st = 'Python is simple and easy language' #['and']
def  FetchallWords_contains_oddNum_characters(st):
    s = st.split()
    newlst = []

    for i in s:
        if len(i)%2==1:
            newlst.append(i)
    print(newlst)
FetchallWords_contains_oddNum_characters(st)
'''
# 20. Write a Function to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is number one language' #['one']
s = st.split()
newlst = []
for i in s:
    if i[0] in 'aeiou' and i[-1] in 'aeiou':
        newlst.append(i)
print(newlst) 
'''
# 21. Write a Function to fetch all palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] # #['madam', 'dad', 'eye', 'malayalam']
def Fetch_all_palindrome(names):
    newlst = []
    for i in names:
        if i == i[-1::-1]:
            newlst.append(i)
    print(newlst)
Fetch_all_palindrome(names)
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


# 22. Write a Function to fetch all non-palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['python', 'language']
def Fetch_all_non_palindrome (names):
    newlst = []
    for i in names:
        if i != i[-1::-1]:
            newlst.append(i)
    print(newlst)
Fetch_all_non_palindrome (names)
'''
# 23. Write a Function to fetch all palindrome words which starts with 'm' character?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'malayalam']
def fetch_all_palindrome_startwith_m (names):
    newlst = []
    for i in names:
        if i == i[-1::-1] and i[0]=='m':
            newlst.append(i)
    print(newlst)
fetch_all_palindrome_startwith_m (names)
'''     
# 24. Write a Function to fetch all palindrome words which more then 3 characters? 
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam','malayalam']
def Fetch_all_palindrome_whichMorethen3_char (names):
    newlst = []
    for i in names:
        if i == i[-1::-1] and len(i[-1::-1]) > 3:
            newlst.append(i)
    print(newlst)
Fetch_all_palindrome_whichMorethen3_char (names)
'''

# 25. Write a Function to longest palindrome word? 

names = ['madam', 'python','dad','language','eye','malayalam'] #['malayalam']
def Longest_palindrome_word (names):
    newlst = []
    for i in names:
        if i == i[-1::-1]:
            newlst.append(len(i))
    l = max(newlst)
    for i in names:
        if i == i[::-1] and len(i) == l:
            print(i)
Longest_palindrome_word (names)