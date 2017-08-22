"""
2. Woefully inadequate security checker…

Copy the following list of usernames into a new Python file:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

Ask the user for their username. If the username is in the above list of authorised users, print “Access
granted”, otherwise print “Access denied”.

"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = str(input("Please enter username: "))
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
