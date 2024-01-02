# Social Media Project

existing_users={
    'pyhtonsai':{'first_name':'sai','last_name':'Python','user_name':'pythonsai','password':'python@1234','confirm_password':'python@1234','mobile':8464002165},
    'djangonani':{'first_name':'nani','last_name':'django','user_name':'djangonani','password':'django@1234','confirm_password':'django@1234','mobile':9010607012},
    'uisatya':{'first_name':'satya','last_name':'uisatya','user_name':'uisatya','password':'uisatya@1234','confirm_password':'uisatya@1234','mobile':8464001122},
}

#Registration
keys = ['first_name','last_name','user_name','password','confirm_password','mobile']
values = []

new_user = {}

while True:
    reg_user = input('Enter Your Username: ') #sudarsan
    
    if reg_user in existing_users:
        print('{} is already taken, please choose another name'.format(reg_user))
        continue
    else:
        while True:
            pwd1 = input('Enter Your Password: ')
            pwd2 = input('Enter Your Confirm Password: ')
            if pwd1 != pwd2:
                print('Passwords are mismatched, please enter same passwords')
                continue
            else:
                fname = input('Enter First Name: ')
                Iname = input('Enter Last Name: ')
                mobile = eval(input('Enter Mobile Number: '))
        
                values.append(fname)
                values.append(Iname)
                values.append(reg_user)
                values.append(pwd1)
                values.append(pwd2)
                values.append(mobile)
        
            for k,v in zip(keys, values):
                new_user[k] = v
            
            existing_users[reg_user] = new_user
        
            print('Registration success')
            print(existing_users)
            break
        break

print()
print()
#Login Opreation

while True:
    login_user = input('Enter Your Username: ')
    
    if login_user not in existing_users:
        print('{} is invalid user, please enter valid username'.format(login_user))
        continue
    else:
        while True:
            pwd = input('Enter Your Password: ')
            if existing_users[login_user]['password'] != pwd:
                print('Invalid Password, please correct password')
                continue
            else:
                print('Login Success!!!')
                break
        break
print()
print()


# Updation Password

while True:
    login_user = input('Enter Your Username: ')
    
    if login_user not in existing_users:
        print('{} is invalid user, please enter valid username'.format(login_user))
        continue
    else:
        while True:
            updated_pwd =  input('Enter Your updated Password: ')
            if existing_users[login_user]['password'] == updated_pwd:
                print('Entered password is same as old password')
                continue
            else:
                
                cnfrm_password = input("Confirm password: ")
                if updated_pwd == cnfrm_password:
                    existing_users[login_user]['password'] = updated_pwd
                    existing_users[login_user]['confirm_password'] = cnfrm_password
                    print("Password updated successfully")
                    print(existing_users)
                else:
                    print("Passwords did not match")
                break
        break
    

#Deleting the account
                    
while True:
    login_user = input('Enter Your Username: ')
    
    if login_user not in existing_users:
        print('{} is invalid user, please enter valid username'.format(login_user))
        continue
    else:
        while True:
            reg_users=list(existing_users.keys())
            if login_user in reg_users:
                del existing_users[login_user]
            print(existing_users)
            break
        break
                
                
               