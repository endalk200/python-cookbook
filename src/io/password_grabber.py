"""
CLI Password Grabber.
@author: endalk200

gets the users password in a safe way in a command line tool. It
prompts the user for the password but does not echo the password
into the standard input output stream.
"""
import getpass

# Gets the user. (For computer user)
user = getpass.getuser()
passwd = getpass.getpass()

print('User:', user)
print('Passwd:', passwd)