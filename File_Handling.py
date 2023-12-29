'''
Creating empty text file:-
'''
# print(open('test.txt', 'w'))
'''
Writing Data:-
'''
# print(open('test.txt','w').write('Hello sudarsan'))
'''
Data OverWriting:-
'''
# print(open('test.txt', 'w').write('Welcom Sudarsan'))
'''
Add new data without overwriting:-
'''
# print(open('test.txt', 'a').write('Software'))   
'''
Adding Multiple lines:-
'''
# print(open('test.txt', 'a').write('\nPython Devloper\nIMB'))   
'''
File Read/Output operation:-
'''
'''
read() the data:-
'''
# print(open('test.txt', 'r').read())
'''
readline() the data:-first line only can be show
'''
# print(open('test.txt').readline())
'''
readlines() the data:-data will show all in list formate
'''
# print(open('test.txt').readlines())
# -----------------------------------------------------------------------------------------
'''
Writing Data:-
'''
# print(open('test.txt','w').write('TCS,Ravi,Ram,Sudha,Siva,Basu\n WIPRO,Babu,Karthik,Sandesh,Teja,Kisan\n INOFSYS,Venky,Teja,Alber,Babu,Vijay\n GOOGLE,Sai,Mayuru,Aswini,Mounika,Neeraja\n NTH,Indhu,Supriya,Divya,Teja,Bhavani'))
'''
Write a program to fetch all the data from the file? :-
'''
# print(open('test.txt').read())
'''
Write a program to fetch the first line?
'''
# print(open('test.txt').read().split('\n')[0])
# --------------------# (or) -------------------#
# print(open('test.txt').readline())
# --------------------# (or) -------------------#
# print(open('test.txt').readlines()[0])
'''
3.Write a program to fetch the last line from the file?
'''
# print(open('test.txt').read().split()[-1])
# --------------------# (or) -------------------#
# print(open('test.txt').readlines()[-1])
'''
4.Write a program to fetch third line from the file?
'''
# print(open('test.txt').read().split()[2])
# --------------------# (or) -------------------#
# print(open('test.txt').readlines()[2])
'''
4.Write a program to count number of line in the file?
'''
# print(len(open('test.txt').read().split()))
# --------------------# (or) -------------------#
# print(len(open('test.txt').readlines()))
'''
6.Write a program to find number of commes?
'''
# print(open('test.txt').read().count(','))
# --------------------# (or) -------------------#
# x = open('test.txt').readlines()
# y = 0
# for i in x:
#     y = y+i.count(',')
# print(y)
# --------------------# (or) -------------------#
'''
7.Write a program to count number of words in the first line?
'''
# print(len(open('test.txt').read().split()[0].split(',')))
# --------------------# (or) -------------------#
# print(len(open('test.txt').readline().split(',')))
# --------------------# (or) -------------------#
# print(len(open('test.txt').readlines()[0].split(',')))

'''
8.Write a program to count number of words in the last line?
'''
# print(len(open('test.txt').read().split()[-1].split(',')))
# --------------------# (or) -------------------#
# print(len(open('test.txt').readlines()[-1].split(',')))
'''
9.Write a program to fetch the first word from each line?
'''
# print([i.split(',')[0] for i in open('test.txt').readlines()])

'''
10.Write a program to count number of vowels in the files?
'''
# data = open('test.txt').read()
# v = ('aeiouAEIOU')
# d = {}.fromkeys(v,0)
# for i in data:
#     if i in d:
#         d[i]=d[i]+1
# print(d)
'''
11.Write a program to fetch third word from second line?
'''
# print(open('test.txt').read().split('\n')[1].split(',')[2])
# --------------------# (or) -------------------#

# print(open('test.txt').readlines()[1].split(',')[2])
'''
12.Write a program to fetch the last word from last line?
'''
# print(open('test.txt').read().split('\n')[-1].split(',')[-1])
# --------------------# (or) -------------------#
# print(open('test.txt').readlines()[-1].split(',')[-1])
'''
13.Write a program to fetch the last word from each line?
'''
# print([i.replace('\n','').split(',')[-1] for i in open('test.txt').readlines()])
# --------------------# (or) -------------------#
# print([i.split(',')[-1] for i in open('test.txt').read().split('\n')])

'''
14.Write a program to fetch the first character from second words in third line?
'''
# print(open('test.txt').readlines()[2].split(',')[1][0])
# --------------------# (or) -------------------#
# print(open('test.txt').read().split('\n')[2].split(',')[1][0])
'''
15.Write a program to fetch all the names which starts with 'a' charcter?
'''
# for i in open('test.txt').readlines():
#     for j in i.split(','):
#         if j[0] in 'Aa':
#             print(j)

# --------------------# (or) -------------------#

# print([i for i in open('test.txt').read().replace('\n',',').split(',')])


'''
16.Write a program to fetch all the names which has either 4 or 5 characters?
'''
# a = open('test.txt').read()
# s = a.replace('\n',',').split(',')
# lst = []
# for i in s:
#     if len(i) in [4,5]:
#         lst.append(i)
# print(lst)
# --------------------# (or) -------------------#
# print([i for i in open('test.txt').read().replace('\n',',').split(',') if len(i) in [4,5]])
'''
17.Write a program to fetch all words which starts and ends with vowel?
'''
# print([i for i in open('test.txt').read().replace('\n',',').split(',') if i[0] in 'aeiouAEIOU' and i[-1] in 'aeiouAEIOU'])
'''
18.Write a program to fetch all words which has add number of characters?
'''
# print([i for i in open('test.txt').read().replace('\n',',').split(',') if len(i)%2 ==1])
# --------------------# (or) -------------------#
# x = open('test.txt').read().split('\n')[0].split(',')
# print(x)
'''
19.Write a program to fetch all words which has even number of characters and starts with vowels?
'''
# print([i for i in open('test.txt').read().replace('\n',',').split(',') if len(i)%2 ==0 and i[0] in 'aeiouAEIOU'])
'''
20.Write a program to display all employess names of TCS company?
'''
# print([i.split(',')[1:] for i in open('test.txt').read().split('\n') if i.split(',')[0] == 'TCS'][0])
'''
21.Write a program to display company name where Sai is working?
'''
# print([i.split(',')[0] for i in open('test.txt').read().split('\n') if 'Sai' in i])

'''
22.Write a program to display company name where Teja is not working?
'''
# print([i.split(',')[0] for i in open('test.txt').read().split('\n') if 'Teja' not in i])

'''
23.Write a program to  display company names and third emp count in dict format ?
'''
# companys = [i.split(',')[0] for i in open('test.txt').read().split('\n')]
# counting = [len(i.split(',')[1:]) for i in open('test.txt').read().split('\n')]

# d= {}
# for i,j in zip(companys, counting):
#     d[i] = j
# print(d)
'''
24.Write a program to display first word and last word of each line in dict format?
'''
# fwords = [i.split(',')[0] for i in open('test.txt').read().split('\n')]
# lwords = [i.split(',')[-1] for i in open('test.txt').read().split('\n')]

# d = {}
# for i,j in zip(fwords,lwords):
#     d[i] = j
# print(d)

'''
24.Write a program to display emp names which is available two or more then two names?
'''
# a = open('test.txt').read().replace('\n',',').split(',')
# lst = []
# for i in a:
#     if a.count(i) >= 2:
#         lst.append(i)
# print(list(lst))
# --------------------# (or) -------------------#
# print(list(set([i for i in open('test.txt').read().replace('\n',',').split(',') 
#                 if  open('test.txt').read().replace('\n',',').count(i) >= 2])))