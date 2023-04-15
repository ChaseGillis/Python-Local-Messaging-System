"""
Chase Gillis  4/13/23	CSCI-UA 2 - 006
Assignment #9 Part #1
Email Service
"""
import datetime
d = datetime.datetime.now()
month = d.month
day = d.day
year = d.year
hour = d.hour
minute = d.minute
second = d.second


# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)
def valid_username(x):
    if len(x)>4 and x.isalnum() and not x[0].isdigit():
        return True
    else:
        return False
'''
# TESTER CODE
print( valid_username('abc123') )    # True
print( valid_username('abcde')  )    # True
print( valid_username('abc')    )    # False
print( valid_username('@#$%^')  )    # False
print( valid_username('1abcde') )    # False
print( valid_username('')       )    # False'''

# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) must contain at least one lowercase letter
#             (4) must contain at least one uppercase letter
#             (5) must contain at least one number
# output:     boolean (True if valid, False if invalid)
def valid_password(x):
    low = 0
    dig = 0
    up = 0
    if len(x)>4 and x.isalnum():
        for i in x:
            if i.islower():
                low +=1
                for i in x:
                    if i.isdigit():
                        dig +=1
                        for i in x:
                            if i.isupper():
                                up += 1
    if low > 0 and dig > 0 and up > 0:
        return True
    else:
        return False

'''
# TESTER CODE
print( valid_password('Abc123')     )   # True
print( valid_password('Abc123xyz')  )   # True
print( valid_password('Ab12')       )   # False
print( valid_password('abc123')     )   # False
print( valid_password('123456')     )   # False
print( valid_password('Abc123#')    )   # False
print( valid_password('')           )   # False'''

# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)
def username_exists(x):
    alluser=[]
    file = open('user_info.txt', 'r')
    data = file.read()
    data_list = data.split('\n')
    for line in data_list:
        newlist = line.split(',')
        alluser.append(newlist[0])
    if x in alluser:
        return True
    else:
        return False

'''
# TESTER CODE
print( username_exists('pikachu')           )   # True
print( username_exists('charmander')        )   # True
print( username_exists('squirtle')          )   # True
print( username_exists('Pidgey2020')        )   # True
print( username_exists('SquirtleSquad99')   )   # False
print( username_exists('eevee')             )   # False
print( username_exists('bobcat')            )   # False
print( username_exists('')                  )   # False'''

# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)
def check_password(x,y):
    alluser = []
    allpass = []
    file = open('user_info.txt', 'r')
    data = file.read()
    data_list = data.split('\n')
    for line in data_list:
        newlist = line.split(',')
        alluser.append(newlist[0])
        allpass.append(newlist[1])
    if x in alluser and y in allpass:
        if alluser.index(x) == allpass.index(y):
            return True
        else:
            return False
    else:
        return False
'''
# TESTER CODE
print( check_password('pikachu', 'Abc123')              )    # True
print( check_password('squirtle', 'SquirtleSquad99')    )    # True
print( check_password('fearow', 'Pqr123')               )    # False
print( check_password('foobar', 'Hello123')             )    # False
print( check_password('', '')                           )    # False'''

# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)
def add_user(username, password):
    if valid_username(username):
        if valid_password(password):
            if username_exists(username) == False:
                file = open('user_info.txt', 'a')
                file.write('\n' + username + ',' + password)
                #ALWAYS CLOSE FILE
                file.close()
                print('Added user!')
                # opens a new file named 'somefile.txt' for writing inside of the 'messages' folder
                send_message('admin', username, 'Welcome to your account!')
                return True
            else:
                return False
        else:
            return False
    else:
        return False

'''
# TESTER CODE
add_user('foobar', 'abcABC123')
add_user('barfoo', 'xyz123ABC')
add_user('foobar', 'aTest123') # this should fail

# OUTPUT - check 'user_info.txt' to ensure that that two new accounts have been created'''

# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
#
#             for example, if you call this function using the following arguments:
#
#             send_message('craig', 'pikachu', 'Hello there! nice to see you!')
#
#             the file 'messages/pikachu.txt' should gain an additional line data
#             that looks like the following:
#
#             craig|11/14/2020 12:30:05|Hello there! nice to see you!\n
#
#             note that you can generate the current time by doing the following:
#
#             import datetime
#             d = datetime.datetime.now()
#             month = d.month
#             day = d.day
#             year = d.year
#             ... etc. for hour, minute and second
#
#             keep in mind that you may need to 'append' to the correct messages file
#             since a user can receive an unlimited number of messages.  you may also
#             need to create a new message file if one does not exist for a user.
# output:     nothing
def send_message(sender,recipient,message):
    file = open('messages/'+ recipient +'.txt', 'a')
    file.write(sender + ' | ' + str(d) + ' | ' + message + "\n")
    file.close()


'''
# TESTER CODE
send_message('pikachu', 'charmander', 'Hey there!')
send_message('charmander', 'pikachu', 'Good to see you!')
send_message('pikachu', 'charmander', 'You too, ttyl')'''

# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.  assume you have this file named 'pikachu.txt':
#
#             charmander|11/14/2020 13:37:15|Hey there!
#             charmander|11/14/2020 13:37:15|You too, ttyl
#
#             this function should generate the following output:
#
#             Message #1 received from charmander
#             Time: 11/14/2020 13:37:15
#             Hey there!
#
#             Message #2 received from charmander
#             Time: 11/14/2020 13:37:15
#             You too, ttyl
# output:     no return value (simply prints the messages)
def print_messages(username):
    accumulator = 0
    file = open('messages/'+username + ".txt", 'r')
    data = file.read()
    dataset = data.split('\n')
    for line in dataset:
        message = line.split(' | ')
        accumulator += 1
        if len(message)>1:
            print('Message #' + str(accumulator) + ' recieved from ' + message[0])
            print('Time: ' + message[1])
            print(message[2])
            print()
        elif len(message)<=1 and line == dataset[0]:
            print('No messages in your inbox')
            print()

# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value
def delete_messages(username):
    file = open('messages/'+username+'.txt', 'w')
    file.close()



#Actual Program
while True:
    decision = input('(l)ogin, (r)egister or (q)uit: ')
    if decision == 'q':
        print()
        print('Goodbye!')
        break
    elif decision == 'l':
        while True:
            print('Login')
            username = input('Username (case sensitive): ')
            password = input('Password (case sensitive): ')
            if check_password(username, password):
                while True:
                        print('You have been logged in successfully as', username)
                        decision2 = input('(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ')
                        if decision2 == 'r':
                            print()
                            print_messages(username)
                        elif decision2 == 's':
                            recipient = input('Username of recipient: ')
                            message = input('Type your message: ')
                            send_message(username, recipient, message)
                            print('Message sent!')
                            print()
                        elif decision2 == 'd':
                            delete_messages(username)
                            print('Your messages have been deleted')
                            print()
                        elif decision2 == 'l':
                            print('Logging out as username', username)
                            print()
                            break
                        else:
                            print('Invalid input')
                break
            else:
                print('Invalid username or password.')
    elif decision == 'r':
        print('Register for an account')
        username = input('Username (case sensitive): ')
        password = input('Password (case sensitive): ')
        if username_exists(username):
            print('Duplicate username, registration cancelled')
            print()
        elif not valid_username(username):
            print('Username is invalid, registration cancelled')
            print()
        elif not valid_password(password):
            print('Password is invalid, registration cancelled')
            print()
        if add_user(username, password):
            print('Registration successful!')
            print()
    else:
        print('Invalid input, please try again')
