# print(open('file.txt','w').write('TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas\nINFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra\nWIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna\nCTS,Prabha,Subha,Debha,Rabha,Venkat,Dhoni,Surya,Saroj\nNTH,Narayana,Akhil,Arha,Venkat,Sravya,Ananya,Revanth,Aha\nABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh'))
'''
1. Write a program to fetch all data from the file.
'''
# print(open('file.txt').read())
# --------------------(or)----------------------
# print(open('file.txt').readlines())
'''
2. Write a program to read the first line from the file.
'''
# print(open('file.txt').read().split('\n')[0])
# --------------------(or)----------------------
# print(open('file.txt').readline())
# --------------------(or)----------------------
# print(open('file.txt').readlines()[0])
'''
3. Write a program to read the last line from the file.
'''
# print(open('file.txt').read().split('\n')[-1])
# --------------------(or)----------------------
# print(open('file.txt').readlines()[-1])
'''
4. Write a program to read the 3rd line from file
'''
# print(open('file.txt').read().split('\n')[2])
# --------------------(or)----------------------
# print(open('file.txt').readlines()[2])

'''
5. Write a program to count total number of characters in the file?
'''
# print(len(open('file.txt').read().replace('\n','')))
# --------------------(or)----------------------
# print(sum([len(i.replace('\n','')) for i in open('file.txt').readlines()]))
'''
6. Write a program to count total number of commas in the file?
'''
# print(open('file.txt').read().count(','))  
# --------------------(or)----------------------
# print(sum([i.replace('\n','').count(',') for i in open('file.txt').readlines()]))
'''
7. Write a program to count total number of words in the first line?
'''
# print(len(open('file.txt').read().split('\n')[0].split(',')))
# --------------------(or)----------------------
# print(len(open('file.txt').readline().split('\n')[0].split(',')))
# --------------------(or)----------------------
# print(len(open('file.txt').readlines()[0].replace('\n','').split(',')))
'''
8. Write a program to count total number of lines in the file?
'''
# print(len(open('file.txt').read().split('\n')))
# --------------------(or)----------------------
# print(len(open('file.txt').readlines()))
'''
9. Write a program to count total number of 'Sai' name in the file?
'''
# print(open('file.txt').read().replace('\n',',').count('Sai'))
# --------------------(or)----------------------
# print(sum([i.replace('\n',',').count('Sai') for i in open('file.txt').readlines()]))
'''
10. Write a program to fetch the first word from each line in the file?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') ])
# --------------------(or)----------------------
# print([i.replace('\n','').split(',')[0] for i in open('file.txt').readlines() ])
'''
11. Write a program to fetch the last word from each line?
'''
# print([i.split(',')[-1] for i in open('file.txt').read().split('\n') ])
# --------------------(or)----------------------
# print([i.replace('\n','').split(',')[-1] for i in open('file.txt').readlines() ])

'''
12. Write a program to fetch all words which starts with 'a' Character?
'''
# print([i.split(',') for i in open('file.txt').read().split('\n')])
# n = []
# for i in open('file.txt').readlines():
#     for j in i.replace('\n','').split(','):
#         if j[0] in 'Aa':
#             n.append(j)
# print(n)
# --------------------(or)----------------------
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[0] in 'Aa'])
# --------------------(or)----------------------
# n = []
# for i in open('file.txt').read().split('\n'):
#     for j in i.split(','):
#         if j[0] in 'Aa':
#             n.append(j)
# print(n)
'''
13. Write a program to fetch all words which ends with an vowel?
'''
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[0] in 'aeiouAEIOU'])
# --------------------(or)----------------------
# print([i.replace('\n','').split(',') for i in open('file.txt').readlines()])
'''
14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?
'''
# print([i.replace('\n','').split(',') for i in open('file.txt').readlines()])
# n = []
# for i in open('file.txt').read().split('\n'):
#     for j in i.split(','):
#         if j.count('a') or j.count('i'):
#             n.append(j)
# print(n)
# --------------------(or)----------------------
# n = []
# for i in open('file.txt').readlines():
#     for j in i.replace('\n','').split(','):
#         if j.count('a') or j.count('i'):
#             n.append(j)
# print(n)
'''
# 15. Write a program to fetch all words which contains only 5 characters in the file?
'''
# a = open('file.txt').read().split('\n')
# n = []
# for i in a:
#     for j in i.split(','):
#         if len(j) == 5:
#             n.append(j)
# print(n)

# print([i for i in open('file.txt').read().replace('\n',',').split(',') if len(i) == 5])

# --------------------(or)----------------------

# x=open('file.txt','r')
# y=x.read().split(',')
# z=[]
# for i in y:
#     if len(i)==5:
#         z.append(i)
# print(z)

'''
# 16. Write a program to fetch all words which does not contains vowels except i in the file?
'''
# print([k for k in open('file.txt').read().lower().replace('\n',',').split(',') if 'i' in k and 'a' not in k and 'e' not in k and 'u' not in k and 'o' not in k ])


'''
# 17. Write a program to fetch all words which ends with uppercase character in the file?
'''
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[-1].isupper()])
# (or)
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i.isupper() ])

'''
# 18. Write a program to count total number of characters in the file excluding commas and \ns?
'''
# print(len(open('file.txt').read()))
# --------------------(or)----------------------
# print(sum([len(i) for i in open('file.txt').readlines()]))
'''
# 19. Write a program to count total number of words in the entire file?
'''
# print(len(open('file.txt').read().replace('\n',',').split(',')))
# --------------------(or)----------------------
# print(sum([len(i.replace('\n','').split(',')) for i in open('file.txt').readlines()]))

'''
# 20. Write a program to fetch all even number words from from every line the file?
'''
# print([i.replace('\n',',') for j in open('file.txt') for i in j.split(',') if len(i) % 2 == 0])
'''
# 21. Write a program to fetch all words which ends with 'bha' in the file?
'''
# print([{i.replace('\n',',') for j in open('file.txt') for i in j.split(',') if i.endswith('bha')}])
'''
# 22. Write a program to display all TCS employees?
'''
# print([i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'TCS'][0])
# --------------------(or)----------------------
# print([i.split(',')[1:] for i in open('file.txt').readline() if i.split(',')[0] == 'TCS'])
# --------------------(or)----------------------
# print([i.replace('\n','').split(',')[1:] for i in open('file.txt').readlines() if i.split(',')[0] == 'TCS'][0])

'''
# 23. Write a program to display the company name of Chinna  Employee?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if 'Chinna' in i ])
# --------------------(or)----------------------
# print([i.split(',')[0] for i in open('file.txt').readlines() if 'Chinna' in i ])
'''
# 24. Write a program to fetch the 2nd from 3rd line in the file?
'''
# print(open('file.txt').read().split('\n')[2].split(',')[1])
# --------------------(or)----------------------
# print(open('file.txt').readlines()[2].split(',')[1])
'''
# 25. Write a program to fetch the first character from each word in the 3rd line?
'''
# print([i[0] for i in open('file.txt').read().split('\n')[2].split(',') ])
# --------------------(or)----------------------
# print([i[0] for i in open('file.txt').readlines()[2].split(',') ])
'''
# 26. Write a program to fetch first and last character of each word in the last line?
'''
# print([i[0]+i[-1] for i in open('file.txt').read().split('\n')[-1].split(',') ])
# --------------------(or)----------------------
# print([i[0]+i[-1] for i in open('file.txt').readlines()[-1].split(',') ])
'''
# 27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
'''
# print([i[1:-1] for i in open('file.txt').read().split('\n')[1].split(',') ])
# --------------------(or)----------------------
# print([i.replace('\n','')[1:-1] for i in open('file.txt').readlines()[1].split(',') ])

'''
# 28. Write a program to count total number of words which starts with 'S' character?
'''
# print(sum([i[0].count('S') for i in open('file.txt').read().replace('\n',',').split(',') ]))
# --------------------(or)----------------------

# a = open('file.txt').readlines()
# l = []
# for i in a:
#     for j in i.replace('\n','').split(','):
#         if j[0].count('S'):
#             l.append(j)
# print(len(l))

# or----------------------------

# print(len([j for i in open('file.txt').readlines() for j in i.replace('\n','').split(',') if j[0].count('S')]))

'''
# 29. Write a program to fetch all duplicate names in the file?
'''
# print({i: open('file.txt').read().split(',').count(i) for i in open('file.txt').read().split(',') if open('file.txt').read().split(',').count(i) > 1 })
'''
# 30. Write a program to count all vowels in the file? (Note: output must be in dict)
'''
# d = {}.fromkeys('aeiouAEIOU',0)

# for i in open('file.txt').read():
#    if i in d:
#        d[i] += 1
# print(d)

'''
# 31. Write a program to reverse all words in the file?
'''
# print([i[-1::-1] for i in open('file.txt').read().replace('\n','').split(',') ])

# --------------------(or)----------------------
# l = []
# for i in open('file.txt').readlines():
#     for j in i.replace('\n','').split(','):
#         if j[-1::-1]:
#             l.append(j[-1::-1])
# print(l)   
# --------------------(or)----------------------

# print([j[-1::-1] for i in open('file.txt').readlines() for j in i.replace('\n','').split(',')])
'''
# 32. Write a program to fetch all words which contains two or more then 'a' characters?
'''
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i.count('a') >=2])
# --------------------(or)----------------------
# print([j for i in open('file.txt').readlines() for j in i.replace('\n','').split(',') if j.count('a') >=2])

'''
# 33. Write a program to fetch all words which starts and ends with 'a' character?
'''
# print([i for i in open('file.txt').read().lower().replace('\n',',').split(',') if i[0] == 'a' and i[-1] == 'a'])
# --------------------(or)----------------------
# print([j for i in open('file.txt').readlines() for j in i.replace('\n','').lower().split(',') if j[0] == 'a' and j[-1] == 'a'])
'''
# 34. Write a program to fetch word which has more number of 'a' characters?
'''
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i.count('a') >=1])
# --------------------(or)----------------------
# print([j for i in open('file.txt').readlines() for j in i.replace('\n','').split(',') if j.count('a') >=1])

'''
# 35. Write a program to fetch all company names which starts with vowel?
'''
# =======================================================
# l = []                                             ====
# for i in open('file.txt').read().split('\n'):      ====
#     for j in i.split(','):                         ====
#         if j[0][0] in 'AaEeIiOoUu':                ====
#             l.append(j)                            ====
# print(l)                                           ====
                                                #   WRONG
# l = []                                             ====
# for i in open('file.txt').readlines():             ==== 
#     for j in i.replace('\n','').split(','):        ====
#         if j[0]  in 'AaEeIiOoUu':                  ==== 
#             l.append(j)                            ====
# print(l)                                           ====
# '====================================================='

# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if i[0] in 'aeiouAEIOU'])
# --------------------(or)----------------------
# print([i.split(',')[0] for i in open('file.txt').readlines() if i.replace('\n','')[0] in 'aeiouAEIOU'])
'''
36. Write a program to display company name which contains Saroj Employee?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if 'Saroj' in i])

'''
37. Write a program to count all words which starts and ends with consonants?
'''
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[0] not in 'AEIOUaeiou' and i[-1] not in 'AEIOUaeiou'])
'''
38. Write a program to fetch all company names which does not contain Venkat employee?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if 'Venkat' not in i])

'''
# 39. Write a program to display company name where Narayana is working?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if 'Narayana' in i])

'''
# 40. Write a program to display the first word and last word from each line in dict format?
'''
# print([i[0]+i[-1] for i in open('file.txt').read().split('\n')  ] )
# --------------------(or)----------------------
# print([i.replace('\n','')[-1]+i[0] for i in open('file.txt').readlines() ])

'''
# 41. Write a program to fetch all names whose name starts with 'a' in NTH company?
'''
# a = [j for j in [i.split(',')[1:]  for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'NTH' ]]

# list = []
# for k in a[0] :
#     if k[0] in 'A' :
#         list.append(k)
# print(list)

# --------------------(or)----------------------

# print([k for k in [j for j in [i.split(',')[1:]  for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'NTH' ]][0] if k[0] in 'A'] )

'''
# 42. Write a program to count total number of employees in CTS company?
'''
# print(len([i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'CTS'][0]))
'''
# 43. Write a program to fetch all companies where Venkat employee is working?
'''
# print([i.split(',')[0] for i in open('file.txt').read().split('\n') if 'Venkat' in i])

'''
# 44. Write a program to fetch all companies names which name starts with Vowel?
'''
# x = open('file.txt').read().lower().replace('\n',',').split(',')
'''
# 45. Write a program to fetch all palindrome names from the file?
'''
# x = open('file.txt').read().lower().replace('\n',',').split(',')
# # print(x)
# newlst = []

# for i in x:
#     if i == i[-1::-1]:
#         newlst.append(i)
# print(newlst)

# --------------------(or)----------------------

# print([i for i in open('file.txt').read().lower().replace('\n',',').split(',') if i == i[::-1]  ])
'''
# 46. Write a program to fetch all companies names where palindrome named employees working?
'''
# a = ([i.lower().replace('\n','').split(',') for i in open('file.txt').readlines()])
# print(a)
# for i in a:
    # if i[0] :

# s=open('file.txt').read().split('\n')
# l = []
# for i in s:
#     for j in i.split(','):
#         if j == i[::-1]:
#             l.append(j)
#     print(j)
    

'''
# 47. Write a program to fetch the lengthiest company name?
'''
# for i in [j for j in [i.split(',')[0] for i in open('file.txt').read().split('\n') if i.split(',')] ]:
#     if len(i) == (max([len(j) for j in [i.split(',')[0] for i in open('file.txt').read().split('\n') if i.split(',')] ])):
#         print(i)

# 48. Write a program to fetch the lengthiest employee name in ABC company?

# a = open('file.txt').read().replace('\n','').split(',')
# print(a)
# b = (max([len(j) for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'WIPRO'][0] ]))
# a = (([j for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'WIPRO'][0] ]))

# print(a)
# print(b)
# --------------------(or)----------------------

# for i in [j for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'ABC'][0] ]:
#     if  len(i) == max([len(j) for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'ABC'][0]]):
#         print(i)

'''
# 49. Write a program to fetch shortest employee name in the WIPRO company?
'''
# for i in [j for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'WIPRO'][0] ]:
#     if  len(i) == min([len(j) for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')[0] == 'WIPRO'][0]]):
#         print(i)
'''
# 50. Write a program count total number of employees in each company(in dict format)?
'''
# b = (([len(j) for j in [i.split(',')[1:] for i in open('file.txt').read().split('\n') if i.split(',')] ]))
# # print(b)

# a = ([(j) for j in [i.split(',')[0] for i in open('file.txt').read().split('\n') if i.split(',')] ])
# # print(a)
# d= {}
# for i,j in zip(a, b):
#     d[i] = j
# print(d)



