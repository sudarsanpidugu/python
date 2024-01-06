data='''
'Mr. Kumar has learned Python Language from NTH Institute and placed in TCS Company with 20000 salary,
'Mr. Suresh has learned Java Language from ABC Institute and placed in HCL Company with 30000 salary,
'Ms. Kavya has learned C Language from NTH Institute and placed in Wipro Company with 25000 salary,
'Mrs. Navya has learned C++ Language from XYZ Institute and placed in TCS Company with 10000 salary,
'Ms. Bavya has learned MYSQL Database from NTH Institute and placed in CTS Company with 30000 salary,
'Mrs. Sravya has learned Oracle Database from ABC Institute and placed in Wipro Company with 90000 salary
'''

import re
#1.WAP to get student names? #['Mr.Kumar', 'Mr.Suresh', 'Ms.Kavya', 'Mrs.Navya', 'Ms.Bavya', 'Mrs.Sravya']
'''
print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',data))
'''
#2.WAP to get all male student names? #['Mr. Kumar', 'Mr. Suresh']
'''
print(re.findall('Mr. [A-Za-z]{1,}',data))
'''
#3.WAP to get all female student names? #['Ms. Kavya', 'Mrs. Navya', 'Ms. Bavya', 'Mrs. Sravya']
'''
print(re.findall('M[r]?s. [A-Za-z]{1,}',data))
'''
#4.WAP to get all married female students names?#['Mrs. Navya', 'Mrs. Sravya']
'''
print(re.findall('Mrs. [A-Za-z]{1,}',data))
'''
#5.WAP to get all unmarried female students names?#['Ms. Kavya', 'Ms. Bavya']
'''
print(re.findall('Ms. [A-Za-z]{1,}',data))
'''
#6.WAP to get all courses names?#[' Python', ' Java', ' C', ' C++', ' MYSQL', ' Oracle']
'''
print([i.replace('learned','')for i in re.findall('learned [A-Za-z+]{1,}',data)])
'''
#7.WAP to get all languages names?#['Python ', 'Java ', 'C ', 'C++ ']
'''
m=re.findall('[A-Za-z+]{1,} Language',data)
print([i.replace('Language','')for i in m])

print([i.replace('Language','')for i in re.findall('[A-Za-z+]{1,} Language',data)])
'''
#8.WAP to get all databases names?#['MYSQL ', 'Oracle ']
'''
m=re.findall('[A-Za-z]{1,} Database',data)
print([i.replace('Database','')for i in m])

print([i.replace('Database','')for i in re.findall('[A-Za-z]{1,} Database',data)])
'''
#9.WAP to get all institutes names?#['NTH ', 'ABC ', 'NTH ', 'XYZ ', 'NTH ', 'ABC ']
'''
print(re.findall('[A-Z]{1,} Institute',data))

m=re.findall('[A-Z]{1,} Institute',data)
print([i.replace('Institute','')for i in m])

print([i.replace('Institute','')for i in re.findall('[A-Z]{1,} Institute',data)])
'''
#10.WAP to get all companies names?#['TCS ', 'HCL ', 'Wipro ', 'TCS ', 'CTS ', 'Wipro ']
'''
m=re.findall('[A-Za-z]{1,} Company',data)
print([i.replace('Company','')for i in m])

print([i.replace('Company','')for i in re.findall('[A-Za-z]{1,} Company',data)])
'''
#11.WAP to get all salaries?#['20000 ', '30000 ', '25000 ', '10000 ', '30000 ', '90000 ']
'''
m=re.findall('[0-9]{1,} salary',data)
print([i.replace('salary','')for i in m])

print([i.replace('salary','')for i in re.findall('[0-9]{1,} salary',data)])
'''
#12.WAP to get language name of Mr.Kumar?#['Python ']

'''
m=data.split(',')
for i in m:
    if 'Mr. Kumar' in i:
        print([j.replace('Language','')for j in re.findall('[A-Za-z]{1,} Language',i)])
'''

#13.WAP to get Company name of Mr.Suresh?#['HCL ']
'''
m=data.split(',')
for i in m:
    if 'Mr. Suresh'in i:
        print([j.replace('Company','')for j in re.findall('[A-Za-z]{1,} Company',i)])
'''
#14.WAP to get both institute name Company name of Ms.Kavya?#['NTH '],['Wipro ']
'''
m=data.split(',')
for i in m:
    if 'Ms. Kavya'in i:
        print([j.replace('Institute','')for j in re.findall('[A-Za-z]{1,} Institute',i)])
        print([j.replace('Company','')for j in re.findall('[A-Za-z]{1,} Company',i)])
'''
#15.WAP to get both language name salary name of Mr.Suresh?['Java '],['30000 ']
'''
m=data.split(',')
for i in m:
    if 'Mr. Suresh'in i:
        print([j.replace('Language','')for j in re.findall('[A-Za-z]{1,} Language',i)])
        print([j.replace('salary','')for j in re.findall('[0-9]{1,} salary',i)])
'''
#16.WAP to get all details of Ms.Bavya?#['MYSQL Database'],['30000 salary'],['CTS Company'],['NTH Institute']
'''
m=data.split(',')
for i in m:
    if 'Ms. Bavya'in i:
        print(re.findall('[A-Za-z]{1,} Database',i))
        print(re.findall('[0-9]{1,} salary',i))
        print(re.findall('[A-Za-z]{1,} Company',i))
        print(re.findall('[A-Za-z]{1,} Institute',i))
'''
#17.WAP to get all students names who learned course from NTH Institute?#['Mr. Kumar'],['Ms. Kavya'],['Ms. Bavya']
'''
m=data.split(',')
for i in m:
    if 'NTH'in i:
        print(re.findall('M[rs]?. [A-Za-z]{1,}',i))
'''

#18.WAP to get all students names who learned languages?#['Mr. Kumar'],['Mr. Suresh'],['Ms. Kavya'],['Mrs. Navya']
'''
m=data.split(',')
for i in m:
    if 'Language'in i:
        print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',i))
'''
#19.WAP to get all students names who learned databases?#['Ms. Bavya'],['Mrs. Sravya']
'''
m=data.split(',')
for i in m:
    if 'Database'in i:
        print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',i))
'''
#20.WAP to get all students names who joined in TCS Company?#['Mr. Kumar'],['Mrs. Navya']
'''
m=data.split(',')
for i in m:
    if 'TCS'in i:
        print(re.findall('Mr?[s]?. [A-Za-z]{1,}',i))
'''
#21.WAP to get all students names who getting more than 20000 salary?
    
#22.WAP to get all salaries of male students?#['20000 '],['30000 ']
'''
m=data.split(',')
for i in m:
    if 'Mr. 'in i:
        print([i.replace('salary','')for i in re.findall('[0-9]{1,} salary',i)])
'''        
#23.WAP to get all company names of female students?#['Wipro '],['TCS '],['CTS '],['Wipro ']
'''
m=data.split(',')
for i in m:
    if 'Ms. 'in i or 'Mrs. 'in i:
        print([i.replace('Company','')for i in re.findall('[A-Za-z]{1,} Company',i)])
'''
#24.WAP to get male student name who is  getting highest salary?#30000['Mr. Suresh']
'''
x=[re.findall('[0-9]{1,} salary',i) for i in data.split(',')if 'Mr. 'in i]
sal=[]
for i in x:
    sal.append(int(i[0].replace(' salary','')))
maxSal=max(sal)
print(maxSal)
y=[re.findall('Mr. [A-Za-z]{1,}',i) for i in data.split(',')if str(maxSal)in i and 'Mr. 'in i][0]
print(y)
'''        
#25.WAP to get female student name who is  getting least salary?#['Mrs. Navya ']
'''
minNum = min([int(i[0].replace(' salary','')) for i in [re.findall('[0-9]{1,} salary',i) for i in data.split(',')]])
print(minNum)

for i in data.split(','):
    x = re.findall('[0-9]{1,} salary',i)[0].replace(' salary','')
    if int(x) == minNum:
        print(re.findall('M[r]?s. [A-Za-z]{1,} ',i))
'''
#26.WAP to get all male students names who is not joined HCL Company?#['Mr. Kumar']
'''
m=data.split(',')
for i in m:
    if 'Mr. 'in i and 'HCL'not in i:
        print(re.findall('Mr. [A-Za-z]{1,}',i))
'''
#27.WAP to get all students names who did not learn languages?#['Ms. Bavya']['Mrs. Sravya']
'''
m=data.split(',')
for i in m:
    if 'Language'not in i:
        print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',i))
'''
#28.WAP to get all students names who did not learn databases?['Mr. Kumar']['Mr. Suresh']['Ms. Kavya']['Mrs. Navya']
'''
m=data.split(',')
for i in m:
    if 'Database'not in i:
        print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',i))
'''      
#29.WAP to get salaries of all NTH Students?#['20000 '],['25000 '],['30000 ']
'''
m=data.split(',')
for i in m:
    if 'NTH' in i:
        print([i.replace('salary','')for i in re.findall('[0-9]{1,} salary',i)])
'''
#30. WAP to get all salaries of students who did not XYZ Institute?['20000 ']['30000 ']['25000 ']['30000 ']['90000 ']
'''
m=data.split(',')
for i in m:
    if 'XYZ'not in i:
        print([i.replace('salary','')for i in re.findall('[0-9]{1,} salary',i)])
'''
#31. WAP to get all institute names which is providing python language?#['NTH ']
'''
m=data.split(',')
for i in m:
    if 'Python' in i:
        print([i.replace('Institute','')for i in re.findall('[A-Za-z]{1,} Institute',i)])
'''    
#32. WAP to get all institute names which is providing database courses?#['NTH ']['ABC ']
'''
m=data.split(',')
for i in m:
    if 'Database' in i:
        print([i.replace('Institute','')for i in re.findall('[A-Za-z]{1,} Institute',i)])
'''     
#33. WAP to get male student names who joined HCL Company?#['Mr. Suresh']
'''
m=data.split(',')
for i in m:
    if 'HCL'in i:
        print(re.findall('Mr. [A-Za-z]{1,}',i))
'''
#34. WAP to get company name which is giving highest salary?#['Wipro Company']
'''
maxNum = max([int(i[0].replace(' salary','')) for i in [re.findall('[0-9]{1,} salary',i) for i in data.split(',')]])
print(maxNum)

for i in data.split(','):
    x = re.findall('[0-9]{1,} salary',i)[0].replace(' salary','')
    if int(x) == maxNum:
        print(re.findall('[A-Za-z]{1,} Company',i))
'''
#35. WAP to get student name who learned language and placed in HCL Company?#['Mr. Suresh']
'''
m=data.split(',')
for i in m:
    if 'Language' in i and 'HCL' in i:
        print(re.findall('M[rs]. [A-Za-z]{1,}',i))
'''        
#36. WAP to get student name who leanred database and getting more then 10000 salary?

#37. WAP to count total number of male students?#2
'''
print(len(re.findall('Mr. [A-Za-z]{1,}',data)))
'''
#38. WAP to count total number of courses?#6
'''
print(len(re.findall('[A-Za-z]{1,} Institute',data)))
'''
#39. WAP to get all unique company names?#{'HCL Company', 'Wipro Company', 'CTS Company', 'TCS Company'}
'''
print(set(re.findall('[A-Za-z]{1,} Company',data)))
'''
#40. WAP to get course name of student whose name starts with s character?
'''
m=data.split(',')
for i in m:
    x=re.findall('Mr?s?. [A-Za-z]{1,}',i)
    for j in x:
        if j.split(' ')[1][0]== 'S':
            print([j.replace('learned','')for j in re.findall('learned [A-Za-z]{1,}',i)])
'''

#41. WAP to get students names and their institute names in dict?
        #{'Mr. Kumar': 'NTH ', 'Mr. Suresh': 'ABC ', 'Ms. Kavya': 'NTH ', 'Mrs. Navya': 'XYZ ', 'Ms. Bavya': 'NTH ', 'Mrs. Sravya': 'ABC '}
'''
w1=re.findall('M[rs]{1,2}. [A-Za-z]{1,}',data)
w2=[i.replace('Institute','')for i in re.findall('[A-Za-z]{1,} Institute',data)]
print(w1)
print(w2)
d={}
for k,v in zip(w1,w2):
    d[k]=v
print(d)
'''
#42. WAP to get instutitu names and company names in dict?#{'NTH': 'CTS', 'ABC': 'Wipro', 'XYZ': 'TCS'}
'''
w1=[i.replace(' Institute','')for i in re.findall('[A-Za-z]{1,} Institute',data)]
w2=[i.replace(' Company','')for i in re.findall('[A-Za-z]{1,} Company',data)]
d={}
for k,v in zip(w1,w2):
    d[k]=v
print(d)
'''
#43. WAP to get company name and thier employees count in dict?#{'TCS': 2, 'Wipro': 2, 'CTS': 1, 'HCL': 1}
'''
companies=[i.replace(' Company','')for i in re.findall('[A-Za-z]{1,} Company',data)]
emps=re.findall('M[rs]{1,2}. [A-Za-z]{1,}',data)
com=list(set(companies))
cnt=[]
for i in com:
    cnt.append(data.count(i))
d={}

for i,j in zip(com,cnt):
    d[i]=j
print(d)
'''
#44. WAP to get employee name and his company name who is getting least salary?#10000['Mrs. Navya']['TCS Company']
''' 
minNum = min([int(i[0].replace(' salary','')) for i in [re.findall('[0-9]{1,} salary',i) for i in data.split(',')]])
print(minNum)

for i in data.split(','):
    x = re.findall('[0-9]{1,} salary',i)[0].replace(' salary','')
    if int(x) == minNum:
        print(re.findall('M[r]?s. [A-Za-z]{1,}',i)) 
        print(re.findall('[A-Za-z]{1,} Company',i))
'''        
#45. WAP to get institute of employee who name ends with 'a' character?
                                            #['NTH Institute']['XYZ Institute']['NTH Institute']['ABC Institute']
'''
m=data.split(',')
for i in m:
    x=re.findall('Mr?s?. [A-Za-z]{1,}',i)
    for j in x:
        if j.split(' ')[1][-1]== 'aA':
            print([j.replace('Insitute','')for j in re.findall('[A-Za-z]{1,} Institute',i)])
'''
#46. WAP to get all unique slaries?#{'25000 ', '30000 ', '90000 ', '20000 ', '10000 '}
'''
print(set(i.replace('salary','')for i in re.findall('[0-9]{1,} salary',data)))
'''
#47. WAP to get female student name who did not learn data bases course?.......
'''
m=data.split(',')
for i in m:
    if 'Database'not in i and'M[r]?s. ' in i:
        print(re.findall(('M[r]?s. [A-Za-z]{1,}',i)))
'''
'''
print([i.replace('Database','')for i in re.findall('[A-Za-z]{1,} Database',data)if 'Database'not in i and'M[r]?s. ' in i])
'''
#48. WAP to get student name who learned the course which name is short?............
# a = min([i.replace('learned ','') for i in re.findall('learned [A-Za-z]{1,}[+]*',data.lower())])
# b = data.split('\n')
# print(b)
# l = []
# for i in b:
#     for j in i:
#         if j == a: 
#             l.append(i)
# print(l)



#49. WAP to get both male and female students who is getting highest salaries?#90000['Mrs. Sravya']
'''
maxNum = max([int(i[0].replace(' salary','')) for i in [re.findall('[0-9]{1,} salary',i) for i in data.split(',')]])
print(maxNum)

for i in data.split(','):
    x = re.findall('[0-9]{1,} salary',i)[0].replace(' salary','')
    if int(x) == maxNum:
        print(re.findall('M[rs]{1,2}. [A-Za-z]{1,}',i))
'''
#50. WAP to female unmarried student who is getting highest salary?#30000['Ms. Bavya']

x=[re.findall('[0-9]{1,} salary',i) for i in data.split(',')if 'Ms. 'in i]
sal=[]
for i in x:
    sal.append(int(i[0].replace(' salary','')))
maxSal=max(sal)
print(maxSal)
y=[re.findall('Ms. [A-Za-z]{1,}',i) for i in data.split(',')if str(maxSal)in i and 'Ms. 'in i][0]
print(y)





'''
try:
    print('a1')
    try:
        print('a2')
    except:
        print('a3')
    else:
        print('a4')
    finally:
        print('a5')
except:
    print('b1')
    try:
        print('b2')
    except:
        print('b3')
    else:
        print('b4')
    finally:
        print('b5')
else:
    print('c1'/10)
finally:
    print('d1')
'''
