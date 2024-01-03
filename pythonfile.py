# x = open('pavan.txt','w').write('TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas\nINFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra\nWIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna')
# print(x)



n = eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,i+2):
        print(' ', end=' ')
    for k in range(1,n+2-i):
        print('*', end = (' '))
    print()