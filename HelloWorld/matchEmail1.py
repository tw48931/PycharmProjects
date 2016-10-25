import re

format = re.compile(r'^<([A-Z][a-z]*\s[A-Z][a-z]*)>\s[a-zA-Z_.]+@[a-zA-Z0-9]+.(org|com|cn)$')

my_email = raw_input('Please enter your email:')

m = format.match(my_email)

if m:
    print 'name is %s' % m.group(1)
else:
    print 'Error.'