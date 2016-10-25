import re

my_email = raw_input('Please enter your email >')
format = re.compile(r'^[0-9a-zA-Z_.]+@(microsoft|gmail)\.com$')

if format.match(my_email):
    print 'The format of your email is correct.'
else:
    print 'Error.'

