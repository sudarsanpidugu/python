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
# # --------------------(or)----------------------
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
# print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[0] not in 'aeouAEOU'])

'''
# 17. Write a program to fetch all words which ends with uppercase character in the file?
'''
print([i[-1] for i in open('file.txt').read().replace('\n',',').split(',')])
'''
# 18. Write a program to count total number of characters in the file excluding commas and \ns?
'''

'''
# 19. Write a program to count total number of words in the entire file?
'''
'''
# 20. Write a program to fetch all even number words from from every line the file?
'''

'''
# 21. Write a program to fetch all words which ends with 'bha' in the file?
'''

'''
# 22. Write a program to display all TCS employees?
'''
'''
# 23. Write a program to display the company name of Chinna Employee?
'''

'''
# 24. Write a program to fetch the 2nd from 3rd line in the file?
'''
'''
# 25. Write a program to fetch the first character from each word in the 3rd line?
'''

'''
# 26. Write a program to fetch first and last character of each word in the last line?
'''
'''
# 27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
'''

'''
# 28. Write a program to count total number of words which starts with 'S' character?
'''

'''
# 29. Write a program to fetch all duplicate names in the file?
'''

'''
# 30. Write a program to count all vowels in the file? (Note: output must be in dict)
'''

'''
# 31. Write a program to reverse all words in the file?
'''

'''
# 32. Write a program to fetch all words which contains two or more then 'a' characters?
'''

'''
# 33. Write a program to fetch all words which starts and ends with 'a' character?
'''
'''
# 34. Write a program to fetch word which has more number of 'a' characters?
'''
'''
# 35. Write a program to fetch all company names which starts with vowel?
'''
'''
# 36. Write a program to display company name which contains Saroj Employee?
'''
'''
# 37. Write a program to count all words which starts and ends with consonants?
'''
'''
# 38. Write a program to fetch all company names which does not contain Venkat employee?
'''
'''
# 39. Write a program to display company name where Narayana is working?
'''
'''
# 40. Write a program to display the first word and last word from each line in dict format?
'''
'''
# 41. Write a program to fetch all names whose name starts with 'a' in NTH company?
'''
'''
# 42. Write a program to count total number of employees in CTS company?
'''
'''
# 43. Write a program to fetch all companies where Venkat employee is working?
'''
'''
# 44. Write a program to fetch all companies names which name starts with Vowel?
'''
'''
# 45. Write a program to fetch all palindrome names from the file?
'''
'''
# 46. Write a program to fetch all companies names where palindrome named employees working?
'''
'''
# 47. Write a program to fetch the lengthiest company name?
'''
'''
# 48. Write a program to fetch the lengthiest employee name in ABC company?
'''
'''
# 49. Write a program to fetch shortest employee name in the WIPRO company?
'''
'''
# 50. Write a program count total number of employees in each company(in dict format)?
'''